# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552103979.628618
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl'
_template_uri = 'feeds_translations_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['_head_rss', '_html_feed_link', '_head_feed_link', 'feed_link', '_head_atom', 'head', 'translation_link', '_html_translation_link']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
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


def render__head_rss(context,classification=None,kind='index',rss_override=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _head_feed_link(link_type,link_name,link_postfix,classification,kind,language):
            return render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        all_languages = context.get('all_languages', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link and rss_override:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        if generate_rss and not (rss_link and rss_override) and kind != 'archive':
            if len(translations) > 1 and has_other_languages and classification and kind != 'index':
                for language, classification, name in all_languages:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS for ')
                    __M_writer(str(kind))
                    __M_writer(' ')
                    __M_writer(filters.html_escape(str(name)))
                    __M_writer(' (')
                    __M_writer(str(language))
                    __M_writer(')" hreflang="')
                    __M_writer(str(language))
                    __M_writer('" href="')
                    __M_writer(str(_link(kind + "_rss", classification, language)))
                    __M_writer('">\n')
            else:
                for language in sorted(translations):
                    if (classification or classification == '') and kind != 'index':
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/rss+xml', 'RSS for ' + kind + ' ' + classification, 'rss', classification, kind, language)))
                        __M_writer('\n')
                    else:
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/rss+xml', 'RSS', 'rss', classification, 'index', language)))
                        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__html_feed_link(context,link_type,link_name,link_postfix,classification,kind,language,name=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            if name and kind != "archive" and kind != "author":
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer(' (')
                __M_writer(filters.html_escape(str(name)))
                __M_writer(', ')
                __M_writer(str(language))
                __M_writer(')</a>\n')
            else:
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')</a>\n')
        else:
            if name and kind != "archive" and kind != "author":
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer(' (')
                __M_writer(filters.html_escape(str(name)))
                __M_writer(')</a>\n')
            else:
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <link rel="alternate" type="')
            __M_writer(str(link_type))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(link_name)))
            __M_writer(' (')
            __M_writer(str(language))
            __M_writer(')" hreflang="')
            __M_writer(str(language))
            __M_writer('" href="')
            __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
            __M_writer('">\n')
        else:
            __M_writer('        <link rel="alternate" type="')
            __M_writer(str(link_type))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(link_name)))
            __M_writer('" hreflang="')
            __M_writer(str(language))
            __M_writer('" href="')
            __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_feed_link(context,classification,kind):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _html_feed_link(link_type,link_name,link_postfix,classification,kind,language,name=None):
            return render__html_feed_link(context,link_type,link_name,link_postfix,classification,kind,language,name)
        translations = context.get('translations', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        all_languages = context.get('all_languages', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if generate_atom or generate_rss:
            if len(translations) > 1 and has_other_languages and kind != 'index':
                for language, classification, name in all_languages:
                    __M_writer('                <p class="feedlink">\n')
                    if generate_atom:
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/atom+xml', 'Atom feed', 'atom', classification, kind, language, name)))
                        __M_writer('\n')
                    if generate_rss and kind != 'archive':
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/rss+xml', 'RSS feed', 'rss', classification, kind, language, name)))
                        __M_writer('\n')
                    __M_writer('                </p>\n')
            else:
                for language in sorted(translations):
                    __M_writer('                <p class="feedlink">\n')
                    if generate_atom:
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/atom+xml', 'Atom feed', 'atom', classification, kind, language)))
                        __M_writer('\n')
                    if generate_rss and kind != 'archive':
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/rss+xml', 'RSS feed', 'rss', classification, kind, language)))
                        __M_writer('\n')
                    __M_writer('                </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__head_atom(context,classification=None,kind='index'):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _head_feed_link(link_type,link_name,link_postfix,classification,kind,language):
            return render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        len = context.get('len', UNDEFINED)
        all_languages = context.get('all_languages', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if generate_atom:
            if len(translations) > 1 and has_other_languages and classification and kind != 'index':
                for language, classification, name in all_languages:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom for ')
                    __M_writer(str(kind))
                    __M_writer(' ')
                    __M_writer(filters.html_escape(str(name)))
                    __M_writer(' (')
                    __M_writer(str(language))
                    __M_writer(')" hreflang="')
                    __M_writer(str(language))
                    __M_writer('" href="')
                    __M_writer(str(_link(kind + "_atom", classification, language)))
                    __M_writer('">\n')
            else:
                for language in sorted(translations):
                    if (classification or classification == '') and kind != 'index':
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/atom+xml', 'Atom for ' + kind + ' ' + classification, 'atom', classification, kind, language)))
                        __M_writer('\n')
                    else:
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/atom+xml', 'Atom', 'atom', classification, 'index', language)))
                        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,classification=None,kind='index',feeds=True,other=True,rss_override=True,has_no_feeds=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _head_rss(classification=None,kind='index',rss_override=True):
            return render__head_rss(context,classification,kind,rss_override)
        _link = context.get('_link', UNDEFINED)
        def _head_atom(classification=None,kind='index'):
            return render__head_atom(context,classification,kind)
        other_languages = context.get('other_languages', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if feeds and not has_no_feeds:
            __M_writer('        ')
            __M_writer(str(_head_rss(classification, 'index' if (kind == 'archive' and rss_override) else kind, rss_override)))
            __M_writer('\n        ')
            __M_writer(str(_head_atom(classification, kind)))
            __M_writer('\n')
        if other and has_other_languages and other_languages:
            for language, classification, _ in other_languages:
                __M_writer('            <link rel="alternate" hreflang="')
                __M_writer(str(language))
                __M_writer('" href="')
                __M_writer(str(_link(kind, classification, language)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_translation_link(context,kind):
    __M_caller = context.caller_stack._push_frame()
    try:
        other_languages = context.get('other_languages', UNDEFINED)
        def _html_translation_link(classification,kind,language,name=None):
            return render__html_translation_link(context,classification,kind,language,name)
        messages = context.get('messages', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if has_other_languages and other_languages:
            __M_writer('        <div class="translationslist translations">\n            <h3 class="translationslist-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for language, classification, name in other_languages:
                __M_writer('            <p>')
                __M_writer(str(_html_translation_link(classification, kind, language, name)))
                __M_writer('</p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__html_translation_link(context,classification,kind,language,name=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if name and kind != "archive" and kind != "author":
            __M_writer('        <a href="')
            __M_writer(str(_link(kind, classification, language)))
            __M_writer('" hreflang="')
            __M_writer(str(language))
            __M_writer('" rel="alternate">')
            __M_writer(str(messages("LANGUAGE", language)))
            __M_writer(' (')
            __M_writer(filters.html_escape(str(name)))
            __M_writer(')</a>\n')
        else:
            __M_writer('        <a href="')
            __M_writer(str(_link(kind, classification, language)))
            __M_writer('" hreflang="')
            __M_writer(str(language))
            __M_writer('" rel="alternate">')
            __M_writer(str(messages("LANGUAGE", language)))
            __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "feeds_translations_helper.tmpl", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 9, "23": 25, "24": 33, "25": 54, "26": 72, "27": 85, "28": 113, "29": 124, "35": 35, "49": 35, "50": 36, "51": 37, "52": 37, "53": 37, "54": 39, "55": 40, "56": 41, "57": 42, "58": 42, "59": 42, "60": 42, "61": 42, "62": 42, "63": 42, "64": 42, "65": 42, "66": 42, "67": 42, "68": 44, "69": 45, "70": 46, "71": 47, "72": 47, "73": 47, "74": 48, "75": 49, "76": 49, "77": 49, "83": 11, "91": 11, "92": 12, "93": 13, "94": 14, "95": 14, "96": 14, "97": 14, "98": 14, "99": 14, "100": 14, "101": 14, "102": 14, "103": 14, "104": 14, "105": 14, "106": 14, "107": 15, "108": 16, "109": 16, "110": 16, "111": 16, "112": 16, "113": 16, "114": 16, "115": 16, "116": 16, "117": 16, "118": 16, "119": 18, "120": 19, "121": 20, "122": 20, "123": 20, "124": 20, "125": 20, "126": 20, "127": 20, "128": 20, "129": 20, "130": 20, "131": 20, "132": 21, "133": 22, "134": 22, "135": 22, "136": 22, "137": 22, "138": 22, "139": 22, "140": 22, "141": 22, "147": 3, "154": 3, "155": 4, "156": 5, "157": 5, "158": 5, "159": 5, "160": 5, "161": 5, "162": 5, "163": 5, "164": 5, "165": 5, "166": 5, "167": 6, "168": 7, "169": 7, "170": 7, "171": 7, "172": 7, "173": 7, "174": 7, "175": 7, "176": 7, "182": 87, "195": 87, "196": 88, "197": 89, "198": 90, "199": 91, "200": 92, "201": 93, "202": 93, "203": 93, "204": 95, "205": 96, "206": 96, "207": 96, "208": 98, "209": 100, "210": 101, "211": 102, "212": 103, "213": 104, "214": 104, "215": 104, "216": 106, "217": 107, "218": 107, "219": 107, "220": 109, "226": 56, "239": 56, "240": 57, "241": 58, "242": 59, "243": 60, "244": 60, "245": 60, "246": 60, "247": 60, "248": 60, "249": 60, "250": 60, "251": 60, "252": 60, "253": 60, "254": 62, "255": 63, "256": 64, "257": 65, "258": 65, "259": 65, "260": 66, "261": 67, "262": 67, "263": 67, "269": 75, "280": 75, "281": 76, "282": 77, "283": 77, "284": 77, "285": 78, "286": 78, "287": 80, "288": 81, "289": 82, "290": 82, "291": 82, "292": 82, "293": 82, "299": 115, "308": 115, "309": 116, "310": 117, "311": 118, "312": 118, "313": 119, "314": 120, "315": 120, "316": 120, "317": 122, "323": 27, "329": 27, "330": 28, "331": 29, "332": 29, "333": 29, "334": 29, "335": 29, "336": 29, "337": 29, "338": 29, "339": 29, "340": 30, "341": 31, "342": 31, "343": 31, "344": 31, "345": 31, "346": 31, "347": 31, "353": 347}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
