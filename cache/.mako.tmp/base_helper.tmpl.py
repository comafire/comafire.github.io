# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549730956.3613315
_enable_loop = True
_template_filename = '/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootblog4/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'html_navigation_links', 'html_navigation_links_entries', 'html_stylesheets', 'html_feedlinks', 'late_load_js', 'html_headstart']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs_link = context.get('abs_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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


def render_html_navigation_links_entries(context,navigation_links_source):
    __M_caller = context.caller_stack._push_frame()
    try:
        isinstance = context.get('isinstance', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
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


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
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
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/bootblog.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        __M_writer('    <link href="https://fonts.googleapis.com/css?family=Playfair+Display:700,900" rel="stylesheet">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
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
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/popper.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/baguetteBox.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n')
            __M_writer('        <script src="/assets/js/fancydates.min.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        prevlink = context.get('prevlink', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        url_type = context.get('url_type', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        description = context.get('description', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        meta_generator_tag = context.get('meta_generator_tag', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        __M_writer("prefix='")
        __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
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


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 2, "22": 63, "23": 88, "24": 118, "25": 122, "26": 145, "27": 170, "28": 178, "34": 172, "44": 172, "45": 173, "46": 174, "47": 175, "48": 175, "49": 175, "50": 175, "51": 175, "52": 175, "53": 175, "59": 120, "66": 120, "67": 121, "68": 121, "74": 124, "84": 124, "85": 125, "86": 126, "87": 127, "88": 127, "89": 127, "90": 129, "91": 130, "92": 131, "93": 131, "94": 131, "95": 131, "96": 131, "97": 131, "98": 131, "99": 132, "100": 133, "101": 133, "102": 133, "103": 133, "104": 133, "105": 136, "106": 137, "107": 138, "108": 139, "109": 139, "110": 139, "111": 139, "112": 139, "113": 139, "114": 139, "115": 140, "116": 141, "117": 141, "118": 141, "119": 141, "120": 141, "126": 91, "134": 91, "135": 92, "136": 93, "137": 96, "138": 97, "139": 98, "140": 99, "141": 100, "142": 101, "143": 102, "144": 105, "145": 109, "146": 110, "147": 113, "148": 114, "149": 117, "155": 149, "166": 149, "167": 150, "168": 151, "169": 151, "170": 151, "171": 152, "172": 153, "173": 154, "174": 155, "175": 155, "176": 155, "177": 155, "178": 155, "179": 157, "180": 158, "181": 158, "182": 158, "183": 161, "184": 162, "185": 163, "186": 164, "187": 164, "188": 164, "189": 164, "190": 164, "191": 166, "192": 167, "193": 167, "194": 167, "200": 65, "207": 65, "208": 66, "209": 67, "210": 73, "211": 74, "212": 75, "213": 76, "214": 77, "215": 78, "216": 79, "217": 85, "218": 87, "219": 87, "220": 87, "226": 3, "253": 3, "254": 7, "255": 8, "256": 9, "257": 10, "258": 12, "259": 13, "260": 14, "261": 17, "262": 17, "263": 17, "264": 20, "265": 21, "266": 21, "267": 21, "268": 23, "269": 24, "270": 25, "271": 25, "272": 25, "273": 26, "274": 27, "275": 27, "276": 27, "277": 27, "278": 27, "279": 29, "280": 30, "281": 30, "282": 31, "283": 31, "284": 32, "285": 33, "286": 35, "287": 35, "288": 35, "289": 36, "290": 36, "291": 38, "292": 39, "293": 40, "294": 40, "295": 40, "296": 40, "297": 40, "298": 40, "299": 40, "300": 43, "301": 44, "302": 45, "303": 45, "304": 45, "305": 47, "306": 48, "307": 49, "308": 49, "309": 49, "310": 51, "311": 52, "312": 52, "313": 52, "314": 54, "315": 55, "316": 55, "317": 56, "318": 57, "319": 58, "320": 59, "321": 59, "322": 59, "323": 61, "324": 62, "325": 62, "331": 325}, "uri": "base_helper.tmpl", "source_encoding": "utf-8", "filename": "/usr/local/lib/python3.5/dist-packages/nikola/data/themes/bootblog4/templates/base_helper.tmpl"}
__M_END_METADATA
"""
