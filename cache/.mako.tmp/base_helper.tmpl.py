# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550250493.2220654
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_navigation_links_entries', 'late_load_js', 'html_headstart', 'html_stylesheets', 'html_translations', 'html_feedlinks', 'html_navigation_links']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links_entries(context,navigation_links_source):
    __M_caller = context.caller_stack._push_frame()
    try:
        rel_link = context.get('rel_link', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text in navigation_links_source[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li class="nav-item dropdown"><a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">')
                __M_writer(str(text))
                __M_writer('</a>\n            <div class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <a href="')
                        __M_writer(str(permalink))
                        __M_writer('" class="dropdown-item active">')
                        __M_writer(str(text))
                        __M_writer(' <span class="sr-only">')
                        __M_writer(str(messages("(active)", lang)))
                        __M_writer('</span></a>\n')
                    else:
                        __M_writer('                    <a href="')
                        __M_writer(str(suburl))
                        __M_writer('" class="dropdown-item">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                __M_writer('            </div>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="nav-item active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('" class="nav-link">')
                    __M_writer(str(text))
                    __M_writer(' <span class="sr-only">')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a>\n')
                else:
                    __M_writer('                <li class="nav-item"><a href="')
                    __M_writer(str(url))
                    __M_writer('" class="nav-link">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js" integrity="sha256-EGs9T1xMHdvM1geM8jPpoo8EZ1V1VRsmcJz8OByENLA=" crossorigin="anonymous"></script>\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.11.0/baguetteBox.min.js" integrity="sha256-yQGjQhFs3LtyiN5hhr3k9s9TWZOh/RzCkD3gwwCKlkg=" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.2/moment-with-locales.min.js" integrity="sha256-VrmtNHAdGzjNsUNtWYG55xxE9xDTz4gF63x/prKXKH0=" crossorigin="anonymous"></script>\n')
        if use_bundles and use_cdn:
            __M_writer('        <script src="/assets/js/all.js"></script>\n')
        elif use_bundles:
            __M_writer('        <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if not use_cdn:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/popper.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/baguetteBox.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n            <script src="/assets/js/fancydates.min.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_feedlinks():
            return render_html_feedlinks(context)
        favicons = context.get('favicons', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        description = context.get('description', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        prevlink = context.get('prevlink', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        title = context.get('title', UNDEFINED)
        meta_generator_tag = context.get('meta_generator_tag', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        __M_writer("prefix='")
        __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article#\n')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb# ')
        __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width, initial-scale=1">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n')
        if meta_generator_tag:
            __M_writer('    <meta name="generator" content="Nikola (getnikola.com)">\n')
        __M_writer('    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">\n        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.11.0/baguetteBox.min.css" integrity="sha256-cKiyvRKpm8RaTdU71Oq2RUVgvfWrdIXjvVdQF2oZ1Y4=" crossorigin="anonymous" />\n')
        if use_bundles and use_cdn:
            __M_writer('        <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
        elif use_bundles:
            __M_writer('        <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if not use_cdn:
                __M_writer('            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n            <link href="/assets/css/baguetteBox.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li class="nav-item"><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('" class="nav-link">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rss_link = context.get('rss_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_navigation_links_entries(navigation_links_source):
            return render_html_navigation_links_entries(context,navigation_links_source)
        navigation_links = context.get('navigation_links', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(html_navigation_links_entries(navigation_links)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootstrap4/templates/base_helper.tmpl", "line_map": {"16": 0, "21": 62, "22": 87, "23": 115, "24": 119, "25": 142, "26": 165, "27": 173, "33": 121, "43": 121, "44": 122, "45": 123, "46": 124, "47": 124, "48": 124, "49": 126, "50": 127, "51": 128, "52": 128, "53": 128, "54": 128, "55": 128, "56": 128, "57": 128, "58": 129, "59": 130, "60": 130, "61": 130, "62": 130, "63": 130, "64": 133, "65": 134, "66": 135, "67": 136, "68": 136, "69": 136, "70": 136, "71": 136, "72": 136, "73": 136, "74": 137, "75": 138, "76": 138, "77": 138, "78": 138, "79": 138, "85": 64, "92": 64, "93": 65, "94": 66, "95": 72, "96": 73, "97": 74, "98": 75, "99": 76, "100": 77, "101": 78, "102": 86, "103": 86, "104": 86, "110": 2, "137": 2, "138": 6, "139": 7, "140": 8, "141": 9, "142": 11, "143": 12, "144": 13, "145": 16, "146": 16, "147": 16, "148": 19, "149": 20, "150": 20, "151": 20, "152": 22, "153": 23, "154": 24, "155": 24, "156": 24, "157": 25, "158": 26, "159": 26, "160": 26, "161": 26, "162": 26, "163": 28, "164": 29, "165": 29, "166": 30, "167": 30, "168": 31, "169": 32, "170": 34, "171": 34, "172": 34, "173": 35, "174": 35, "175": 37, "176": 38, "177": 39, "178": 39, "179": 39, "180": 39, "181": 39, "182": 39, "183": 39, "184": 42, "185": 43, "186": 44, "187": 44, "188": 44, "189": 46, "190": 47, "191": 48, "192": 48, "193": 48, "194": 50, "195": 51, "196": 51, "197": 51, "198": 53, "199": 54, "200": 54, "201": 55, "202": 56, "203": 57, "204": 58, "205": 58, "206": 58, "207": 60, "208": 61, "209": 61, "215": 90, "223": 90, "224": 91, "225": 92, "226": 95, "227": 96, "228": 97, "229": 98, "230": 99, "231": 100, "232": 101, "233": 104, "234": 107, "235": 108, "236": 111, "237": 112, "243": 167, "253": 167, "254": 168, "255": 169, "256": 170, "257": 170, "258": 170, "259": 170, "260": 170, "261": 170, "262": 170, "268": 144, "279": 144, "280": 145, "281": 146, "282": 146, "283": 146, "284": 147, "285": 148, "286": 149, "287": 150, "288": 150, "289": 150, "290": 150, "291": 150, "292": 152, "293": 153, "294": 153, "295": 153, "296": 156, "297": 157, "298": 158, "299": 159, "300": 159, "301": 159, "302": 159, "303": 159, "304": 161, "305": 162, "306": 162, "307": 162, "313": 117, "320": 117, "321": 118, "322": 118, "328": 322}, "uri": "base_helper.tmpl"}
__M_END_METADATA
"""
