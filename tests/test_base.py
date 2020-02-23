# encoding: utf-8

import pytest
from mynt import base

class TestParser():
    def test_empty_object(self):
        parser = base.Parser()
        assert isinstance(parser, base.Parser)
        assert parser.options == {}
        with pytest.raises(NotImplementedError):
            parser.parse("")

    def test_object_with_options(self):
        parser = base.Parser("foo")
        assert parser.options == "foo"
        parser = base.Parser(["foo", "bar"])
        assert parser.options == ["foo", "bar"]
        parser = base.Parser({"foo": "bar"})
        assert parser.options == {"foo": "bar"}


class TestRenderer():
    def test_empty_object(self):
        renderer = base.Renderer("/foo/bar")
        assert isinstance(renderer, base.Renderer)
        assert renderer.path == "/foo/bar"
        assert renderer.options == {}
        assert renderer.globals == {}
        with pytest.raises(NotImplementedError):
            renderer.from_string("")
        with pytest.raises(NotImplementedError):
            renderer.register("foo", "bar")
        with pytest.raises(NotImplementedError):
            renderer.render("foo.html")

    def test_object_with_params(self):
        renderer = base.Renderer("/foo/bar", {"foo": "bar"}, {"bar": "foo"})
        assert isinstance(renderer, base.Renderer)
        assert renderer.path == "/foo/bar"
        assert renderer.options == {"foo": "bar"}
        assert renderer.globals == {"bar": "foo"}

