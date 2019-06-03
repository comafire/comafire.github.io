# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1559564638.722791
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl'
_template_uri = 'feeds_translations_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['translation_link', '_head_feed_link', '_html_translation_link', 'feed_link', 'head', '_head_atom', '_html_feed_link', '_head_rss']


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


def render_translation_link(context,kind):
    __M_caller = context.caller_stack._push_frame()
    try:
        other_languages = context.get('other_languages', UNDEFINED)
        def _html_translation_link(classification,kind,language,name=None):
            return render__html_translation_link(context,classification,kind,language,name)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
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


def render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
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


def render_feed_link(context,classification,kind):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        def _html_feed_link(link_type,link_name,link_postfix,classification,kind,language,name=None):
            return render__html_feed_link(context,link_type,link_name,link_postfix,classification,kind,language,name)
        sorted = context.get('sorted', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
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


def render_head(context,classification=None,kind='index',feeds=True,other=True,rss_override=True,has_no_feeds=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        other_languages = context.get('other_languages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def _head_atom(classification=None,kind='index'):
            return render__head_atom(context,classification,kind)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        def _head_rss(classification=None,kind='index',rss_override=True):
            return render__head_rss(context,classification,kind,rss_override)
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


def render__head_atom(context,classification=None,kind='index'):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _head_feed_link(link_type,link_name,link_postfix,classification,kind,language):
            return render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language)
        len = context.get('len', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        all_languages = context.get('all_languages', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
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


def render__html_feed_link(context,link_type,link_name,link_postfix,classification,kind,language,name=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
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


def render__head_rss(context,classification=None,kind='index',rss_override=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _head_feed_link(link_type,link_name,link_postfix,classification,kind,language):
            return render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language)
        rss_link = context.get('rss_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 2, "22": 9, "23": 25, "24": 33, "25": 54, "26": 72, "27": 85, "28": 113, "29": 124, "35": 115, "44": 115, "45": 116, "46": 117, "47": 118, "48": 118, "49": 119, "50": 120, "51": 120, "52": 120, "53": 122, "59": 3, "66": 3, "67": 4, "68": 5, "69": 5, "70": 5, "71": 5, "72": 5, "73": 5, "74": 5, "75": 5, "76": 5, "77": 5, "78": 5, "79": 6, "80": 7, "81": 7, "82": 7, "83": 7, "84": 7, "85": 7, "86": 7, "87": 7, "88": 7, "94": 27, "100": 27, "101": 28, "102": 29, "103": 29, "104": 29, "105": 29, "106": 29, "107": 29, "108": 29, "109": 29, "110": 29, "111": 30, "112": 31, "113": 31, "114": 31, "115": 31, "116": 31, "117": 31, "118": 31, "124": 87, "137": 87, "138": 88, "139": 89, "140": 90, "141": 91, "142": 92, "143": 93, "144": 93, "145": 93, "146": 95, "147": 96, "148": 96, "149": 96, "150": 98, "151": 100, "152": 101, "153": 102, "154": 103, "155": 104, "156": 104, "157": 104, "158": 106, "159": 107, "160": 107, "161": 107, "162": 109, "168": 75, "179": 75, "180": 76, "181": 77, "182": 77, "183": 77, "184": 78, "185": 78, "186": 80, "187": 81, "188": 82, "189": 82, "190": 82, "191": 82, "192": 82, "198": 56, "211": 56, "212": 57, "213": 58, "214": 59, "215": 60, "216": 60, "217": 60, "218": 60, "219": 60, "220": 60, "221": 60, "222": 60, "223": 60, "224": 60, "225": 60, "226": 62, "227": 63, "228": 64, "229": 65, "230": 65, "231": 65, "232": 66, "233": 67, "234": 67, "235": 67, "241": 11, "249": 11, "250": 12, "251": 13, "252": 14, "253": 14, "254": 14, "255": 14, "256": 14, "257": 14, "258": 14, "259": 14, "260": 14, "261": 14, "262": 14, "263": 14, "264": 14, "265": 15, "266": 16, "267": 16, "268": 16, "269": 16, "270": 16, "271": 16, "272": 16, "273": 16, "274": 16, "275": 16, "276": 16, "277": 18, "278": 19, "279": 20, "280": 20, "281": 20, "282": 20, "283": 20, "284": 20, "285": 20, "286": 20, "287": 20, "288": 20, "289": 20, "290": 21, "291": 22, "292": 22, "293": 22, "294": 22, "295": 22, "296": 22, "297": 22, "298": 22, "299": 22, "305": 35, "319": 35, "320": 36, "321": 37, "322": 37, "323": 37, "324": 39, "325": 40, "326": 41, "327": 42, "328": 42, "329": 42, "330": 42, "331": 42, "332": 42, "333": 42, "334": 42, "335": 42, "336": 42, "337": 42, "338": 44, "339": 45, "340": 46, "341": 47, "342": 47, "343": 47, "344": 48, "345": 49, "346": 49, "347": 49, "353": 347}, "uri": "feeds_translations_helper.tmpl", "source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl"}
__M_END_METADATA
"""
