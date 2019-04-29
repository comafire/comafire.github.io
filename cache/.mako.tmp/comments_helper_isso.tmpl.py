# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1556543523.2912743
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl'
_template_uri = 'comments_helper_isso.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'comment_link_script', 'comment_form']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <a href="')
            __M_writer(str(link))
            __M_writer('#isso-thread">Comments</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id and 'index' in pagekind:
            __M_writer('        <script src="')
            __M_writer(str(comment_system_id))
            __M_writer('js/count.min.js" data-isso="')
            __M_writer(str(comment_system_id))
            __M_writer('" data-isso-lang="')
            __M_writer(str(lang))
            __M_writer('"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        isso_config = context.get('isso_config', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <div data-title="')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('" id="isso-thread"></div>\n        <script src="')
            __M_writer(str(comment_system_id))
            __M_writer('js/embed.min.js" data-isso="')
            __M_writer(str(comment_system_id))
            __M_writer('" data-isso-lang="')
            __M_writer(str(lang))
            __M_writer('"\n')
            if isso_config:
                for k, v in isso_config.items():
                    __M_writer('        data-isso-')
                    __M_writer(str(k))
                    __M_writer('="')
                    __M_writer(str(v))
                    __M_writer('"\n')
            __M_writer('        ></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "comments_helper_isso.tmpl", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl", "line_map": {"65": 2, "86": 8, "72": 2, "73": 3, "74": 4, "75": 4, "76": 4, "77": 5, "78": 5, "79": 5, "16": 0, "81": 5, "82": 5, "83": 6, "84": 7, "21": 13, "22": 19, "23": 26, "88": 8, "89": 8, "90": 11, "29": 15, "96": 90, "80": 5, "34": 15, "35": 16, "36": 17, "37": 17, "38": 17, "44": 22, "87": 8, "51": 22, "52": 23, "53": 24, "54": 24, "55": 24, "56": 24, "57": 24, "58": 24, "59": 24, "85": 8}}
__M_END_METADATA
"""
