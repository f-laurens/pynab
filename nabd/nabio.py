import abc
import asyncio
from .choreography import ChoreographyInterpreter

class NabIO(object, metaclass=abc.ABCMeta):
  """ Interface for I/O interactions with a nabaztag """

  async def setup_ears(self, left_ear, right_ear):
    """
    Init ears and setup them to the initial position.
    """
    raise NotImplementedError( 'Should have implemented' )

  def set_ears(self, left_ear, right_ear):
    """ Set the position of ears (left & right) """
    raise NotImplementedError( 'Should have implemented' )

  def set_leds(self, left, center, right, nose, bottom):
    """ Set the leds. None means to turn them off. """
    raise NotImplementedError( 'Should have implemented' )

  def bind_button_event(self, loop, callback):
    """
    Define the callback for button events.
    callback is cb(event_type) with event_type being:
    - 'down'
    - 'up'
    - 'click'
    - 'doubleclick'

    Make sure the callback is called on the provided event loop, with loop.call_soon_threadsafe
    """
    raise NotImplementedError( 'Should have implemented' )

  def bind_ears_event(self, loop, callback):
    """
    Define the callback for ears events.
    callback is cb(left_ear, right_ear) with left_ear and right_ear being the positions.

    Make sure the callback is called on the provided event loop, with loop.call_soon_threadsafe
    """
    raise NotImplementedError( 'Should have implemented' )

  async def play_info(self, tempo, colors):
    """
    Play an info animation.
    tempo & colors are as described in the nabd protocol.
    Run the animation once and returns.

    If 'left'/'center'/'right'/'bottom'/'nose' slots are absent, the light is off.
    """
    raise NotImplementedError( 'Should have implemented' )

  async def play_sequence(self, sequence):
    preloaded = await self.preload(sequence)
    for seq_item in preloaded:
      if 'audio' in seq_item:
        audio_task_list = [self.sound.play_list(seq_item['audio'], True)]
      else:
        audio_task_list = []
      if 'choreography' in seq_item:
        ci = ChoreographyInterpreter(self.leds, self.ears, self.sound)
        choeography_task_list = [ci.play(seq_item['choreography'])]
      else:
        choeography_task_list = []
      if audio_task_list + choeography_task_list != []:
        await asyncio.wait(audio_task_list + choeography_task_list)

  async def preload(self, sequence):
    preloaded_sequence = []
    for seq_item in sequence:
      if 'audio' in seq_item:
        preloaded_audio_list = []
        for res in seq_item['audio']:
          f = await self.sound.preload(res)
          if f != None:
            preloaded_audio_list.append(f)
        seq_item['audio'] = preloaded_audio_list
      preloaded_sequence.append(seq_item)
    return preloaded_sequence

  def cancel(self):
    """
    Cancel currently running sequence or info animation.
    """
    raise NotImplementedError( 'Should have implemented' )
