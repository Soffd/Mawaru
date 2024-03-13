## 此文件包含有可自定义您游戏的设置。
##
## 以“##”开头的语句是注释，您不应该对其取消注释。以“#”开头的语句是注释掉的代码，
## 在适用的时候您可能需要对其取消注释。


## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。

define config.name = _("Mawaru")


## 决定上面给出的标题是否显示在标题界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = False


## 游戏版本号。

define config.version = "0.0.1"


## 放置在游戏内“关于”屏幕上的文本。将文本放在三个引号之间，并在段落之间留出空
## 行。

define gui.about = _p("""本游戏由Yiki Soffd制作，使用了较多AI成分，注意辨别。\n\n背景来源：{a=https://min-chi.material.jp/}【フリー素材】 みんちりえ 【背景イラスト配布サイト】{/a}。\n\n立绘来源：{a=https://play.google.com/store/apps/details?id=io.mewtant.pixaiart}PixAI{/a}。\n\n主题曲：{a=https://c6.y.qq.com/base/fcgi-bin/u?__=e6oM1nWzLLIO}循環，歌手名：HoneyComeBear，专辑名：循環{/a}。\n\n配音来源：{a=https://www.modelscope.cn/studios/xzjosh/GPT-SoVITS/summary}GPT-SoVITS在线一键语音生成合集（Xz乔希）{/a}。\n\n其他BGM和音效来源：{a=https://bcut.bilibili.cn/}必剪素材{/a}。\n\n由于一些问题，我建议调低音乐音量，调高设备音量，避免听不清配音。\n\n此外，对于Android用户，{color=#ff0000}如果你无法在游戏里正常输入中文文本{/color}，比如打字时调用了安全键盘，那我建议你在手机设置 → 其他设置 → 键盘与输入法中关闭输入密码时启用安全键盘。\n\n联系作者（你有任何的意见和建议都可以联系。）：{a=https://qm.qq.com/q/yVIHxLMTHE}QQ联系{/a}。\n\n邮箱：20051026liubin@gmail.com。\n\n本应用使用了SIL协议以及GPL协议的字体，以下为SIL协议授权许可，PC端可在程序附带的文件中查看。\n\nThis Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is copied below, and is also available with a FAQ at:\n\n
{a=https://openfontlicense.org/}http://scripts.sil.org/OFL{/a}


-----------------------------------------------------------

SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007

-----------------------------------------------------------

PREAMBLE

The goals of the Open Font License (OFL) are to stimulate worldwide
development of collaborative font projects, to support the font creation
efforts of academic and linguistic communities, and to provide a free and
open framework in which fonts may be shared and improved in partnership
with others.

The OFL allows the licensed fonts to be used, studied, modified and
redistributed freely as long as they are not sold by themselves. The
fonts, including any derivative works, can be bundled, embedded, 
redistributed and/or sold with any software provided that any reserved
names are not used by derivative works. The fonts and derivatives,
however, cannot be released under any other type of license. The
requirement for fonts to remain under this license does not apply
to any document created using the fonts or their derivatives.

DEFINITIONS

"Font Software" refers to the set of files released by the Copyright
Holder(s) under this license and clearly marked as such. This may
include source files, build scripts and documentation.

"Reserved Font Name" refers to any names specified as such after the
copyright statement(s).

"Original Version" refers to the collection of Font Software components as
distributed by the Copyright Holder(s).

"Modified Version" refers to any derivative made by adding to, deleting,
or substituting -- in part or in whole -- any of the components of the
Original Version, by changing formats or by porting the Font Software to a
new environment.

"Author" refers to any designer, engineer, programmer, technical
writer or other person who contributed to the Font Software.

PERMISSION & CONDITIONS

Permission is hereby granted, free of charge, to any person obtaining
a copy of the Font Software, to use, study, copy, merge, embed, modify,
redistribute, and sell modified and unmodified copies of the Font
Software, subject to the following conditions:

1) Neither the Font Software nor any of its individual components,
in Original or Modified Versions, may be sold by itself.

2) Original or Modified Versions of the Font Software may be bundled,
redistributed and/or sold with any software, provided that each copy
contains the above copyright notice and this license. These can be
included either as stand-alone text files, human-readable headers or
in the appropriate machine-readable metadata fields within text or
binary files as long as those fields can be easily viewed by the user.

3) No Modified Version of the Font Software may use the Reserved Font
Name(s) unless explicit written permission is granted by the corresponding
Copyright Holder. This restriction only applies to the primary font name as
presented to the users.

4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font
Software shall not be used to promote, endorse or advertise any
Modified Version, except to acknowledge the contribution(s) of the
Copyright Holder(s) and the Author(s) or with their explicit written
permission.

5) The Font Software, modified or unmodified, in part or in whole,
must be distributed entirely under this license, and must not be
distributed under any other license. The requirement for fonts to
remain under this license does not apply to any document created
using the Font Software.

TERMINATION

This license becomes null and void if any of the above conditions are
not met.

DISCLAIMER

THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT
OF COPYRIGHT, PATENT, TRADEMARK, OR OTHER RIGHT. IN NO EVENT SHALL THE
COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
INCLUDING ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL
DAMAGES, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM
OTHER DEALINGS IN THE FONT SOFTWARE.\n\n


以下为中文翻译：\n\n本“字型软件”以《SIL开源字型授权》1.1版授权释出。
本授权条款全文副本如下，亦随《常见问题目录》（FAQ）于以下网址提供：
{a=https://openfontlicense.org/}https://scripts.sil.org/OFL{/a}

==============================

SIL开源字型授权　1.1 版 – 2007 年 2 月 26 日

==============================


{size=+20}{color=#0000ffff}序言{/size}{/color}

《开源字型授权》（Open Font License，简称《OFL》）旨在促进全球字型协作项目的共同开发，支持学术及语言学团体对于字型创作的努力，以及提供一个自由开源的基本框架，让字型能在彼此合作的关系中分享与改进。
OFL允许以本授权释出的字型自由地使用、研究、修改和再分发(redistributed)，而该释出字型不得被单独销售。该字型，以及任何其衍生作品 (derivative works)，可以与任何软件捆绑 (bundled)、嵌入 (embedded)、再分发以及／或一并销售，前提是衍生作品不得使用任何保留字型名称 (reserved names)。然而，该释出字型与其衍生作品不得在任何其他授权条款下发布。本授权针对释出字型“必须以同样授权释出”的要求规定，并不适用于任何使用该释出字型或其衍生作品创建的任何文档。


{size=+20}{color=#0000ffff}定义{/size}{/color}

“字型软件” (font software) 指由版权持有者（或著作权人，copyright holder(s)）通过本授权下发布释出并明确标示本授权的一系列文件。“字型软件”可以包括源文件(source files)、构建脚本 (build script) 以及说明文档。

“保留字型名称” (Reserved Font Name) 指在版权声明后、被特别标示指定为“保留字型名称”的任何名称。

“原始版本（或简称原版）” (original version) 指版权持有者所分发的“字型软件”构件的集合。

“修改版本” (modified version) 指通过增加、删除或替换 (substituting) “原始版本”中的任何部分或整体构件、转换字型软件的格式或移植字型软件到新的运作环境中而产生的衍生版本。

“作者” (author) 指任何为“字型软件”做出贡献的设计师、工程师、程序员、技术文档工程师 (technical writer) 或其他人员。


{size=+20}{color=#0000ffff}许可与条件{/size}{/color}

特此允许任何取得本“字型软件”副本的个人，授予免费使用、研究、复制、合并、嵌入、修改、再分发以及销售已修改和未修改的字型副本，但需要遵守下列所规定的条件：

1) 无论是“原始版本”或“修改版本”，“字型软件”或其中任何独立的个别构件，均不能被单独销售。

2) “字型软件”的“原始版本”或“修改版本”可以与任何软件捆绑 (bundled)、再分发以及／或一并销售，前提为每份软件副本都必须包含本授权条款上述的版权声明 (copyright notice) 以及本授权条款全文。这些版权声明与条款全文可以被放置在独立纯文本文件、人类可读信息头、或文本／二进制文件内适当的、用户易于查阅浏览的机器可读元数据字段。

3) “修改版本”的“字型软件”不得使用“保留字型名称”，除非相应名称的版权持有者授予明确的书面同意许可。此项限制仅适用于对用户显示的主要字型名称 (primary font name)。

4) 版权持有者或“字型软件”的作者姓名不应被使用来推广、认可或宣传任何“修改版本”的字型。不过，在取得版权持有者的书面同意许可前提下，可以进行以上行为；向版权持有者和作者的贡献致谢而标示姓名也不在此列。

5) “字型软件”，无论已修改或未修改、部分或整体，均必须完全通过本授权下分发，不得在任何其他授权条款下分发。本授权针对释出字型“必须以同样授权释出”的要求规定，并不适用于任何使用该“字型软件”创建的任何文档。


{size=+20}{color=#0000ffff}终止授权{/size}{/color}

假如上述任一条款无法被遵守，本授权条款将会失效 (null and void)。


{size=+20}{color=#0000ffff}免责声明{/size}{/color}

“字型软件”是以“按原样” (AS IS) 提供，并不作任何明示或暗示的保证，包括但不限于对“字型软件”的适销性 (MERCHANTABILITY)、特定用途适用性和不侵犯版权、专利权、商标权或任何其他权利的保证。此外，在任何情况下，无论是在合同诉讼、侵权诉讼或其他诉讼中，版权持有者均不承担因使用或无法使用“字型软件”，或出于任何使用“字型软件”的任何行为而产生、引起的任何索赔、损害或可归责事由而来的任何责任，包括任何一般、特殊、间接、附带或结果性损害。\n\n


{size=+25}{color=#ff0000}本程序遵循GPL协议，完全开源，源代码会逐步公开。{/size}{/color}
""")


## 在构建的发布版中，可执行文件和目录所使用的短名称。此处仅限使用 ASCII 字符，并
## 且不能包含空格、冒号或分号。

define build.name = "Mawaru"


## 音效和音乐 #######################################################################

## 这三个变量控制哪些内置的混音器会默认显示给用户。将其中一个设置为 False 将隐藏
## 对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 为了让用户在音效或语音轨道上播放测试音频，请取消对下面一行的注释并设置播放的
## 样本声音。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 将以下语句取消注释就可以设置标题界面播放的背景音乐文件。此文件将在整个游戏中
## 持续播放，直至音乐停止或其他文件开始播放。

define config.main_menu_music = "循環-HoneyComeBear.mp3"


## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve


## 载入游戏后使用的转场。

define config.after_load_transition = None


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = None


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 语句。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。若为 show，对话框将总是显示。若为 hide，对话框
## 仅在对话出现时显示。若为 auto，对话框会在 scene 语句前隐藏，并在有新对话时重
## 新显示。
##
## 在游戏开始后，可以用 window show、window hide 和 window auto 语句来改变其状
## 态。

define config.window = "hide"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 为瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 0


## 默认的自动前进延迟。数字越大，等待时间越长，有效范围为 0 - 30。

default preferences.afm_time = 15


## 存档目录 ########################################################################
##
## 控制 Ren'Py 放置游戏存档的特定操作系统目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该语句通常不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "Mawaru-1708674387"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon.png"


## 构建配置 ########################################################################
##
## 此部分控制 Ren'Py 如何将您的项目转变为发行版文件。

init python:

    ## 以下函数接受文件模式。文件模式不区分大小写，并与基础目录的相对路径相匹
    ## 配，包括或不包括 /。如果多个模式匹配，则使用第一个模式。
    ##
    ## 在一个模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中的 txt 文件，“game/**.ogg”匹配游戏目录或任何子
    ## 目录中的 ogg 文件，“**.psd”匹配项目中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从构建的发行版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 若要封装文件，需将其列为“archive”。

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## 匹配为文档模式的文件会在 Mac 应用程序构建中被复制，因此它们同时出现在 APP
    ## 和 ZIP 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')


## 执行应用内购需要一个 Google Play 许可密钥。许可密钥可以在 Google Play 开发者
## 控制台的“Monetize” > “Monetization Setup” > “Licensing”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 项目相关的用户名和项目名，以 / 分隔。

# define build.itch_project = "renpytom/test-project"
