# encoding: utf-8

import logging
import pytest
from mynt import utils
from os import path
import time

class TestCleanpath():
    def test_empty(self):
        with pytest.raises(TypeError):
            utils._cleanpath(*None)

    def test_empty_string(self):
        with pytest.raises(IndexError):
            utils._cleanpath(*"")

    def test_empty_list(self):
        with pytest.raises(IndexError):
            utils._cleanpath(*[])

    def test_list_of_integers(self):
        with pytest.raises(AttributeError):
            utils._cleanpath(*[1, 2, 3, 4])

    def test_clean_strings(self):
        assert utils._cleanpath(
            *["foo", "bar"]
        ) == ["foo", "bar"]

    def test_bad_strings(self):
        assert utils._cleanpath(
            *[
                " foo/ ",
                "\t\nbar/foobar/ ",
                "  \t\n\r\v\f" + path.sep + "bar/foo  \t\n\r\v\f" + path.sep,
            ]
        ) == ["foo/", "bar/foobar", "bar/foo"]


class TestAbspath():
    def test_empty(self):
        with pytest.raises(TypeError):
            utils.abspath(*None)

    def test_empty_string(self):
        with pytest.raises(IndexError):
            utils.abspath(*"")

    def test_empty_list(self):
        with pytest.raises(IndexError):
            utils.abspath(*[])

    def test_list_of_integers(self):
        with pytest.raises(AttributeError):
            utils.abspath(*[1, 2, 3, 4])

    def test_clean_strings(self):
        assert utils.abspath(
            *["foo", "bar"]
        ) == path.realpath(
            path.expanduser(
                path.join(
                    *["foo", "bar"]
                )
            )
        )

    def test_bad_strings(self):
        assert utils.abspath(
            *[
                " foo/ ",
                "\t\nbar/foobar/ ",
                "  \t\n\r\v\f" + path.sep + "bar/foo  \t\n\r\v\f" + path.sep,
            ]
        ) == path.realpath(
            path.expanduser(
                path.join(
                    *["foo/", "bar/foobar", "bar/foo"]
                )
            )
        )

class TestNormpath():
    def test_empty(self):
        with pytest.raises(TypeError):
            utils.normpath(*None)

    def test_empty_string(self):
        with pytest.raises(IndexError):
            utils.normpath(*"")

    def test_empty_list(self):
        with pytest.raises(IndexError):
            utils.normpath(*[])

    def test_list_of_integers(self):
        with pytest.raises(AttributeError):
            utils.normpath(*[1, 2, 3, 4])

    def test_clean_strings(self):
        assert utils.normpath(
            *["foo", "bar"]
        ) == path.normpath(
            path.join(
                *["foo", "bar"]
            )
        )

    def test_bad_strings(self):
        assert utils.normpath(
            *[
                " foo/ ",
                "\t\nbar/foobar/ ",
                "  \t\n\r\v\f" + path.sep + "bar/foo  \t\n\r\v\f" + path.sep,
            ]
        ) == path.normpath(
            path.join(
                *["foo/", "bar/foobar", "bar/foo"]
            )
        )

class TestEscape():
    def test_empty(self):
        with pytest.raises(AttributeError):
            utils.escape(None)

    def test_empty_string(self):
        assert utils.escape("") == ""

    def test_normal_string(self):
        assert utils.escape("foo") == "foo"

    def test_entity_string(self):
        assert utils.escape("foo & bar") == "foo &amp; bar"

    def test_multiple_entities(self):
        assert utils.escape(
            '''"foo" & <bar> Rock'n'Roll /o/'''
        ) == "&quot;foo&quot; &amp; &lt;bar&gt; Rock&#x27;n&#x27;Roll &#x2F;o&#x2F;"

class TestUnescape():
    def test_empty(self):
        with pytest.raises(AttributeError):
            utils.unescape(None)

    def test_empty_string(self):
        assert utils.unescape("") == ""

    def test_normal_string(self):
        assert utils.unescape("foo & bar") == "foo & bar"

    def test_entity_string(self):
        assert utils.unescape("foo &amp; bar") == "foo & bar"

    def test_multiple_entities(self):
        assert utils.unescape(
            "&quot;foo&quot; &amp; &lt;bar&gt; Rock&#x27;n&#x27;Roll &#x2F;o&#x2F;"
        ) == '''"foo" & <bar> Rock'n'Roll /o/'''

class TestGetLogger():
    def test_empty_names(self):
        names = (
            None,
            "",
        )
        for name in names:
            logger = utils.get_logger(name)
            assert isinstance(logger, logging.RootLogger)

    def test_multiple_names(self):
        names = (
            "foo",
            "foo & bar",
        )
        for name in names:
            logger = utils.get_logger(name)
            assert isinstance(logger, logging.Logger)


class TestTimer():
    def test_no_queue(self):
        with pytest.raises(IndexError):
            utils.Timer.stop()

    def test_queue(self):
        assert len(utils.Timer._start) == 0
        utils.Timer.start()
        assert len(utils.Timer._start) == 1
        utils.Timer.start()
        assert len(utils.Timer._start) == 2
        utils.Timer.start()
        assert len(utils.Timer._start) == 3
        utils.Timer.stop()
        assert len(utils.Timer._start) == 2
        utils.Timer.stop()
        assert len(utils.Timer._start) == 1
        utils.Timer.stop()
        assert len(utils.Timer._start) == 0

    def test_object(self):
        start = time.time()
        utils.Timer.start()
        time.sleep(.1)
        result = utils.Timer.stop()
        assert result <= (time.time() - start)

    def test_double_object(self):
        start = time.time()
        utils.Timer.start()
        utils.Timer.start()
        time.sleep(.1)
        result = utils.Timer.stop()
        assert result <= (time.time() - start)
        time.sleep(.3)
        result = utils.Timer.stop()
        assert result <= (time.time() - start)


class TestUrl():
    def test_join(self):
        url = utils.Url()
        assert url.join("foo") == "/foo"
        assert url.join("foo", "bar") == "/foo/bar"
        assert url.join("/foo/", "/bar/") == "/foo/bar/"
        assert url.join("http://foo", "bar") == "http://foo/bar"
        assert url.join("https://foo", "bar") == "https://foo/bar"
        assert url.join("anything://foo", "bar/") == "anything://foo/bar/"

    def test_slugify(self):
        url = utils.Url()
        assert url.slugify("this is a test  ") == "this-is-a-test"
        # Maybe this one should be cleaned ?
        assert url.slugify("This is a #&!:? test  ") == "This-is-a--test"

    def test_format(self):
        assert utils.Url.format("foo", False) == "foo.html"
        assert utils.Url.format("foo/bar", False) == "foo/bar.html"
        assert utils.Url.format("https://foo/bar/", False) == "https://foo/bar/.html"
        assert utils.Url.format("foo", True) == "/foo/"
        assert utils.Url.format("foo/bar", True) == "/foo/bar/"
        assert utils.Url.format("https://foo/bar/", True) == "https://foo/bar/"

    def test_from_path(self):
        assert utils.Url.from_path("root", "text") == "root/text.html"
        assert utils.Url.from_path("/path/folder/", "document") == "/path/folder/document.html"
