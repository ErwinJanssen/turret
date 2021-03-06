# -*- coding: utf-8 -*-

"""Unit tests for the `Program` class."""

from pytest import raises

from turret.core.extenders import Program

test_name = 'ls'


def test_defaults():
    """Verify that the __init__ function sets certain defaults."""
    program = Program(test_name)
    assert program.arguments == list()
    assert program.show_help is False
    assert program.help_option == '--help'
    assert program.show_version is False
    assert program.version_option == '--version'
    assert program.command == [test_name]


def test_command_read_only():
    """The `command` attribute should be read-only, assignment should fail."""
    program = Program('some_name')
    with raises(AttributeError):
        program.command = 'This assignment must fail'


def test_help_options():
    """Test if the `show_help` options behaves as expected."""
    program = Program(test_name, show_help=True, help_option='-h')
    assert program.command == [test_name, '-h']
    program.help_option = '--show-help'
    assert program.command == [test_name, '--show-help']


def test_version_options():
    """Test if the `show_version` options behaves as expected."""
    program = Program(test_name, show_version=True, version_option='-V')
    assert program.command == [test_name, '-V']
    program.version_option = '--show-version'
    assert program.command == [test_name, '--show-version']


def test_arguments():
    """Arguments should be appended to the command, also when changed."""
    program = Program(test_name, ['some', 'arguments'])
    assert program.arguments == ['some', 'arguments']
    assert program.command == [test_name, 'some', 'arguments']

    program.arguments = ['something', 'else']
    assert program.arguments == ['something', 'else']
    assert program.command == [test_name, 'something', 'else']


def test_run():
    """Program.run() should return a completed program."""
    program = Program(test_name)
    assert program.run().returncode is 0
    program = Program(test_name, show_help=True)
    assert program.run().returncode is 0
    program = Program(test_name, show_version=True)
    assert program.run().returncode is 0


def test_completed_program():
    """Test that the attributes of CompletedProgram are properly set."""
    program = Program(test_name, ['-al'])
    completed = program.run()
    assert completed.args == ['ls', '-al']
    assert completed.returncode == 0
    assert isinstance(completed.output['stdout'], bytes)
    assert completed.output['stderr'] == b''
