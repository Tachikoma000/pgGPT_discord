import pytest
import unittest.mock as mock
from discord.ext.commands import Context
from bot_v1.bot_commands import setup

def test_ask_command():
    # Mock a Context object
    ctx = mock.MagicMock(spec=Context)
    
    # Test a simple case
    setup(ctx, question="What is Subgrounds?")
    
    # Check that the bot sent a message
    ctx.send.assert_called_once()
    
    # Reset the mock for the next test
    ctx.reset_mock()
    
    # Test an error case
    setup(ctx, question="")
    
    # Check that the bot sent an error message
    ctx.send.assert_called_once()
