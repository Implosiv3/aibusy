"""
A simple test to verify that pytes is working and
the tests are being detected.
"""
import pytest


@pytest.mark.mandatory
def test_classes():
    from aibusy.engine.engine import Engine
    from aibusy.engine.builder import EngineBuilder
    from aibusy.engine.settings import EngineSettings

    
    builder = EngineBuilder()
