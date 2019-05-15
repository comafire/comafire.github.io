# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1557934404.0273075
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/post_helper.tmpl'
_template_uri = 'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['twitter_card_information', 'mathjax_script', 'meta_translations', 'html_tags', 'html_pager', 'open_graph_metadata']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer('    <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(str(twitter_card.get('card', 'summary'))))
            __M_writer('">\n')
            if 'site:id' in twitter_card:
                __M_writer('    <meta name="twitter:site:id" content="')
                __M_writer(str(twitter_card['site:id']))
                __M_writer('">\n')
            elif 'site' in twitter_card:
                __M_writer('    <meta name="twitter:site" content="')
                __M_writer(str(twitter_card['site']))
                __M_writer('">\n')
            if 'creator:id' in twitter_card:
                __M_writer('    <meta name="twitter:creator:id" content="')
                __M_writer(str(twitter_card['creator:id']))
                __M_writer('">\n')
            elif 'creator' in twitter_card:
                __M_writer('    <meta name="twitter:creator" content="')
                __M_writer(str(twitter_card['creator']))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in sorted(translations):
                if langname != lang and ((not post.skip_untranslated) or post.is_translation_available(langname)):
                    __M_writer('                <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags:
            __M_writer('        <ul itemprop="keywords" class="tags">\n')
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer('            <li><a class="tag p-category" href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('" rel="tag">')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.prev_post or post.next_post:
            __M_writer('        <ul class="pager hidden-print">\n')
            if post.prev_post:
                __M_writer('            <li class="previous">\n                <a href="')
                __M_writer(str(post.prev_post.permalink()))
                __M_writer('" rel="prev" title="')
                __M_writer(filters.html_escape(str(post.prev_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Previous post")))
                __M_writer('</a>\n            </li>\n')
            if post.next_post:
                __M_writer('            <li class="next">\n                <a href="')
                __M_writer(str(post.next_post.permalink()))
                __M_writer('" rel="next" title="')
                __M_writer(filters.html_escape(str(post.next_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Next post")))
                __M_writer('</a>\n            </li>\n')
            __M_writer('        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs_link = context.get('abs_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<meta property="og:site_name" content="')
        __M_writer(filters.html_escape(str(blog_title)))
        __M_writer('">\n<meta property="og:title" content="')
        __M_writer(filters.html_escape(str(post.title()[:70])))
        __M_writer('">\n<meta property="og:url" content="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n')
        if post.description():
            __M_writer('    <meta property="og:description" content="')
            __M_writer(filters.html_escape(str(post.description()[:200])))
            __M_writer('">\n')
        else:
            __M_writer('    <meta property="og:description" content="')
            __M_writer(filters.html_escape(str(post.text(strip_html=True)[:200])))
            __M_writer('">\n')
        if post.previewimage:
            __M_writer('    <meta property="og:image" content="')
            __M_writer(str(url_replacer(permalink, post.previewimage, lang, 'absolute')))
            __M_writer('">\n')
        __M_writer('<meta property="og:type" content="article">\n')
        if post.date.isoformat():
            __M_writer('    <meta property="article:published_time" content="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('">\n')
        if post.tags:
            for tag in post.tags:
                __M_writer('       <meta property="article:tag" content="')
                __M_writer(filters.html_escape(str(tag)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "post_helper.tmpl", "source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/post_helper.tmpl", "line_map": {"23": 2, "26": 0, "31": 2, "32": 12, "33": 24, "34": 41, "35": 68, "36": 84, "37": 89, "43": 70, "48": 70, "49": 71, "50": 72, "51": 72, "52": 72, "53": 73, "54": 74, "55": 74, "56": 74, "57": 75, "58": 76, "59": 76, "60": 76, "61": 78, "62": 79, "63": 79, "64": 79, "65": 80, "66": 81, "67": 81, "68": 81, "74": 87, "79": 87, "80": 88, "81": 88, "87": 4, "95": 4, "96": 5, "97": 6, "98": 7, "99": 8, "100": 8, "101": 8, "102": 8, "103": 8, "109": 14, "115": 14, "116": 15, "117": 16, "118": 17, "119": 18, "120": 19, "121": 19, "122": 19, "123": 19, "124": 19, "125": 22, "131": 26, "136": 26, "137": 27, "138": 28, "139": 29, "140": 30, "141": 31, "142": 31, "143": 31, "144": 31, "145": 31, "146": 31, "147": 34, "148": 35, "149": 36, "150": 36, "151": 36, "152": 36, "153": 36, "154": 36, "155": 39, "161": 43, "170": 43, "171": 44, "172": 44, "173": 45, "174": 45, "175": 46, "176": 46, "177": 47, "178": 48, "179": 48, "180": 48, "181": 49, "182": 50, "183": 50, "184": 50, "185": 52, "186": 53, "187": 53, "188": 53, "189": 55, "190": 60, "191": 61, "192": 61, "193": 61, "194": 63, "195": 64, "196": 65, "197": 65, "198": 65, "204": 198}}
__M_END_METADATA
"""
