"""
This module defines a built-in contrib module that enables embedding gifs as
ascii animations within a slide.
"""


from marshmallow import fields, Schema
import re
import shlex
import urwid
import yaml


import lookatme.render
from lookatme.exceptions import IgnoredByContrib
import lookatme.config


def user_warnings():
    """Provide warnings to the user that loading this extension may cause
    shell commands specified in the markdown to be run.
    """
    return []


class YamlRender:
    def loads(data): return yaml.safe_load(data)
    def dumps(data): return yaml.safe_dump(data)


class TerminalExSchema(Schema):
    """The schema used for ``tai`` code blocks.
    """
    command = fields.Str()
    rows = fields.Int(default=10, missing=10)
    init_text = fields.Str(default=None, missing=None)
    init_wait = fields.Str(default=None, missing=None)
    init_codeblock = fields.Bool(default=True, missing=True)
    init_codeblock_lang = fields.Str(default="text", missing="text")

    class Meta:
        render_module = YamlRender


CREATED_TERMS = []


def render_code(token, body, stack, loop):
    lang = token["lang"] or ""

    numbered_term_match = re.match(r'tai(\d+)', lang)
    if numbered_term_match is None:
        raise IgnoredByContrib

    term_data = TerminalExSchema().load({
        "command": 'tai ' + token["text"].strip(),
        "rows": int(numbered_term_match.group(1)),
        "init_codeblock": False,
    })

    term = urwid.Terminal(
        shlex.split(term_data["command"].strip()),
        main_loop=loop,
        encoding="utf8",
    )
    CREATED_TERMS.append(term)

    box = urwid.WidgetDisable(urwid.BoxAdapter(term, height=term_data["rows"]))
    box.no_cache = ["render"]

    res = []

    if term_data["init_codeblock"] is True:
        fake_token = {
            "text": term_data["init_text"],
            "lang": term_data["init_codeblock_lang"],
        }
        res += lookatme.render.markdown_block.render_code(
            fake_token, body, stack, loop
        )

    res += [
        urwid.Divider(),
        box,
        urwid.Divider(),
    ]

    return res


def shutdown():
    for idx, term in enumerate(CREATED_TERMS):
        lookatme.config.LOG.debug(f"Terminating terminal {idx+1}/{len(CREATED_TERMS)}")
        if term.pid is not None:
            term.terminate()
