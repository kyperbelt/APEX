from typing import ContextManager
import sounddevice as sd
import numpy as np
import queue
import pickle

class Sound_Source(ContextManager):
    """
    A sound source. Establishes an audio stream, and makes the input avaliable via a queue.SimpleQueue
    
    Requires the sounddevice libary
    Usage:
    Sound_Source.queue.get() for data in a 2d numpy array data
    See: https://docs.python.org/3/library/queue.html#queue.SimpleQueue for queue documentation
    
    Stream arguements are directly passed through via keyword
    See: https://python-sounddevice.readthedocs.io/en/0.4.6/api/streams.html#sounddevice.InputStream for stream arguements
    
    Example:
    with Sound_Source(channels=1) as source:
        while True:
            print(source.queue.get() )
    """
    def __init__(self, **kargs):
        self.queue = queue.SimpleQueue()
        
        if(not kargs.get("channels") ):
            kargs["channels"] = 1
        if(not kargs.get("callback") ):
            def callback(data : np.ndarray, frames : int, time, status : sd.CallbackFlags):
                self.queue.put(data)
            kargs["callback"] = callback
            
        self._stream = sd.InputStream(**kargs)
    
    def __enter__(self, **kwargs):
        self._stream.start()
        return self
        
    def __exit__(self, __exc_type, __exc_value,  __traceback):
        self._stream.stop()
