# encoding: utf-8

import pytest
from mynt import exceptions

class TestMyntException():
    def test_simple_object(self):
        exception = exceptions.MyntException("message")
        assert isinstance(exception, exceptions.MyntException)
        assert exception.code == 1
        assert exception.message == "message"
        assert exception.debug == ()
        assert str(exception) == "!! message"

    def test_object_with_args(self):
        exception = exceptions.MyntException("message", "foo", "bar")
        assert isinstance(exception, exceptions.MyntException)
        assert exception.code == 1
        assert exception.message == "message"
        assert exception.debug == ("foo", "bar")
        assert str(exception) == "!! message\n..  foo\n..  bar"

class TestConfigException():
    def test_simple_object(self):
        exception = exceptions.ConfigException("message", "foo", "bar")
        assert isinstance(exception, exceptions.ConfigException)
        assert exception.code == 1
        assert exception.message == "message"
        assert exception.debug == ("foo", "bar")
        assert str(exception) == "!! message\n..  foo\n..  bar"

class TestContentException():
    def test_simple_object(self):
        exception = exceptions.ContentException("message", "foo", "bar")
        assert isinstance(exception, exceptions.ContentException)
        assert exception.code == 1
        assert exception.message == "message"
        assert exception.debug == ("foo", "bar")
        assert str(exception) == "!! message\n..  foo\n..  bar"

class TestFileSystemException():
    def test_simple_object(self):
        exception = exceptions.FileSystemException("message", "foo", "bar")
        assert isinstance(exception, exceptions.FileSystemException)
        assert exception.code == 1
        assert exception.message == "message"
        assert exception.debug == ("foo", "bar")
        assert str(exception) == "!! message\n..  foo\n..  bar"

class TestOptionException():
    def test_simple_object(self):
        exception = exceptions.OptionException("message", "foo", "bar")
        assert isinstance(exception, exceptions.OptionException)
        assert exception.code == 2
        assert exception.message == "message"
        assert exception.debug == ("foo", "bar")
        assert str(exception) == "!! message\n..  foo\n..  bar"

class TestParserException():
    def test_simple_object(self):
        exception = exceptions.ParserException("message", "foo", "bar")
        assert isinstance(exception, exceptions.ParserException)
        assert exception.code == 1
        assert exception.message == "message"
        assert exception.debug == ("foo", "bar")
        assert str(exception) == "!! message\n..  foo\n..  bar"

class TestRendererException():
    def test_simple_object(self):
        exception = exceptions.RendererException("message", "foo", "bar")
        assert isinstance(exception, exceptions.RendererException)
        assert exception.code == 1
        assert exception.message == "message"
        assert exception.debug == ("foo", "bar")
        assert str(exception) == "!! message\n..  foo\n..  bar"
