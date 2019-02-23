# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550946706.8700922
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl'
_template_uri = 'feeds_translations_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['feed_link', 'head', '_html_translation_link', '_head_atom', '_head_feed_link', '_html_feed_link', 'translation_link', '_head_rss']


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


def render_feed_link(context,classification,kind):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        all_languages = context.get('all_languages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def _html_feed_link(link_type,link_name,link_postfix,classification,kind,language,name=None):
            return render__html_feed_link(context,link_type,link_name,link_postfix,classification,kind,language,name)
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


def render_head(context,classification=None,kind='index',feeds=True,other=True,rss_override=True,has_no_feeds=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        other_languages = context.get('other_languages', UNDEFINED)
        def _head_rss(classification=None,kind='index',rss_override=True):
            return render__head_rss(context,classification,kind,rss_override)
        def _head_atom(classification=None,kind='index'):
            return render__head_atom(context,classification,kind)
        _link = context.get('_link', UNDEFINED)
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


def render__head_atom(context,classification=None,kind='index'):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        def _head_feed_link(link_type,link_name,link_postfix,classification,kind,language):
            return render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language)
        all_languages = context.get('all_languages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
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


def render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
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


def render__html_feed_link(context,link_type,link_name,link_postfix,classification,kind,language,name=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
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


def render_translation_link(context,kind):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        other_languages = context.get('other_languages', UNDEFINED)
        def _html_translation_link(classification,kind,language,name=None):
            return render__html_translation_link(context,classification,kind,language,name)
        messages = context.get('messages', UNDEFINED)
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


def render__head_rss(context,classification=None,kind='index',rss_override=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        def _head_feed_link(link_type,link_name,link_postfix,classification,kind,language):
            return render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language)
        all_languages = context.get('all_languages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"uri": "feeds_translations_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 9, "23": 25, "24": 33, "25": 54, "26": 72, "27": 85, "28": 113, "29": 124, "35": 87, "48": 87, "49": 88, "50": 89, "51": 90, "52": 91, "53": 92, "54": 93, "55": 93, "56": 93, "57": 95, "58": 96, "59": 96, "60": 96, "61": 98, "62": 100, "63": 101, "64": 102, "65": 103, "66": 104, "67": 104, "68": 104, "69": 106, "70": 107, "71": 107, "72": 107, "73": 109, "79": 75, "90": 75, "91": 76, "92": 77, "93": 77, "94": 77, "95": 78, "96": 78, "97": 80, "98": 81, "99": 82, "100": 82, "101": 82, "102": 82, "103": 82, "109": 27, "115": 27, "116": 28, "117": 29, "118": 29, "119": 29, "120": 29, "121": 29, "122": 29, "123": 29, "124": 29, "125": 29, "126": 30, "127": 31, "128": 31, "129": 31, "130": 31, "131": 31, "132": 31, "133": 31, "139": 56, "152": 56, "153": 57, "154": 58, "155": 59, "156": 60, "157": 60, "158": 60, "159": 60, "160": 60, "161": 60, "162": 60, "163": 60, "164": 60, "165": 60, "166": 60, "167": 62, "168": 63, "169": 64, "170": 65, "171": 65, "172": 65, "173": 66, "174": 67, "175": 67, "176": 67, "182": 3, "189": 3, "190": 4, "191": 5, "192": 5, "193": 5, "194": 5, "195": 5, "196": 5, "197": 5, "198": 5, "199": 5, "200": 5, "201": 5, "202": 6, "203": 7, "204": 7, "205": 7, "206": 7, "207": 7, "208": 7, "209": 7, "210": 7, "211": 7, "217": 11, "225": 11, "226": 12, "227": 13, "228": 14, "229": 14, "230": 14, "231": 14, "232": 14, "233": 14, "234": 14, "235": 14, "236": 14, "237": 14, "238": 14, "239": 14, "240": 14, "241": 15, "242": 16, "243": 16, "244": 16, "245": 16, "246": 16, "247": 16, "248": 16, "249": 16, "250": 16, "251": 16, "252": 16, "253": 18, "254": 19, "255": 20, "256": 20, "257": 20, "258": 20, "259": 20, "260": 20, "261": 20, "262": 20, "263": 20, "264": 20, "265": 20, "266": 21, "267": 22, "268": 22, "269": 22, "270": 22, "271": 22, "272": 22, "273": 22, "274": 22, "275": 22, "281": 115, "290": 115, "291": 116, "292": 117, "293": 118, "294": 118, "295": 119, "296": 120, "297": 120, "298": 120, "299": 122, "305": 35, "319": 35, "320": 36, "321": 37, "322": 37, "323": 37, "324": 39, "325": 40, "326": 41, "327": 42, "328": 42, "329": 42, "330": 42, "331": 42, "332": 42, "333": 42, "334": 42, "335": 42, "336": 42, "337": 42, "338": 44, "339": 45, "340": 46, "341": 47, "342": 47, "343": 47, "344": 48, "345": 49, "346": 49, "347": 49, "353": 347}, "source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl"}
__M_END_METADATA
"""
