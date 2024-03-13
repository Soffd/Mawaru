define yyl = Character("亚依璃", who_color="#ff0000")
# あいり
define ndy = Character("奈都羽", who_color="#2600ff")
# なつは
define ybj = Character("有波皆", who_color="#04ff00")
# ありなみみな
define fy = Character("芙优", who_color="#ff00ee")
# ふゆう  AI星瞳
define zl = Character("朝里", who_color="#00e5ff")
# あさり
define cmj = Character("彩弥加", who_color="#fffb00")
# あやか
define wj = Character("[povname]", who_color="#00fbff")
# ものえ
label splashscreen:
    scene black
    with Pause(1)

    show text "{size=+10}由Yuki Soffd制作。{/size}" with fade
    with Pause(3)

    show text "{size=+10}使用耳机游玩，体验更佳。{/size}" with fade
    with Pause(3)

    show text "{size=+10}希望你可以先阅读“关于”。{/size}" with fade
    with Pause(3)
    return
label start:
    menu:
        "前方还在施工，是否开始？"
        "开始游戏":
            jump name
        "算了，退出":
            return
label name:
    python:
        povname = renpy.input("请输入你的名字，若为空白，则为默认名字“物江”。{color=#ff0000}注意！本游戏中，你的视角角色性别为女性，注意区分！{/color}")
        povname = povname.strip()
        if not povname:
            povname = "物江"
    wj "你的名字是[povname]。"
    jump chapter1