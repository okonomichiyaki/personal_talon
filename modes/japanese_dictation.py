from talon import Module, Context, speech_system
from talon.engines.webspeech import WebSpeechEngine

webspeech = WebSpeechEngine()
speech_system.add_engine(webspeech)

mod = Module()
mod.mode("japanese", desc="Japanese dictation mode")
