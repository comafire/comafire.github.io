# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552059593.0720742
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/post_helper.tmpl'
_template_uri = 'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['twitter_card_information', 'html_pager', 'meta_translations', 'open_graph_metadata', 'mathjax_script', 'html_tags']


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


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        blog_title = context.get('blog_title', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
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


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/post_helper.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "31": 2, "32": 12, "33": 24, "34": 41, "35": 68, "36": 84, "37": 89, "43": 70, "48": 70, "49": 71, "50": 72, "51": 72, "52": 72, "53": 73, "54": 74, "55": 74, "56": 74, "57": 75, "58": 76, "59": 76, "60": 76, "61": 78, "62": 79, "63": 79, "64": 79, "65": 80, "66": 81, "67": 81, "68": 81, "74": 26, "79": 26, "80": 27, "81": 28, "82": 29, "83": 30, "84": 31, "85": 31, "86": 31, "87": 31, "88": 31, "89": 31, "90": 34, "91": 35, "92": 36, "93": 36, "94": 36, "95": 36, "96": 36, "97": 36, "98": 39, "104": 4, "112": 4, "113": 5, "114": 6, "115": 7, "116": 8, "117": 8, "118": 8, "119": 8, "120": 8, "126": 43, "135": 43, "136": 44, "137": 44, "138": 45, "139": 45, "140": 46, "141": 46, "142": 47, "143": 48, "144": 48, "145": 48, "146": 49, "147": 50, "148": 50, "149": 50, "150": 52, "151": 53, "152": 53, "153": 53, "154": 55, "155": 60, "156": 61, "157": 61, "158": 61, "159": 63, "160": 64, "161": 65, "162": 65, "163": 65, "169": 87, "174": 87, "175": 88, "176": 88, "182": 14, "188": 14, "189": 15, "190": 16, "191": 17, "192": 18, "193": 19, "194": 19, "195": 19, "196": 19, "197": 19, "198": 22, "204": 198}, "uri": "post_helper.tmpl"}
__M_END_METADATA
"""
