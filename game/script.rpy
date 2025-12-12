# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

# 定义角色
define mc = Character("陈砚青", color="#c8ffff")
define lmt = Character("李墨亭", color="#8B4513") # 掌柜
define sm = Character("史密斯", color="#808080") # 洋商
define cm = Character("陈墨",color="#8B4513")#师弟
define wnn = Character("王奶奶", color="#D2691E") # 老主顾

define audio1 = "audio/竹子物语（第一幕以及游戏初始界面）.mp3"
define audioending15 = "audio/万代传承（结局用）.mp3"
define audioending234 = "audio/跨时空的梦（第2.3.4结局）.mp3"
define audio2 = "audio/赴大荒（第二幕）.mp3"
define audio3 = "audio/观心（第三幕）.mp3"

image yanliao12:
    "images/加井水颜料.jpg"
image temple:
    "images/寺庙.jpg"
image endingwoodcut:
    "images/结局一.jpg"
image bg3:
    "images/bg3.jpg"
image i_junguan:
    "images/军官-removebg-preview.png"
    zoom 2.0
    xanchor 0.5
    yanchor 1.0
    xpos 960
    ypos 1080
image gouxian1:
    "images/独自勾线.jpg"
image gouxian21:
    "images/娃娃对比.jpg"
image keiban4:
    "images/掌柜卧床.jpg"
    zoom 1.0
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 720
image endingflowing:
    "images/结局四.jpg"
    zoom 1.2
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 720
image yanliao11:
    "images/颜料化开.jpg"
image yanliao1:
    "images/颜料未化开.jpg" 
image keiban125:
    "images/彩色鲤鱼.jpg"
image keiban12:
    "images/鲤鱼.jpg"
image keiban11:
    "images/门神.jpg"
image yanliao0:
    "images/颜料0.jpg"
image keiban0:
    "images/刻板0.jpg"
image gouxian0:
    "images/勾线0.jpg"
image bginside:
    "images/bg_inside.jpg"
image bg1:
    "images/bg1.jpg"
image bg2:
    "images/bg2.jpg"
    zoom 1.5
image i_lmt:
    "images/lmt-removebg-preview.png"
    zoom 1.8
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 1080
image i_cyqyn:
    "images/cyqyouninan-removebg-preview.png"
    xanchor 2.5
    yanchor 0.5
    xpos 960
    ypos 720
image i_cyqzn:
    "images/cyqzhongnian-removebg-preview.png"
    zoom 1.5
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 1080
image i_cyqwn:
    "images/cyqwannian-removebg-preview.png"
    zoom 1.5
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 1080
image i_wnn:
    "images/wnn-removebg-preview.png"
    zoom 1.5
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 720
image i_sm:
    "images/sm-removebg-preview.png"
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 720

# 定义核心变量：代表你的三个技艺起点
default skill_keiban = 0 # 刻版技能点
default skill_yanliao = 0 # 颜料技能点
default skill_gouxian = 0 # 勾线技能点

# 定义重要选择标记
default apprentice_choice = "" # 记录学徒期选择: "keiban", "yanliao", "gouxian"
default chapter2_choice = "" # 记录第二幕选择
default chapter3_choice = "" # 记录第三幕选择

# 定义结局收集标记（可选）
default ending_unlocked = []


# 游戏在此开始。
label start:
    play music audio1 fadein 2.0
    scene bg1
    "光绪十一年（1885年），你——陈砚青，刚满十五岁。"
    "三年前，你在杨柳青镇的雪地里快冻僵时，被墨香斋掌柜李墨亭捡回了家。"
    "今日是你正式学手艺的第一天。"

    scene bginside # 这里先用文字描述，未来可替换为图片

    "作坊里，案上摆着三样东西：未打磨的梨木版、半碟朱砂、一张描红的'福'字底稿。"
    show i_lmt  with dissolve 
    lmt "学年画，先学'敬物'。"
    "掌柜的手指叩了叩梨木版。"
    lmt "你先选一样上手，选好了，往后的路就跟着物件走。"
    show i_lmt  with dissolve:
        xpos 500
    show i_cyqyn with dissolve:
        xpos 1920
    menu apprentice_menu:
        "你选择从哪一样开始？"
        "选梨木版：想先学刻版，听说木版是年画的根":
            $ apprentice_choice = "keiban"
            $ skill_keiban += 1
            jump chapter1_keiban
        "选朱砂：想调颜料，看您上次调的朱砂红得发亮":
            $ apprentice_choice = "yanliao"
            $ skill_yanliao += 1
            jump chapter1_yanliao
        "选描红底稿：想先练勾线，把字描好才能画好人物":
            $ apprentice_choice = "gouxian"
            $ skill_gouxian += 1
            jump chapter1_gouxian
label chapter1_keiban:
    scene bg_inside
    "你抱着梨木版坐在窗边..."
    show i_lmt
    lmt "（给了你两把刀，并指了指木板上的杂纹）：刀身宽平，刃口锋利的这把是平刀，刮杂纹时用平刀，刀刃要贴紧木纹，像给木板”剃胡子 ”"
    lmt "刀头呈弧形，刃口内凹这把是圆刀，遇到木纹拐弯的地方，记得换圆刀”顺拐 ”，别硬切——梨木性韧，硬切会崩茬，板就废了。"
    "第一天刮木版，你握着平刀的手腕发僵，刀刃没贴紧木纹，“噌”地一下在木版边缘划了道小口，血滴在浅褐色的木纹里，晕开一点暗红。"# ... 你的详细文本描述 ...
    lmt "（缓缓走过来，手里拿着块磨石，给了你两个建议）"

    menu keiban_choice_1:
        "你决定..."
        "按老规矩，把带血的木版一角削掉":
            show i_lmt
            lmt "“血不沾版，艺才干净”，削的时候用圆刀斜着下刀，“刀角要卡着木纹的‘筋’，别断了木版的‘气’”"# ... 你的文本 ...
            $ skill_keiban += 2 # 成功完成，技能提升更多
            "你取来圆刀，按掌柜说的，刀角贴着木纹的斜向，轻轻一旋，带血的木角就掉了下来，断面光滑，没崩一点木茬。"
            lmt "（凑近看断面，点头）嗯，滑而不崩，是会用刀了。"
            "晚上，你被他叫到灯下。"
            lmt "(铺开一张“门神秦琼”的板样，手指在上面缓缓移动)：认板纹要”看木纹“。（指尖点一处直纹）你看这处直纹，适合刻秦琼的铠甲片，用平刀推刻，手腕稳着送到底，（比划推刀动作）一刀下去就是一条直边"
            lmt "(又移向另一处旋纹)再看这处旋纹，转着长，正好刻他的护心镜，（手指画圈）用圆刀转着刻，弧度才圆活。” "
            show i_cyqyn:
                xpos 1920
            show i_lmt:
                xpos 500
            mc "所以……刀得顺着木头的性子走？"
            lmt "（微笑）是让它替你说话。明天起，你先用铅笔在板上描纹路——描准了，再动刀。"
            "你按着掌柜的说法，先用铅笔在木板上描出纹路走向，再换平刀推刻铠甲——推刀时手臂不动，全靠手腕发力，一刀推到底，木渣呈细条状掉下来，才算合格。"
            scene keiban11 with dissolve
            "练了半个月后，你递上刻好的第一块“门神秦琼”板。"
            hide i_cyqyn
            show i_lmt
            lmt "（拈起，对着灯细看每一道线）：让我看看呵......"
            lmt "（点头）劲透进去了。"
            lmt "（取来印泥试印，纸上渐显门神轮廓。他凝视良久，轻放拓样）铠甲片直挺，护心镜圆润，甲是甲的骨，镜是镜的魂……这板，能用了。"
            jump chapter2_intro # 进入第二幕
        "用清水把血擦干净，继续刮版":
            show i_lmt
            lmt "（站在旁边，握着你的手腕教你“借力”）：刮杂纹时，平刀要跟着木纹的”顺向 ”走。"# ... 你的文本 ...
            $ skill_keiban += 1 # 选择2的技能提升略少
            lmt "（接过平刀示范，刀身微微倾斜）比如这道木纹是从左往右斜，刀就从左往右推，不是使蛮力，是让木纹带着刀走。你试试。"
            " 你试着放松手腕，果然，平刀顺着木纹轻轻一刮，细木渣就掉了下来，木版表面变得光滑。"
            show i_cyqyn:
                xpos 1920
            show i_lmt:
                xpos 500
            mc " ……确实轻松多了。"
            hide i_cyqyn
            hide i_lmt
            "几日后，刻“鲤鱼”板时，"
            show i_lmt
            lmt "刻鱼鳞要用圆刀“点刻”，刀头轻轻扎进木板，顺时针转半圈，留下一个月牙形的刀痕，每片鱼鳞的刀痕方向要一致"
            "（他手腕灵巧一旋，木板上留下个月牙凹痕）"
            lmt "这样印出来的鱼鳞，才会有叠压的立体感。"
            hide i_lmt
            "你看着掌柜的操作，日复一日的练习，刻板。"
            "几天后，你将刻好的板和试印后的宣纸交给掌柜看。"
            scene keiban125 with dissolve
            show i_lmt
            lmt "（拎着纸走到窗边细看）……这鳞会呼吸。"
            hide i_lmt
            "（某日，镇里张婶来送货，瞥见晾着的鲤鱼印样）"
            scene keiban12 with dissolve
            "张婶：（凑近瞧了又瞧）哎哟，这鱼鳞活泛得——（转头对掌柜笑）给我留两张，贴厨房水缸边上！看着就有活气！"
            "（掌柜朝你抬了抬下巴，你正埋头擦新板的木屑，耳根却悄悄红了）"
            jump chapter2_intro
label chapter1_yanliao:
    scene yanliao0
    "你蹲在颜料缸前，掌柜给了你一本泛黄的《颜料谱》，又摆开一锭暗红朱砂、一罐碎桃胶和一口小石臼"
    lmt "调朱砂分三步——”研、泡、搅 ”。"
    lmt "（手指轻点朱砂块）先把朱砂块研成粉，要足够细才行。"
    lmt "（又指桃胶）再用温水泡桃胶，最后把这俩搅匀，记住，比例是一两朱砂加三钱桃胶。"
    lmt "（抬起头，目光看向你）多一钱胶会发暗，少一钱色会散。"
    "你拿起那朱砂块放进石臼，握着石杵开始研磨。可刚研了几下，朱砂块就滑到石臼边，研出来的粉也粗细不均。"
    lmt "（蹲下身，手轻轻覆在你握杵的手上）：石杵要贴着石臼内壁，顺时针慢慢转，力度要匀，像磨豆腐，急了磨不细，慢了磨不出。"
    "（他松开手，看你慢慢找到节奏）"
    lmt "研好还得过一遍“绢筛”。（取来一面细绷的绢筛）筛不下的粗粒，要回头再研。若偷懒留在里头……（指尖捻起一点粗粉）印在纸上会扎手，画就“破相”了。"
    "你按着掌柜的说法，研了半个时辰，终于筛出一碗细如粉尘的朱砂粉。"
    "接着泡桃胶，你把三钱桃胶放进碗里，加了半碗温水，可桃胶却浮在水面，久久不化。"
    scene yanliao1
    "你正低头看着不知所措时，师兄陈墨悄悄凑过来"
    "师兄（压低声音）:师弟，卡在这啦？两个法子——"
    "（伸出食指）一是按册子里的老规矩来，用筷子把桃胶搅碎，再泡半个时辰，错不了的。"
    "掌柜他总说桃胶要”醒透 ”，不然调进朱砂里会结块，还说泡好的桃胶要像“蜂蜜水”，用筷子挑起来能拉出细丝，才算合格"# ... 你的详细文本描述 ...
    "（他瞥了眼掌柜的方向，声音更轻）二是加一点镇上那口井里的活水，再把碗放在温水里“温泡”。"
    "我上次看掌柜加过，他说活水的”灵气 ”能让桃胶化得快，拿温水慢慢温泡能让胶性更匀。"

    menu yanliao_choice_1:
        "你决定..."
        "按册子来，用筷子把桃胶搅碎，再泡半个时辰":
            show i_lmt
            lmt "（在一旁看着，点头）现在把朱砂粉倒进胶水里。记住，搅朱砂要“朝一个方向”，不然颜料会“泄”，印出来的色发灰。"
            "（你接过竹搅棒，顺时针搅动一刻钟，手臂都酸了，朱砂终于和桃胶完全融合，倒在瓷碟里，红得像初凝的血，亮得能映出人影。）"# ... 你的文本 ...
            $ skill_yanliao += 1 # 成功完成，技能提升更多
            scene yanliao11
            lmt "（仔细端详后，将《颜料谱》后半本递给你，翻开一页）调石绿得加“槐花汁”。（指尖轻点书页）须选清晨带露的槐花，捣烂滤汁，按一两石绿加二钱槐花汁的比例调，这样石绿会透出青气，像春天的柳叶。"
            "（又翻过一页）"
            lmt "调石青则要“晒三日”。第一天晒正午太阳，第二天晒傍晚夕阳，第三天晒清晨朝阳。晒足三日，石青色泽更沉稳，印在门神袍上，像染了蓝天的色。"
            "你搅了足足一刻钟，手臂都酸了，朱砂终于和桃胶完全融合，倒在瓷碟里，红得像初凝的血，亮得能映出人影。"
            "掌柜看到后，把《颜料谱》的后半本给了你，指着其中一页说"
            lmt "调石绿要加‘槐花汁’，得选清晨带露的槐花，捣烂后滤出汁，按一两石绿加二钱槐花汁的比例调，这样石绿会透着青气，像春天的柳叶。"
            lmt "调石青要‘晒三日’，第一天晒正午的太阳，第二天晒傍晚的夕阳，第三天晒清晨的朝阳，晒足三日，石青会更沉稳，印在门神的袍子上，像染了蓝天的色。"
            jump chapter2_intro # 进入第二幕
        "加一点镇上井里的活水，再把碗放在温水里“温泡”":
            scene yanliao12
            "你加了点井水，把碗放进温水里温泡。果然，桃胶半个时辰就化开了，你将温泡好的桃胶水轻轻倾倒出来，发现碗底沉着些微小胶粒，未多留意便与朱砂粉一同调匀。"# ... 你的文本 ...
            $ skill_yanliao += 2 # 选择2的技能提升略少
            "试印晾干后，纸上颜色略浅，且散布着细小红点。"
            show i_lmt
            lmt "（接过印纸，对着窗光细看，指尖点在一处红点上）这法子是好的，但“色牢、色匀”这个根基不能丢。"
            lmt "（转向你）你看这些红点，是未化开的朱砂颗粒。若印在年画上，贴出门去，风吹雨打几日便会剥落。再者，桃胶未醒透，胶性不足，颜色也挂不住。"
            lmt "（取过一小碗澄澈透亮的桃胶水）：现再我教你“补胶”。往这颜料里，再加一钱已泡透的桃胶水。"
            lmt "（将胶水缓缓注入）记住，补胶时要慢，让新胶与旧胶融成一体。"
            lmt "（递来竹搅棒）仍按一个方向，搅上十分钟。"
            "（你依言补胶重搅，再次试印。）"
            lmt "(拿起新印纸仔细端详，面上露出笑意)：嗯，这回成了。颜料是年画的“皮”，皮要光滑，色要饱满，才算合格。"
            jump chapter2_intro
label chapter1_gouxian:
    scene gouxian0
    "你坐在临窗的画案前，握着一支硬毫笔。笔锋尖细如针，弹性极佳。面前是李墨亭亲绘的“福”字墨线稿——油烟墨在棉连纸上泛着乌亮的光。"
    "你深吸一口气，笔尖落纸，可笔锋刚一受力就散岔，横画写出左高右低的斜坡，边缘洇出毛刺。"
    lmt "（走过来，铺上一张新的棉连纸，从背后握住你的手）勾线要“三定”：腕定、笔定、气定。"
    lmt "（掌心温暖干燥）腕贴案如碗底着桌，只动碗口，不动碗底。笔握“中正”——"
    lmt "（调整你的手指）拇指食指捏笔杆，中指抵笔肚，无名小指虚蜷如握卵。气沉丹田，眼随笔尖走，看起笔藏锋、行笔提按、收笔回锋。"# ... 你的详细文本描述 ...
    "（你重新调整，腕贴桌案，笔尖轻触纸面——起笔处留下一个圆润的墨点，行笔至中段微微提笔，收笔时手腕轻回。虽仍歪斜，但已无毛边。连续三日，进展甚微。）"
    scene bginside
    show i_wnn with dissolve
    "（这天，来取《连年有余》的老主顾王奶奶端详你的字稿，放下茶碗）"
    wnn "孩子，笔还生。我给你提两点："
    wnn "（伸出食指）第一，固本培元：“先练骨架，再画皮肉”。你在废纸上练“永字八法”。（指着案面木纹）横画与木纹平，竖画与窗棂直。练满百刀纸，手腕自有“筋骨”。当年我爹学画，光一个“横”练了三个月，你更要练习了。"
    wnn "（又伸出第二根手指）第二，以形带功：“画活了鱼，线自然活”。"
    wnn "你先临《连年有余》的鲤鱼。（展开一幅旧稿）杨柳青的鱼，背弧如弓，腹圆如鼓。勾鱼身时，笔尖要“压-提-转”，像鱼在水里摆尾。鱼活了，你的手腕就“松”了。"
    wnn "（看着你）你想先从哪样练起？"
    menu gouxian_choice_1:
        "你决定..."
        "固本培元：“先练骨架，再画皮肉”“孩子，在废纸上练‘永字八法’。”":
            scene gouxian1
            "你每天在废纸上练上百个横画，一开始总与木纹对不齐。练到第五天，终于能画出和木纹平行的横画，起收笔清晰，中间粗细均匀。接着练竖画，对着灯芯一笔笔写，手腕渐稳。"
            "半个月后，你再描“福”字，横画平如木纹，竖画直如灯芯，还能在转弯处“转锋”。"
            show i_lmt
            lmt "（拿起你的新稿，笑着递来一幅“娃娃抱鱼”底稿）如今骨架稳了。你看这娃娃衣褶——（指着袖口）"
            lmt "贴在身上的褶要“重笔”，笔锋按得重一点，线条粗；"# ... 你的文本 ...
            lmt "（移向衣角）飘起来的褶要“轻笔”，笔锋提一点，线条细。这样衣褶才有层次感，像真的布一样。"
            "（你按此法勾描，袖口重笔，衣角轻笔，勾出的衣褶果然立体。）"
            $ skill_keiban += 2 # 成功完成，技能提升更多
            jump chapter2_intro # 进入第二幕
        "以形带功：“画活了鱼，线自然活”“先临《连年有余》的鲤鱼。”":
            "（你开始临摹“连年有余”的鱼。一开始，鱼身画得像根棍子。）"
            show i_wnn with fade
            wnn "（俯身指点）先画“鱼骨架”。（用铅笔在纸上轻轻画一条弧线）这是鱼脊，要弯如弓。"# ... 你的文本 ...
            $ skill_keiban += 1 # 选择2的技能提升略少
            wnn "（在两侧添上小弧线）这是鱼腹，要圆如鼓。骨架立住了，再上笔勾形。"
            hide i_wnn
            "你按此法，先画骨架，再用毛笔勾轮廓。勾鱼身时，笔锋从鱼头开始，慢慢向右行，到鱼腹处轻轻按笔，到鱼尾处再提笔；勾鱼尾时，笔锋分两叉，向左向右各画一条弧线，两尖对齐如剪刀。"
            "练了一周，你画的鱼终于有了“游感”。"
            scene keiban125
            "（此时你再描“福”字，发现手腕稳了许多。）"
            show i_lmt
            lmt "（点头赞许）会找巧劲了。"
            lmt "（指着娃娃稿的眼睛）勾娃娃眼睛要“点睛”：先用细笔勾出圆形的眼白，再在中间偏上点一个小黑点当眼珠。这样娃娃的眼睛才会“亮”，像在笑。"
            "（你试着点睛，娃娃的脸一下子活了，像要从纸上跳下来。"
            jump chapter2_intro
label chapter2_intro:
    
    play music audio2 fadein 2.0 
    scene bg2
    "第二幕：风起杨柳青（时间跳转至光绪二十六年，1900年春）"
    "经过半年的学徒生涯，你已经能独立完成一幅简单的年画。但在这一天，一名不速之客的到来打乱了墨香斋的日常。"
    show i_sm with dissolve
    "（清晨，镇口石板路响起陌生的脚步声。一个穿洋装、戴礼帽的中年男人径直走进墨香斋，摘下帽子微微一躬。）..."
    sm "我要五百幅‘百（操着生硬的官话）掌柜的，鄙人史密斯。想订五百幅“百子迎福图”。"
    sm "（从皮包取出一个玻璃瓶）但要用我这洋颜料——"
    sm "（又抽出一张画片）还要把娃娃头发画成金色，像我们那儿的娃娃。"
    "（掌柜盯着那瓶刺目的金色颜料，眉头渐渐拧紧。他沉默片刻，转身朝后院唤你过去。）"
    hide i_sm
    show i_cyqzn:
        xpos 1420
    show i_lmt:
        xpos 500
    lmt "（压低声音）你来。这不是生意，是要改我们杨柳青的根。（目光沉静地看着你）跟了我半年手艺，这事，你得一起拿个主意。"
    hide i_lmt
    hide i_sm
    show i_cyqzn with dissolve
    "你陷入沉思..."
    hide i_cyqzn
    # 根据第一幕的选择，显示不同的选项菜单
    if apprentice_choice == "keiban":
        scene bg3
        show i_cyqzn:
            xpos 1420
        show i_lmt:
            xpos 500
        mc "（低声对掌柜说）师父，我去库房看过他那“洋模板”了，刻的是洋人的花纹，根本不是咱杨柳青的“娃娃脸”。"
        mc "（想起掌柜平日教诲）您说过，“木板是根”。"
        lmt "（眼神一凛）你要怎么做？"
        menu chapter2_keiban_menu:
            "作为刻版学徒，你决定..."
            "当着镇民的面，把洋模板和老木版摆在一起对比,对比两种纹路，揭穿他想改手艺的心思":
                $ chapter2_choice = "keiban_public"
                jump chapter3_keiban_public
            "偷偷把老木版藏到镇外的庙里，再假意答应，拖延时间，找机会让他放弃":
                $ chapter2_choice = "keiban_hide"
                jump chapter3_keiban_hide

    elif apprentice_choice == "yanliao":
        scene bg3
        show i_cyqzn:
            xpos 1420
        show i_lmt:
            xpos 500
        mc "（取来试调的样纸，面色凝重）师父，我用他的洋颜料试过，颜色虽亮，但存在晕开的问题，根本不适合咱杨柳青的“套色”。"
        mc "（翻开《颜料谱》）您册子上写的“色牢为魂”，这洋颜料最多贴两个月就会掉色，还会开裂。"
        lmt "（点头）你看得准。那依你之见？"
        menu chapter2_yanliao_menu:
            "作为颜料学徒，你决定..."
            "带着真颜料和洋颜料的样画，去邻镇找其他画坊联合抵制,不让他毁了“颜料口碑”":
                $ chapter2_choice = "yanliao_unite"
                jump chapter3_yanliao_unite
            "把真颜料的配方写在纸上，交给师兄，让他藏好，再假装和史密斯合作，偷偷用真颜料掺着洋颜料画，保住“色牢”。":
                $ chapter2_choice = "yanliao_mix"
                jump chapter3_yanliao_mix

    elif apprentice_choice == "gouxian":
        scene bg3
        show i_cyqzn:
            xpos 1420
        show i_lmt:
            xpos 500
        mc "（铺开自己按史密斯要求试画的“金发娃娃”）师父您看，这样画出来的，根本没有咱杨柳青“胖娃娃”的憨劲，显得生硬。（想起王奶奶的话）王奶奶说过，“画要像人，才有灵气”，这洋娃娃不是咱镇民喜欢的样子。"
        lmt "（端详画稿，叹息）灵气没了，画就死了。你觉着该怎么回绝他？"
        menu chapter2_gouxian_menu:
            "作为勾线学徒，你决定..."
            "去集市上，让镇民选你画的'传统胖娃娃'和'金发娃娃',用大家的选择说服史密斯放弃":
                $ chapter2_choice = "gouxian_vote"
                jump chapter3_gouxian_vote
            "把传统“百子迎福图”的底稿多描几份，藏在作坊的夹层里，再按史密斯的要求画，等他走后继续印传统年画":
                $ chapter2_choice = "gouxian_hide"
                jump chapter3_gouxian_hide
    
label chapter3_keiban_public:

    play music audio3 fadein 7.0
    scene bg2
    "灰烬中的刀痕：庚子劫后的重生"
    "光绪二十六年六月十八（1900年7月14日）镇中心的戏台上，你的声音还在回荡。老木板的梨木纹理在阳光下泛着温润的光，洋模板的锌板反着冷硬的铁灰。"
    "史密斯的手杖重重砸在戏台木板上，灰溜溜地走了。但你看见他眼中一闪而过的阴狠。"
    "七月廿三（8月17日）洋兵的马蹄踏碎了杨柳青的黎明。这次来的不是史密斯的随从，是真正的军队——八国联军的一支分队，奉命“清理拳匪据点及附属产业”。"
    show i_junguan with fade
    "领头的军官操着生硬的汉语：“有举报，这里藏有敌视西洋文明的木板，必须销毁。”"

    "你带着师兄们把七十三块核心老板搬进地窖，用柴草掩好入口。刚爬上来，刺刀已经顶在了作坊门口。"
    hide i_junguan
    show i_cyqzn with dissolve
    mc "“要烧就烧我。”（你举起刻刀，刀刃对着自己的胸膛）“别碰老木板。”"
    "要烧老匠人们来了，镇民们来了，手挽手站成人墙。"
    hide i_cyqzn
    show i_junguan with dissolve
    "但那军官只是（冷笑），掏出一纸公文：“联军司令部令，凡有抵抗，以拳匪论处，可就地枪决。"
    "话音刚落，我左脚便踏了出去，握着刻刀的手臂高高地扬起，众人脸色骤变，师兄一把拉住想冲到那狗官面前的我"
    "老匠人们说：“小陈子，冷静一点。”"
    "师兄们也在（极力劝阻）我说：“陈师弟，你别这样。留得青山在，不怕没柴烧啊！”"
    "火是在午时起的。洋兵浇上煤油，将七十三块老木板堆在墨香斋的天井里。"
    "火舌舔上《门神秦琼》的铠甲时，发出噼啪的脆响——那是桃胶和百年梨木最后的悲鸣。《连年有余》的鲤鱼在火焰中扭曲，《百子迎福》的娃娃脸被浓烟熏黑。"
    "你（跪在火堆前三丈远的地方），（眼睁睁）看着自己学徒时第一刀刻下的那道痕——那道曾滴过你的血、又被你亲手削平的木纹——在烈焰中卷曲、碳化、化为飞灰。"
    hide i_junguan with dissolve
    show i_sm
    sm "（站在军官身旁）金丝眼镜后的眼睛（毫无波澜）：“陈，你看。这就是进步的必要代价。”"
    hide i_sm
    jump chapter4_ending # 进入结局判定
label chapter3_keiban_hide:
    
    play music audio3 fadein 2.0
    scene bg3
    "你把老木板藏到庙里"
    "你回去对史密斯说：“老木板得晒三日才能用，我先给您用新木板试印。”"
    "你故意把新木板刻得歪歪扭扭，印出的娃娃脸都是斜的。"
    show i_sm
    sm "（不满意）“你这做的什么东西，在糊弄我呢，我再你等三天，再不把这木板弄好，你们的老木板就别想要了！Do you understand”"
    hide i_sm
    "这三日里，你对师兄说;“师兄你去邻镇找画坊帮忙，还有让镇民们准备好——等史密斯再来，我们就一起拦着他。”"
    "可没想到，第二日洋兵就进了镇，史密斯带着人直接去了作坊，要找老木板。"
    show i_cyqzn:
            xpos 1420
    show i_sm:
            xpos 500
            ypos 720
    mc "“您不知道啊，您前脚刚走，当天晚上就有扒手来把老木板偷走了。我现在也着急找啊！”"
    sm "你以为我会相信你说的谎话吗，陈，我这次不会相信你了。"
    "但是什么都没找到，史密斯（恼羞成怒）：“给我把那些该死的新木板都烧了。”"
    hide i_cyqyn
    hide i_sm
    scene temple
    "幸好你藏在庙里的老木板没被发现，战乱过后，你用老木板重新开始印画。"
    jump chapter4_ending # 进入结局判定
label chapter3_yanliao_unite:
   
    play music audio3 fadein 2.0
    scene bg3
    "你带着真颜料和洋颜料的样画，跑了三个邻镇，找到了五家画坊。 "
    "大家一看洋颜料会掉色（着急）：“这要是让他卖出去，咱们杨柳青年画的名声就毁了！”"
    "于是有人提议：“各位，咱们大家约定好，谁都别把画卖给那个洋鬼子，咱们还在得镇里贴告示，告诉大伙这洋颜料孬的很，比不上我们自己的颜料一星半点。”"
    show i_sm
    sm "(恼羞成怒)没一个有眼光，这画，没你们中国画坊也一样能做！"
    "史密斯后来自己找工人画，可他的工人不会调真颜料，画的年画没几天就掉色了。"
    hide i_sm
    "百姓们都不买（鄙夷）:”瞧这年画，咱就说不行吧，那黄头发的真以为咱的杨柳青年画是那么好复刻的啊，还真是关公门前耍大刀。”"
    "庚子事变时，你和邻镇的画坊一起，把真颜料藏在山洞里。"
    "战乱过后，大家一起改良了颜料配方，让颜色更亮、更耐存。"
    jump chapter4_ending # 进入结局判定
label chapter3_yanliao_mix:
    
    play music audio3 fadein 2.0
    scene bg3
    "你按史密斯的要求画年画，却偷偷在洋颜料里掺了朱砂——这样既符合他“金色头发”的要求，又能让颜色耐存。"
    "印好的年画送到史密斯手里，他没发现异常，可等他运到北京去卖时，却发现年画的颜色比其他洋颜料画的亮多了，百姓们（惊讶）都（抢着买）:“嘿，这外邦人的年画还真有我们这里年画的一点意思，这颜色鲜艳的，跟其他洋鬼子的都不是一个档次的。”"
    show i_cyqzn:
            xpos 1420
    show i_sm:
            xpos 500
            ypos 720
    sm "（好奇）陈，这画的颜色那么鲜艳是怎么回事。"
    mc "（自得）这是我们杨柳青的‘秘方’，你要想知道就得按我们的杨柳青的规矩来。"
    sm "（无奈）没办法，只能答应：“I promise，陈，我不用洋模板，也不用洋颜料。”"
    "庚子事变爆发后，你把真颜料配方交给了掌柜，自己带着掺料的年画，去给逃难的百姓贴，让大家在战乱里也能看到点红色的希望。"
    jump chapter4_ending # 进入结局判定  
label chapter3_gouxian_vote:
    
    play music audio3 fadein 2.0
    scene gouxian21
    "你在集市上摆了两张画：一张是你画的传统“胖娃娃”，娃娃抱着红鲤鱼，脸圆圆的，眼睛亮晶晶；另一张是“金发娃娃”，头发是金色的，脸尖尖的。"
    show i_cyqzn
    "你吆喝着：”来瞧一瞧，看一看喽，正宗杨柳青年画还有外邦板年画！“"
    "镇民们（认可）围过来，都（指着传统娃娃）说：“这才是咱们杨柳青的娃娃，看着就喜庆！”"
    "还有人（皱眉）说：“金发娃娃看着生分，贴在家里不踏实。”"
    "史密斯看到大家都选传统娃娃，只能放弃改样子的要求，还让你按传统样式画。"
    "庚子事变时，你画的传统娃娃年画成了镇民的“定心符”——大家（感慨，把画贴在门上），说“看到这喜人的娃娃啊，俺们就觉得这日子还能过得下去。”"
    jump chapter4_ending # 进入结局判定
label chapter3_gouxian_hide:
   
    play music audio3 fadein 2.0
    "你把传统底稿藏好后，按史密斯的要求画了金发娃娃，可印的时候，你故意少印了一半，假装说“纸不够了”。"
    "等史密斯走后，你拿出传统底稿，连夜印了很多传统年画，分给镇民。"
    "大家拿到画，都高兴地说：“还是这老样子看着舒服。前些天那些新年画像什么样子啊，咱这是杨柳青镇，又不是那外邦。”"
    "庚子事变爆发，洋兵进镇要烧底稿，你把底稿裹在衣服里，躲到了地窖里。“人在，这底稿就在，这杨柳青年画的根啊，可不能丢啊。”"
    "战乱过后，你把底稿拿出来，教镇里的孩子怎么描线，怎么画传统娃娃——很多孩子就是从这时开始喜欢上年画的。"
    jump chapter4_ending # 进入结局判定
label chapter4_ending:
    # 基于 apprentice_choice, chapter2_choice, chapter3_choice 进行判断
    if apprentice_choice == "keiban" and chapter2_choice == "keiban_public":
        # 条件：刻版起点 + 当众对比 
        jump ending_woodcut_legacy
    elif apprentice_choice == "yanliao" and chapter2_choice == "yanliao_unite":
        # 条件：颜料起点 + 联合抵制 
        jump ending_pigment_new
    elif apprentice_choice == "gouxian" and chapter2_choice == "gouxian_vote":
        # 条件：勾线起点 + 集市选画
        jump ending_line_emotion
    elif chapter2_choice == "keiban_hide" or chapter2_choice == "yanliao_hide" or chapter2_choice == "gouxian_hide":
        jump ending_flowing
    else:
        # 默认结局或技艺断层结局
        jump ending_fracture

label ending_woodcut_legacy:
    play music audioending15 
    "结局1：木版永续"
    "光绪二十七年春（1901年9月）《辛丑条约》签了，联军撤了，运河又开始行船。"
    scene keiban4
    "墨香斋的废墟上长出了野草。李墨亭掌柜在去年冬天咳血去世，临终前拉着你的手，只说了三个字：“要……记得。”"
    scene endingwoodcut with dissolve
    show i_cyqzn with dissolve
    "“我要记得什么？”你迷茫地坐在废墟间，手指抚过焦黑的梁木。“这作坊里还剩些什么。”"
    scene endingwoodcut
    "作坊里什么都没有了——板烧了，颜料被抢了，底稿化灰了。连那本蓝布封面的《颜料谱》，都在混乱中被洋兵当成引火纸投入灶膛。"
    "你只剩下记忆，可记忆还有多少呢？“一两朱砂，三钱桃胶……”你惶恐地闭上眼，默诵比例。然后卡住了——”桃胶要泡多久？温水还是冷水？画《鲤鱼》时，鱼鳞的点刻是顺时针还是逆时针？怎么办，我记不清了。“记忆像一匹被虫蛀的锦缎，一扯就破出窟窿。"# ... 粘贴结局1的文本 ...
    "掌柜的“顺拐刀法”，只在特定的木纹拐角处手腕要抖那一下——你见过千百次，但从没问过为什么。"
    "王奶奶勾鱼尾的“剪刀尖”，左边比右边长一分——她说这样鱼才“有劲”，可这一分的分寸在哪里？"
    "《颜料谱》角页上，李掌柜用朱笔批的那行小字是什么？你只记得关于槐花汁要“晨露未晞时采”，可后面的半句呢？"
    "你成了自己技艺的局外人。你终于意识到：有些东西，烧掉了就是烧掉了。“杨柳青年画的根，师傅，我该去哪里找啊。” "
    $ ending_unlocked.append("木版永续")
    return # 游戏结束

label ending_pigment_new:
    play music audioending234 
    "结局2：颜料新生"
    "你和邻镇画坊改良的颜料配方，成了杨柳青年画的核心技艺之一——这种颜料不仅颜色正，还能保存上百年。"
    "你把配方写成了一本新的《颜料谱》，里面不仅有比例，还有你学徒时调颜料的心得，以及其他师兄的巧思，"# ... 粘贴结局2的文本 ...
    show i_cyqwn
    mc "按我们老一辈人的经验，这朱砂啊，一定要搅够半个时辰"
    mc "这石绿啊，得要选晨露洗过的槐花来才做得漂亮"
    "后来，《颜料谱》成了非遗传承的教材，很多画坊都按你的配方调颜料。"
    $ ending_unlocked.append("颜料新生")
    return

label ending_line_emotion:
    play music audioending234 
    "结局3：勾线传情"
    "你教孩子们勾线时，还是从“横平竖直”开始，告诉他们“孩子们，勾线不仅是画形，更是传情——娃娃的笑脸要勾得圆，鱼的尾巴要勾得活。你们可得把心用在手上，这样才能让别人，感受到你们做这年画的感情啊！”。"
    "庚子事变后，你画的“传统胖娃娃”成了杨柳青年画的经典样式，很多人学年画，都是从临摹你的娃娃开始。"# ... 粘贴结局3的文本 ...
    "你还把勾线的技巧编成了口诀，比如“腕要稳，笔要轻，娃娃眼睛要点睛”，方便孩子们记忆。"
    $ ending_unlocked.append("勾线传情")
    return

label ending_flowing:
    play music audioending234 
    "结局4：流动的传承"
    scene endingflowing
    "战乱过后，你推着一辆小车，车上装着老木板、真颜料和传统底稿，走街串巷地印年画。遇到想学的人，你就免费教——教人刻板，教人调颜料，教人勾线。"
    "看着眼前画面你感慨道：“我教这年画啊，不为别的，就是怕我这代人在战火后断了杨柳青年画的根呐。"
    "你的小车走到哪里，杨柳青年画就传到哪里。"
    "后来，很多人跟着你的小车学手艺，慢慢形成了“流动传习”的模式，让杨柳青年画在更多地方扎了根。"
    $ ending_unlocked.append("流动的传承")
    return

label ending_fracture:
    play music audioending15 
    "结局5：技艺断层"
    "庚子事变时，你为了逃命，丢了老木板或真颜料配方，也没藏好传统底稿。"
    scene endingwoodcut
    "战乱过后，墨香斋的作坊被烧了，掌柜的也去世了。你想重新学手艺，却发现没人能再教你刻老木板、调真颜料——老匠人要么走了，要么忘了技巧。"
    "镇上的年轻人只能照着旧年画临摹，可画不出老手艺的“魂”。"
    scene temple
    "直到多年后，有人在庙里找到你当年藏的半块老木板，才慢慢找回一点刻板的技巧，但很多技艺，还是永远丢了。"
    $ ending_unlocked.append("技艺断层")
    return              