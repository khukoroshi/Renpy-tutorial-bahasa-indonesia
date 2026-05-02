# TODO: Translation updated at 2026-04-28 23:57

# game/indepth_style.rpy:40
translate indonesian new_gui_17a0326e:

    # e "When you create a new project, Ren'Py will automatically create a GUI - a Graphical User Interface - for it."
    e "Saat Anda membuat proyek baru, Ren'Py akan secara otomatis membuat GUI - Graphical User Interface (Antarmuka Pengguna Grafis) - untuk proyek tersebut."

# game/indepth_style.rpy:42
translate indonesian new_gui_12c814ed:

    # e "It defines the look of both in-game interface, like this text box, and out-of-game interface like the main and game menus."
    e "Ini mendefinisikan tampilan antarmuka di dalam game, seperti kotak teks ini, maupun antarmuka di luar game seperti menu utama dan menu game."

# game/indepth_style.rpy:44
translate indonesian new_gui_0a2a73bb:

    # e "The default GUI is meant to be nice enough for a simple project. With a few small changes, it's what you're seeing in this game."
    e "GUI default dirancang agar cukup bagus untuk proyek sederhana. Dengan beberapa perubahan kecil, itulah yang Anda lihat di game ini."

# game/indepth_style.rpy:46
translate indonesian new_gui_22adf68e:

    # e "The GUI is also meant to be easy for an intermediate creator to customize. Customizing the GUI consists of changing the image files in the gui directory, and changing variables in gui.rpy."
    e "GUI juga dirancang agar mudah disesuaikan oleh pembuat tingkat menengah. Menyesuaikan GUI terdiri dari mengubah file gambar di direktori 'gui', dan mengubah variabel dalam 'gui.rpy'."

# game/indepth_style.rpy:48
translate indonesian new_gui_da21de30:

    # e "At the same time, even when customized, the default GUI might be too recognizable for an extremely polished game. That's why we've made it easy to totally replace."
    e "Pada saat yang sama, meskipun sudah disesuaikan, GUI default mungkin masih terlalu mudah dikenali untuk game yang sangat terpoles. Itulah sebabnya kami memudahkannya untuk diganti secara total."

# game/indepth_style.rpy:50
translate indonesian new_gui_45765574:

    # e "We've put an extensive guide to customizing the GUI on the Ren'Py website. So if you want to learn more, visit the {a=https://www.renpy.org/doc/html/gui.html}GUI customization guide{/a}."
    e "Kami telah menyediakan panduan ekstensif untuk menyesuaikan GUI di situs web Ren'Py. Jadi, jika Anda ingin mempelajari lebih lanjut, kunjungi {a=https://www.renpy.org/doc/html/gui.html}panduan kustomisasi GUI{/a}."

# game/indepth_style.rpy:58
translate indonesian styles_fa345a38:

    # e "Ren'Py has a powerful style system that controls what displayables look like."
    e "Ren'Py memiliki sistem gaya (style) yang kuat yang mengontrol tampilan displayable."

# game/indepth_style.rpy:60
translate indonesian styles_6189ee12:

    # e "While the default GUI uses variables to provide styles with sensible defaults, if you're replacing the GUI or creating your own screens, you'll need to learn about styles yourself."
    e "Meskipun GUI default menggunakan variabel untuk memberikan gaya dengan standar yang wajar, jika Anda mengganti GUI atau membuat layar (screen) sendiri, Anda harus mempelajari tentang gaya secara mandiri."

# game/indepth_style.rpy:68
translate indonesian styles_menu_a4a6913e:

    # e "What would you like to know about styles?" nointeract
    e "Apa yang ingin Anda ketahui tentang gaya?" nointeract

# game/indepth_style.rpy:98
translate indonesian style_basics_9a79ef89:

    # e "Styles let a displayable look different from game to game, or even inside the same game."
    e "Gaya memungkinkan suatu displayable terlihat berbeda dari satu game ke game lainnya, atau bahkan di dalam game yang sama."

# game/indepth_style.rpy:103
translate indonesian style_basics_48777f2c:

    # e "Both of these buttons use the same displayables. But since different styles have been applied, the buttons look different from each other."
    e "Kedua tombol ini menggunakan displayable yang sama. Namun karena gaya yang berbeda telah diterapkan, tombol-tombol tersebut terlihat berbeda satu sama lain."

# game/indepth_style.rpy:108
translate indonesian style_basics_57704d8c:

    # e "Styles are a combination of information from four different places."
    e "Gaya adalah kombinasi informasi dari empat tempat berbeda."

# game/indepth_style.rpy:121
translate indonesian style_basics_144731f6:

    # e "The first place Ren'Py can get style information from is part of a screen. Each displayable created by a screen can take a style name and style properties."
    e "Tempat pertama Ren'Py bisa mendapatkan informasi gaya adalah sebagai bagian dari sebuah layar (screen). Setiap displayable yang dibuat oleh layar dapat menerima nama gaya dan properti gaya."

# game/indepth_style.rpy:138
translate indonesian style_basics_67e48162:

    # e "When a screen displayable contains text, style properties prefixed with text_ apply to that text."
    e "Ketika suatu layar displayable berisi teks, properti gaya dengan awalan 'text_' akan diterapkan pada teks tersebut."

# game/indepth_style.rpy:151
translate indonesian style_basics_03516b4a:

    # e "The next is as part of a displayable created in an image statement. Style properties are just arguments to the displayable."
    e "Berikutnya adalah sebagai bagian dari displayable yang dibuat dalam pernyataan gambar (image). Properti gaya hanyalah argumen untuk displayable tersebut."

# game/indepth_style.rpy:160
translate indonesian style_basics_ccc0d1ca:

    # egreen "Style properties can also be given as arguments when defining a character."
    egreen "Properti gaya juga dapat diberikan sebagai argumen saat mendefinisikan karakter."

# game/indepth_style.rpy:162
translate indonesian style_basics_013ab314:

    # egreen "Arguments beginning with who_ are style properties applied to the character's name, while those beginning with what_ are applied to the character's dialogue."
    egreen "Argumen yang dimulai dengan 'who_' adalah properti gaya yang diterapkan pada nama karakter, sedangkan yang dimulai dengan 'what_' diterapkan pada dialog karakter."

# game/indepth_style.rpy:164
translate indonesian style_basics_dbe80939:

    # egreen "Style properties that don't have a prefix are also applied to the character's name."
    egreen "Properti gaya yang tidak memiliki awalan (prefix) juga akan diterapkan pada nama karakter."

# game/indepth_style.rpy:174
translate indonesian style_basics_ac6a8414:

    # e "Finally, there is the style statement, which creates or changes a named style. By giving Text the style argument, we tell it to use the blue_text style." id style_basics_ac6a8414
    e "Terakhir, ada pernyataan gaya (style statement), yang membuat atau mengubah gaya bernama. Dengan memberikan argumen gaya pada Teks, kita memberitahunya untuk menggunakan gaya 'blue_text'." id style_basics_ac6a8414

# game/indepth_style.rpy:180
translate indonesian style_basics_3d9bdff7:

    # e "A style property can inherit from a parent. If a style property is not given in a style, it comes from the parent of that style."
    e "Sebuah properti gaya dapat mewarisi (inherit) dari induknya. Jika properti gaya tidak ditentukan dalam suatu gaya, maka properti tersebut diambil dari induk gaya tersebut."

# game/indepth_style.rpy:182
translate indonesian style_basics_49c5fbfe:

    # e "By default the parent of the style has the same name, with the prefix up to the first underscore removed. If the style does not have an underscore in its name, 'default' is used." id style_basics_49c5fbfe
    e "Secara default, induk dari gaya memiliki nama yang sama, namun dengan awalan hingga garis bawah (underscore) pertama dihapus. Jika gaya tersebut tidak memiliki garis bawah pada namanya, maka 'default' yang akan digunakan." id style_basics_49c5fbfe

# game/indepth_style.rpy:184
translate indonesian style_basics_6ab170a3:

    # e "For example, blue_text inherits from text, which in turn inherits from default. The default style defines all properties, so it doesn't inherit from anything."
    e "Sebagai contoh, 'blue_text' mewarisi dari 'text', yang kemudian mewarisi dari 'default'. Gaya 'default' mendefinisikan semua properti, jadi ia tidak mewarisi dari apa pun."

# game/indepth_style.rpy:190
translate indonesian style_basics_f78117a7:

    # e "The parent can be explicitly changed by giving the style statement an 'is' clause. In this case, we're explictly setting the style to the parent of text."
    e "Induk dapat diubah secara eksplisit dengan memberikan klausa 'is' pada pernyataan gaya. Dalam hal ini, kita secara eksplisit mengatur gaya tersebut ke induk dari 'text'."

# game/indepth_style.rpy:194
translate indonesian style_basics_6007040b:

    # e "Each displayable has a default style name. By default, it's usually the lower-case displayable name, like 'text' for Text, or 'button' for buttons."
    e "Setiap displayable memiliki nama gaya default. Secara bawaan, biasanya berupa nama displayable dalam huruf kecil, seperti 'text' untuk Text, atau 'button' untuk tombol."

# game/indepth_style.rpy:196
translate indonesian style_basics_35db9a05:

    # e "In a screen, a displayable can be given the style_prefix property to give a prefix for that displayable and its children." id style_basics_35db9a05
    e "Dalam sebuah layar (screen), suatu displayable dapat diberikan properti 'style_prefix' untuk memberikan awalan bagi displayable tersebut dan anak-anaknya (children)." id style_basics_35db9a05

# game/indepth_style.rpy:198
translate indonesian style_basics_422a87f7:

    # e "For example, a text displayable with a style_prefix of 'help' will be given the style 'help_text'."
    e "Sebagai contoh, displayable teks dengan 'style_prefix' berupa 'help' akan diberikan gaya 'help_text'."

# game/indepth_style.rpy:200
translate indonesian style_basics_bad2e207:

    # e "Lastly, when a displayable is a button, or inside a button, it can take style prefixes."
    e "Terakhir, ketika suatu displayable berupa tombol, atau berada di dalam tombol, ia dapat menerima awalan gaya (style prefixes)."

# game/indepth_style.rpy:202
translate indonesian style_basics_22ed20a1:

    # e "The prefixes idle_, hover_, and insensitive_ are used when the button is unfocused, focused, and unfocusable."
    e "Awalan 'idle_', 'hover_', dan 'insensitive_' digunakan saat tombol tidak disorot, sedang disorot (hover), dan saat tidak dapat diklik."

# game/indepth_style.rpy:204
translate indonesian style_basics_7a58037e:

    # e "These can be preceded by selected_ to change how the button looks when it represents a selected value or screen."
    e "Ini juga dapat diawali dengan 'selected_' untuk mengubah tampilan tombol saat mewakili nilai atau layar yang sedang dipilih."

# game/indepth_style.rpy:233
translate indonesian style_basics_0cdcb8c3:

    # e "This screen shows the style prefixes in action. You can click on a button to select it, or click outside to advance."
    e "Layar ini menunjukkan cara kerja awalan gaya (style prefixes). Anda dapat mengklik tombol untuk memilihnya, atau klik di luar untuk melanjutkan."

# game/indepth_style.rpy:240
translate indonesian style_basics_aed05094:

    # e "Those are the basics of styles. If GUI customization isn't enough for you, styles let you customize just about everything in Ren'Py."
    e "Itulah dasar-dasar gaya. Jika kustomisasi GUI saja tidak cukup bagi Anda, sistem gaya memungkinkan Anda menyesuaikan hampir segala hal di Ren'Py."

# game/indepth_style.rpy:253
translate indonesian style_general_81f3c8ff:

    # e "The first group of style properties that we'll go over are the general style properties. These work with every displayable, or at least many different ones."
    e "Kelompok properti gaya pertama yang akan kita bahas adalah properti gaya umum. Ini berfungsi untuk setiap displayable, atau setidaknya untuk banyak jenis yang berbeda."

# game/indepth_style.rpy:264
translate indonesian style_general_a8d99699:

    # e "Every displayable takes the position properties, which control where it can be placed on screen. Since I've already mentioned them, I won't repeat them here."
    e "Setiap displayable menerima properti posisi, yang mengontrol di mana ia dapat ditempatkan di layar. Karena saya sudah pernah menyebutkannya, saya tidak akan mengulanginya di sini."

# game/indepth_style.rpy:275
translate indonesian style_general_58d4a18f:

    # e "The xmaximum and ymaximum properties set the maximum width and height of the displayable, respectively. This will cause Ren'Py to shrink things, if possible."
    e "Properti 'xmaximum' dan 'ymaximum' masing-masing mengatur lebar dan tinggi maksimum dari displayable. Ini akan menyebabkan Ren'Py mengecilkan objek tersebut jika memungkinkan."

# game/indepth_style.rpy:277
translate indonesian style_general_cae9a39f:

    # e "Sometimes, the shrunken size will be smaller than the size given by xmaximum and ymaximum."
    e "Terkadang, ukuran yang menyusut akan menjadi lebih kecil dari ukuran yang diberikan oleh 'xmaximum' dan 'ymaximum'."

# game/indepth_style.rpy:279
translate indonesian style_general_5928c24e:

    # e "Similarly, the xminimum and yminimum properties set the minimum width and height. If the displayable is smaller, Ren'Py will try to make it bigger."
    e "Demikian pula, properti 'xminimum' dan 'yminimum' mengatur lebar dan tinggi minimum. Jika displayable lebih kecil, Ren'Py akan mencoba membuatnya menjadi lebih besar."

# game/indepth_style.rpy:289
translate indonesian style_general_35a8ee5e:

    # e "The xsize and ysize properties set the minimum and maximum size to the same value, fixing the size."
    e "Properti 'xsize' dan 'ysize' mengatur ukuran minimum dan maksimum ke nilai yang sama, sehingga mengunci ukurannya (fixed size)."

# game/indepth_style.rpy:291
translate indonesian style_general_fcfb0640:

    # e "These only works for displayables than can be resized. Some displayables, like images, can't be made bigger or smaller."
    e "Ini hanya berfungsi untuk displayable yang dapat diubah ukurannya. Beberapa displayable, seperti gambar, tidak dapat dibuat menjadi lebih besar atau lebih kecil (secara otomatis)."

# game/indepth_style.rpy:299
translate indonesian style_general_cd5cc97c:

    # e "The area property takes a tuple - a parenthesis bounded list of four items. The first two give the position, and the second two the size."
    e "Properti 'area' menerima sebuah tuple — daftar empat item di dalam kurung. Dua item pertama menentukan posisi, dan dua item terakhir menentukan ukuran."

# game/indepth_style.rpy:308
translate indonesian style_general_e5a58f0b:

    # e "Finally, the alt property changes the text used by self-voicing for the hearing impaired."
    e "Terakhir, properti 'alt' mengubah teks yang digunakan oleh fitur 'self-voicing' untuk penyandang disabilitas pendengaran."

# game/indepth_style.rpy:335
translate indonesian style_text_fe457b8f:

    # e "The text style properties apply to text and input displayables."
    e "Properti gaya teks berlaku untuk displayable teks dan input."

# game/indepth_style.rpy:337
translate indonesian style_text_7ab53f03:

    # e "Text displayables can be created implicitly or explicitly. For example, a textbutton creates a text displayable with a style ending in button_text."
    e "Displayable teks dapat dibuat secara implisit maupun eksplisit. Sebagai contoh, sebuah 'textbutton' membuat displayable teks dengan gaya yang berakhiran 'button_text'."

# game/indepth_style.rpy:339
translate indonesian style_text_6dd42a57:

    # e "These can also be set in gui.rpy by changing or defining variables with names like gui.button_text_size."
    e "Ini juga dapat diatur dalam 'gui.rpy' dengan mengubah atau mendefinisikan variabel dengan nama seperti 'gui.button_text_size'."

# game/indepth_style.rpy:347
translate indonesian style_text_c689130e:

    # e "The bold style property makes the text bold. This can be done using an algorithm, rather than a different version of the font."
    e "Properti gaya 'bold' membuat teks menjadi tebal. Hal ini dapat dilakukan menggunakan algoritma, alih-alih menggunakan versi file font yang berbeda."

# game/indepth_style.rpy:355
translate indonesian style_text_3420bfe4:

    # e "The color property changes the color of the text. It takes hex color codes, just like everything else in Ren'Py."
    e "Properti 'color' mengubah warna teks. Properti ini menerima kode warna heksadesimal (hex), sama seperti hal lainnya di Ren'Py."

# game/indepth_style.rpy:363
translate indonesian style_text_14bd6327:

    # e "The first_indent style property determines how far the first line is indented."
    e "Properti gaya 'first_indent' menentukan seberapa jauh baris pertama menjorok ke dalam (indentasi)."

# game/indepth_style.rpy:371
translate indonesian style_text_779ac517:

    # e "The font style property changes the font the text uses. Ren'Py takes TrueType and OpenType fonts, and you'll have to include the font file as part of your visual novel."
    e "Properti gaya 'font' mengubah jenis huruf yang digunakan teks. Ren'Py menerima font TrueType (.ttf) dan OpenType (.otf), dan Anda harus menyertakan file font tersebut sebagai bagian dari novel visual Anda."

# game/indepth_style.rpy:379
translate indonesian style_text_917e2bca:

    # e "The size property changes the size of the text."
    e "Properti 'size' mengubah ukuran teks."

# game/indepth_style.rpy:388
translate indonesian style_text_1a46cd43:

    # e "The italic property makes the text italic. Again, this is better done with a font, but for short amounts of text Ren'Py can do it for you."
    e "Properti 'italic' membuat teks menjadi miring. Sekali lagi, ini lebih baik dilakukan dengan font khusus, tetapi untuk teks yang singkat, Ren'Py dapat melakukannya untuk Anda."

# game/indepth_style.rpy:397
translate indonesian style_text_472f382d:

    # e "The justify property makes the text justified, lining all but the last line up on the left and the right side."
    e "Properti 'justify' membuat teks menjadi rata kanan-kiri, meratakan semua baris kecuali baris terakhir pada sisi kiri dan kanan."

# game/indepth_style.rpy:405
translate indonesian style_text_87b075f8:

    # e "The kerning property kerns the text. When it's negative, characters are closer together. When positive, characters are farther apart."
    e "Properti 'kerning' mengatur jarak antar karakter (kerning). Jika nilainya negatif, karakter akan saling mendekat. Jika positif, karakter akan saling menjauh."

# game/indepth_style.rpy:415
translate indonesian style_text_fe7dec14:

    # e "The line_leading and line_spacing properties put spacing before each line, and between lines, respectively."
    e "Properti 'line_leading' dan 'line_spacing' masing-masing memberikan ruang sebelum setiap baris, dan di antara baris."

# game/indepth_style.rpy:424
translate indonesian style_text_aee9277a:

    # e "The outlines property puts outlines around text. This takes a list of tuples, which is a bit complicated."
    e "Properti 'outlines' memberikan garis tepi (outline) di sekitar teks. Ini menerima daftar tuple, yang teknisnya sedikit rumit."

# game/indepth_style.rpy:426
translate indonesian style_text_b4c5190f:

    # e "But if you ignore the brackets and parenthesis, you have the width of the outline, the color, and then horizontal and vertical offsets."
    e "Namun jika Anda mengabaikan kurung siku dan kurung biasa, Anda akan melihat lebar garis tepi, warna, lalu pergeseran (offset) horizontal dan vertikal."

# game/indepth_style.rpy:434
translate indonesian style_text_5a0c2c02:

    # e "The rest_indent property controls the indentation of lines after the first one."
    e "Properti 'rest_indent' mengontrol indentasi untuk baris-baris setelah baris pertama."

# game/indepth_style.rpy:443
translate indonesian style_text_430c1959:

    # e "The textalign property controls the positioning of multiple lines of text inside the text displayable. For example, 0.5 means centered." id style_text_430c1959
    e "Properti 'textalign' mengontrol posisi dari beberapa baris teks di dalam displayable teks tersebut. Sebagai contoh, 0.5 berarti rata tengah." id style_text_430c1959

# game/indepth_style.rpy:445
translate indonesian style_text_19aa0833:

    # e "It doesn't change the position of the text displayable itself. For that, you'll often want to set the textalign and xalign to the same value." id style_text_19aa0833
    e "Ini tidak mengubah posisi dari displayable teks itu sendiri. Untuk itu, Anda biasanya perlu mengatur 'textalign' dan 'xalign' ke nilai yang sama." id style_text_19aa0833

# game/indepth_style.rpy:455
translate indonesian style_text_efc3c392:

    # e "When both textalign and xalign are set to 1.0, the text is properly right-justified." id style_text_efc3c392
    e "Ketika 'textalign' dan 'xalign' keduanya diatur ke 1.0, teks akan menjadi rata kanan dengan benar." id style_text_efc3c392

# game/indepth_style.rpy:464
translate indonesian style_text_43be63b9:

    # e "The underline property underlines the text."
    e "Properti 'underline' memberikan garis bawah pada teks."

# game/indepth_style.rpy:471
translate indonesian style_text_343f6d34:

    # e "Those are the most common text style properties, but not the only ones. Here are a few more that you might need in special circumstances."
    e "Itulah properti gaya teks yang paling umum, tetapi bukan satu-satunya. Berikut adalah beberapa lagi yang mungkin Anda butuhkan dalam keadaan khusus."

# game/indepth_style.rpy:479
translate indonesian style_text_e7204a95:

    # e "By default, text in Ren'Py is antialiased, to smooth the edges. The antialias property can turn that off, and make the text a little more jagged."
    e "Secara default, teks di Ren'Py menggunakan antialias untuk menghaluskan tepiannya. Properti 'antialias' dapat mematikan fitur tersebut dan membuat teks terlihat sedikit lebih tajam/kasar (jagged)."

# game/indepth_style.rpy:487
translate indonesian style_text_a5316e4c:

    # e "The adjust_spacing property is a very subtle one, that only matters when a player resizes the window. When True, characters will be shifted a bit so the Text has the same relative spacing."
    e "Properti 'adjust_spacing' sangat halus, yang hanya berpengaruh saat pemain mengubah ukuran jendela (resize). Jika bernilai True, karakter akan sedikit digeser agar Teks tetap memiliki spasi relatif yang sama."

# game/indepth_style.rpy:496
translate indonesian style_text_605d4e4a:

    # e "When False, the text won't jump around as much. But it can be a little wider or narrower based on screen size."
    e "Jika bernilai False, teks tidak akan terlalu banyak bergeser. Namun teks bisa menjadi sedikit lebih lebar atau sempit tergantung pada ukuran layar."

# game/indepth_style.rpy:505
translate indonesian style_text_acf8a0e1:

    # e "The layout property has a few special values that control where lines are broken. The 'nobreak' value disables line breaks entirely, making the text wider."
    e "Properti 'layout' memiliki beberapa nilai khusus yang mengontrol di mana baris diputus. Nilai 'nobreak' menonaktifkan pemutusan baris sepenuhnya, sehingga teks menjadi lebih lebar."

# game/indepth_style.rpy:516
translate indonesian style_text_785729cf:

    # e "When the layout property is set to 'subtitle', the line breaking algorithm is changed to try to make all lines even in length, as subtitles usually are."
    e "Ketika properti 'layout' diatur ke 'subtitle', algoritma pemutusan baris diubah untuk mencoba membuat semua baris memiliki panjang yang seimbang, seperti gaya subjudul pada umumnya."

# game/indepth_style.rpy:524
translate indonesian style_text_9c26f218:

    # e "The strikethrough property draws a line through the text. It seems pretty unlikely you'd want to use this one."
    e "Properti 'strikethrough' menggambar garis yang mencoret teks. Sepertinya kecil kemungkinan Anda ingin menggunakan yang satu ini."

# game/indepth_style.rpy:534
translate indonesian style_text_c7229243:

    # e "The vertical style property places text in a vertical layout. It's meant for Asian languages with special fonts."
    e "Properti gaya 'vertical' menempatkan teks dalam tata letak vertikal. Ini ditujukan untuk bahasa-bahasa Asia yang menggunakan font khusus."

# game/indepth_style.rpy:540
translate indonesian style_text_724bd5e0:

    # e "And those are the text style properties. There might be a lot of them, but we want to give you a lot of control over how you present text to your players."
    e "Dan itulah properti gaya teks. Mungkin jumlahnya banyak, tetapi kami ingin memberi Anda kontrol penuh atas cara Anda menyajikan teks kepada pemain."

# game/indepth_style.rpy:580
translate indonesian style_button_300b6af5:

    # e "Next up, we have the window and button style properties. These apply to windows like the text window at the bottom of this screen and frames like the ones we show examples in."
    e "Selanjutnya, kita memiliki properti gaya window (jendela) dan button (tombol). Ini berlaku untuk jendela seperti kotak teks di bagian bawah layar ini dan frame seperti contoh yang kami tunjukkan."

# game/indepth_style.rpy:582
translate indonesian style_button_255a18e4:

    # e "These properties also apply to buttons, in-game and out-of-game. To Ren'Py, a button is a window you can click."
    e "Properti ini juga berlaku untuk tombol, baik di dalam maupun di luar game. Bagi Ren'Py, sebuah tombol adalah jendela yang dapat diklik."

# game/indepth_style.rpy:593
translate indonesian style_button_9b53ce93:

    # e "I'll start off with this style, which everything will inherit from. To make our lives easier, it inherits from the default style, rather than the customized buttons in this game's GUI." id style_button_9b53ce93
    e "Saya akan mulai dengan gaya ini, yang akan diwarisi oleh semuanya. Untuk mempermudah kita, gaya ini mewarisi dari gaya default, bukan dari tombol yang telah dikustomisasi di GUI game ini."

# game/indepth_style.rpy:595
translate indonesian style_button_aece4a8c:

    # e "The first style property is the background property. It adds a background to a button or window. Since this is a button, idle and hover variants choose different backgrounds when focused." id style_button_aece4a8c
    e "Properti gaya pertama adalah properti 'background'. Ini menambahkan latar belakang pada tombol atau jendela. Karena ini adalah tombol, varian 'idle' dan 'hover' memilih latar belakang yang berbeda saat difokuskan."

# game/indepth_style.rpy:597
translate indonesian style_button_b969f04a:

    # e "We also center the two buttons, using the xalign position property."
    e "Kami juga menempatkan kedua tombol di tengah menggunakan properti posisi 'xalign'."

# game/indepth_style.rpy:601
translate indonesian style_button_269ae069:

    # e "We've also customized the style of the button's text, using this style. It centers the text and makes it change color when hovered."
    e "Kami juga telah menyesuaikan gaya teks tombol menggunakan gaya ini. Ini menempatkan teks di tengah dan membuatnya berubah warna saat disorot (hover)."

# game/indepth_style.rpy:612
translate indonesian style_button_1009f3e1:

    # e "Without any padding around the text, the button looks odd. Ren'Py has padding properties that add space inside the button's background."
    e "Tanpa padding di sekitar teks, tombol akan terlihat aneh. Ren'Py memiliki properti padding yang menambahkan ruang di dalam latar belakang tombol."



# game/indepth_style.rpy:621
translate indonesian style_button_5bdfa45a:

    # e "More commonly used are the xpadding and ypadding style properties, which add the same padding to the left and right, or the top and bottom, respectively."
    e "Yang lebih umum digunakan adalah properti gaya 'xpadding' dan 'ypadding', yang masing-masing menambahkan padding yang sama ke kiri dan kanan, atau atas dan bawah."

# game/indepth_style.rpy:629
translate indonesian style_button_81283d42:

    # e "The margin style properties work the same way, except they add space outside the background. The full set exists: left_margin, right_margin, top_margin, bottom_margin, xmargin, and ymargin."
    e "Properti gaya margin bekerja dengan cara yang sama, kecuali mereka menambahkan ruang di luar latar belakang. Tersedia set lengkap: left_margin, right_margin, top_margin, bottom_margin, xmargin, dan ymargin."

# game/indepth_style.rpy:638
translate indonesian style_button_0b7aca6b:

    # e "The size_group style property takes a string. Ren'Py will make sure that all the windows or buttons with the same size_group string are the same size."
    e "Properti gaya 'size_group' menerima sebuah string. Ren'Py akan memastikan bahwa semua jendela atau tombol dengan string 'size_group' yang sama memiliki ukuran yang sama."

# game/indepth_style.rpy:647
translate indonesian style_button_4c6da7d9:

    # e "Alternatively, the xfill and yfill style properties make a button take up all available space in the horizontal or vertical directions."
    e "Alternatifnya, properti gaya 'xfill' dan 'yfill' membuat tombol menghabiskan semua ruang yang tersedia dalam arah horizontal atau vertikal."

# game/indepth_style.rpy:657
translate indonesian style_button_fd5338b2:

    # e "The foreground property gives a displayable that is placed on top of the contents and background of the window or button."
    e "Properti 'foreground' memberikan displayable yang ditempatkan di atas konten dan latar belakang jendela atau tombol."

# game/indepth_style.rpy:659
translate indonesian style_button_b8af697c:

    # e "One way to use it is to provide extra decorations to a button that's serving as a checkbox. Another would be to use it with a Frame to provide a glossy shine that overlays the button's contents."
    e "Salah satu cara menggunakannya adalah untuk memberikan dekorasi ekstra pada tombol yang berfungsi sebagai kotak centang (checkbox). Cara lainnya adalah menggunakannya dengan Frame untuk memberikan efek kilau (glossy shine) yang melapisi konten tombol."

# game/indepth_style.rpy:668
translate indonesian style_button_c0b1b62e:

    # e "There are also a few style properties that only apply to buttons. The hover_sound and activate_sound properties play sound files when a button is focused and activated, respectively."
    e "Ada juga beberapa properti gaya yang hanya berlaku untuk tombol. Properti 'hover_sound' dan 'activate_sound' masing-masing memainkan file suara saat tombol difokuskan dan diaktifkan."

# game/indepth_style.rpy:677
translate indonesian style_button_02fa647e:

    # e "Finally, the focus_mask property applies to partially transparent buttons. When it's set to True, only areas of the button that aren't transparent cause a button to focus."
    e "Terakhir, properti 'focus_mask' berlaku untuk tombol yang transparan sebagian. Saat diatur ke True, hanya area tombol yang tidak transparan yang dapat membuat tombol fokus."

# game/indepth_style.rpy:757
translate indonesian style_bar_414d454a:

    # e "To demonstrate styles, let me first show two of the images we'll be using. This is the image we're using for parts of the bar that are empty."
    e "Untuk mendemonstrasikan gaya, izinkan saya menunjukkan dua gambar yang akan kita gunakan. Ini adalah gambar yang kita gunakan untuk bagian bar yang kosong."

# game/indepth_style.rpy:761
translate indonesian style_bar_9422b7b0:

    # e "And here's what we use for parts of the bar that are full."
    e "Dan inilah yang kita gunakan untuk bagian bar yang penuh."

# game/indepth_style.rpy:773
translate indonesian style_bar_8ae6a14b:

    # e "The left_bar and right_bar style properties, and their hover variants, give displayables for the left and right side of the bar. By default, the value is shown on the left."
    e "Properti gaya 'left_bar' dan 'right_bar', serta varian hover-nya, memberikan displayable untuk sisi kiri dan kanan bar. Secara default, nilai bar ditampilkan di sisi kiri."

# game/indepth_style.rpy:775
translate indonesian style_bar_7f0f50e5:

    # e "Also by default, both the left and right displayables are rendered at the full width of the bar, and then cropped to the appropriate size."
    e "Juga secara default, displayable kiri dan kanan dirender pada lebar penuh bar, lalu dipotong (cropped) ke ukuran yang sesuai."

# game/indepth_style.rpy:777
translate indonesian style_bar_9ef4f62f:

    # e "We give the bar the ysize property to set how tall it is. We could also give it xsize to choose how wide, but here it's limited by the width of the frame it's in."
    e "Kami memberikan properti 'ysize' pada bar untuk mengatur tingginya. Kami juga bisa memberikan 'xsize' untuk menentukan lebarnya, tetapi di sini lebarnya dibatasi oleh bingkai (frame) tempatnya berada."

# game/indepth_style.rpy:790
translate indonesian style_bar_d4c29710:

    # e "When the bar_invert style property is True, the bar value is displayed on the right side of the bar. The left_bar and right_bar displayables might also need to be swapped."
    e "Ketika properti gaya 'bar_invert' bernilai True, nilai bar ditampilkan di sisi kanan. Displayable 'left_bar' dan 'right_bar' mungkin juga perlu ditukar posisinya."

# game/indepth_style.rpy:804
translate indonesian style_bar_cca67222:

    # e "The bar_resizing style property causes the bar images to be resized to represent the value, rather than being rendered at full size and cropped."
    e "Properti gaya 'bar_resizing' menyebabkan gambar bar diubah ukurannya (resized) untuk mewakili nilainya, alih-alih dirender pada ukuran penuh lalu dipotong."

# game/indepth_style.rpy:817
translate indonesian style_bar_7d361bac:

    # e "The thumb style property gives a thumb image, that's placed based on the bar's value. In the case of a scrollbar, it's resized if possible." id style_bar_7d361bac
    e "Properti gaya 'thumb' memberikan gambar thumb (pegangan penggeser), yang ditempatkan berdasarkan nilai bar. Dalam kasus scrollbar, ukurannya akan diubah jika memungkinkan."

# game/indepth_style.rpy:819
translate indonesian style_bar_b6dfb61b:

    # e "Here, we use it with the base_bar style property, which sets both bar images to the same displayable."
    e "Di sini, kami menggunakannya dengan properti gaya 'base_bar', yang mengatur kedua gambar bar ke displayable yang sama."

# game/indepth_style.rpy:834
translate indonesian style_bar_996466ad:

    # e "The left_gutter and right_gutter properties set a gutter on the left or right size of the bar. The gutter is space the bar can't be dragged into, that can be used for borders."
    e "Properti 'left_gutter' dan 'right_gutter' mengatur gutter (celah) pada sisi kiri atau kanan bar. Gutter adalah ruang di mana bar tidak dapat digeser masuk, yang bisa digunakan untuk area pembatas (border)."

# game/indepth_style.rpy:849
translate indonesian style_bar_fa41a83c:

    # e "The bar_vertical style property displays a vertically oriented bar. All of the other properties change names - left_bar becomes top_bar, while right_bar becomes bottom_bar."
    e "Properti gaya 'bar_vertical' menampilkan bar dengan orientasi vertikal. Semua properti lainnya akan berubah nama — 'left_bar' menjadi 'top_bar', sedangkan 'right_bar' menjadi 'bottom_bar'."

# game/indepth_style.rpy:854
translate indonesian style_bar_5d33c5dc:

    # e "Finally, there's one style we can't show here, and it's unscrollable. It controls what happens when a scrollbar can't be moved at all."
    e "Terakhir, ada satu gaya yang tidak bisa kami tunjukkan di sini, yaitu 'unscrollable'. Ini mengontrol apa yang terjadi saat scrollbar tidak dapat digerakkan sama sekali."

# game/indepth_style.rpy:856
translate indonesian style_bar_e8e32280:

    # e "By default, it's shown. But if unscrollable is 'insensitive', the bar becomes insensitive. If it's 'hide', the bar is hidden, but still takes up space."
    e "Secara default, bar akan tetap ditampilkan. Namun jika 'unscrollable' diatur ke 'insensitive', bar tersebut menjadi tidak aktif. Jika diatur ke 'hide', bar akan disembunyikan tetapi tetap memakan ruang."

# game/indepth_style.rpy:860
translate indonesian style_bar_f1292000:

    # e "That's it for the bar properties. By using them, a creator can customize bars, scrollbars, and sliders."
    e "Itu saja untuk properti bar. Dengan menggunakannya, seorang pembuat dapat menyesuaikan bar, scrollbar, dan slider."

# game/indepth_style.rpy:959
translate indonesian style_box_5fd535f4:

    # e "The hbox displayable is used to lay its children out horizontally. By default, there's no spacing between children, so they run together."
    e "Displayable 'hbox' digunakan untuk menyusun elemen anaknya (children) secara horizontal. Secara default, tidak ada jarak di antara anak-anaknya, sehingga mereka akan menempel satu sama lain."

# game/indepth_style.rpy:965
translate indonesian style_box_0111e5dc:

    # e "Similarly, the vbox displayable is used to lay its children out vertically. Both support style properties that control placement."
    e "Demikian pula, displayable 'vbox' digunakan untuk menyusun anak-anaknya secara vertikal. Keduanya mendukung properti gaya yang mengontrol penempatan."

# game/indepth_style.rpy:970
translate indonesian style_box_5a44717b:

    # e "To make the size of the box displayable obvious, I'll add a highlight to the box itself, and not the frame containing it."
    e "Untuk memperjelas ukuran dari displayable box tersebut, saya akan menambahkan sorotan (highlight) pada box itu sendiri, bukan pada frame yang menampungnya."

# game/indepth_style.rpy:978
translate indonesian style_box_239e7a8f:

    # e "Boxes support the xfill and yfill style properties. These properties make a box expand to fill the available space, rather than the space of the largest child."
    e "Box mendukung properti gaya 'xfill' dan 'yfill'. Properti ini membuat box melebar untuk mengisi ruang yang tersedia, alih-alih hanya mengikuti ukuran anak terbesarnya."

# game/indepth_style.rpy:988
translate indonesian style_box_e513c946:

    # e "The spacing style property takes a value in pixels, and adds that much spacing between each child of the box."
    e "Properti gaya 'spacing' menerima nilai dalam piksel, dan menambahkan jarak sebesar itu di antara setiap anak di dalam box."

# game/indepth_style.rpy:998
translate indonesian style_box_6ae4f94d:

    # e "The first_spacing style property is similar, but it only adds space between the first and second children. This is useful when the first child is a title that needs different spacing."
    e "Properti gaya 'first_spacing' serupa, tetapi hanya menambahkan ruang di antara anak pertama dan kedua. Ini berguna ketika anak pertama adalah judul yang membutuhkan spasi berbeda."

# game/indepth_style.rpy:1008
translate indonesian style_box_0c518d9f:

    # e "The box_reverse style property reverses the order of entries in the box."
    e "Properti gaya 'box_reverse' membalikkan urutan entri di dalam box."

# game/indepth_style.rpy:1021
translate indonesian style_box_f73c1422:

    # e "We'll switch back to a horizontal box for our next example."
    e "Kita akan beralih kembali ke box horizontal untuk contoh berikutnya."

# game/indepth_style.rpy:1031
translate indonesian style_box_285592bb:

    # e "The box_wrap style property fills the box with children until it's full, then starts again on the next line."
    e "Properti gaya 'box_wrap' mengisi box dengan elemen anak sampai penuh, lalu mulai lagi pada baris berikutnya."

# game/indepth_style.rpy:1044
translate indonesian style_box_a7637552:

    # e "Grids bring with them two more style properties. The xspacing and yspacing properties control spacing in the horizontal and vertical directions, respectively."
    e "Grid membawa dua properti gaya lagi. Properti 'xspacing' dan 'yspacing' masing-masing mengontrol spasi dalam arah horizontal dan vertikal."

# game/indepth_style.rpy:1051
translate indonesian style_box_4006f74b:

    # e "Lastly, we have the fixed layout. The fixed layout usually expands to fill all space, and shows its children from back to front."
    e "Terakhir, kita memiliki layout 'fixed'. Layout fixed biasanya melebar untuk mengisi semua ruang, dan menampilkan elemen anaknya dari belakang ke depan."

# game/indepth_style.rpy:1053
translate indonesian style_box_4a2866f0:

    # e "But of course, we have some style properties that can change that."
    e "Namun tentu saja, kita memiliki beberapa properti gaya yang dapat mengubah hal itu."

# game/indepth_style.rpy:1062
translate indonesian style_box_66e042c4:

    # e "When the xfit style property is True, the fixed lays out all its children as if it was full size, and then shrinks in width to fit them. The yfit style works the same way, but in height."
    e "Ketika properti gaya 'xfit' bernilai True, layout fixed menyusun semua anaknya seolah-olah dalam ukuran penuh, lalu mengecil lebarnya agar pas dengan mereka. Properti 'yfit' bekerja dengan cara yang sama, tetapi untuk tinggi."

# game/indepth_style.rpy:1070
translate indonesian style_box_6a593b10:

    # e "The order_reverse style property changes the order in which the children are shown. Instead of back-to-front, they're displayed front-to-back."
    e "Properti gaya 'order_reverse' mengubah urutan tampilan elemen anak. Alih-alih dari belakang-ke-depan, mereka ditampilkan dari depan-ke-belakang."

# game/indepth_style.rpy:1082
translate indonesian style_inspector_21bc0709:

    # e "Sometimes it's hard to figure out what style is being used for a particular displayable. The displayable inspector can help with that."
    e "Terkadang sulit untuk mengetahui gaya mana yang digunakan untuk displayable tertentu. Inspektur displayable dapat membantu dalam hal itu."

# game/indepth_style.rpy:1084
translate indonesian style_inspector_243c50f0:

    # e "To use it, place the mouse over a portion of the Ren'Py user interface, and hit shift+I. That's I for inspector."
    e "Untuk menggunakannya, arahkan mouse ke bagian antarmuka pengguna Ren'Py, lalu tekan Shift+I. Itu I untuk 'inspector'."

# game/indepth_style.rpy:1086
translate indonesian style_inspector_bcbdc396:

    # e "Ren'Py will pop up a list of displayables the mouse is over. Next to each is the name of the style that displayable uses."
    e "Ren'Py akan memunculkan daftar displayable yang ada di bawah kursor mouse. Di samping masing-masing adalah nama gaya yang digunakan displayable tersebut."

# game/indepth_style.rpy:1088
translate indonesian style_inspector_d981e5c8:

    # e "You can click on the name of the style to see where it gets its properties from."
    e "Anda dapat mengklik nama gaya tersebut untuk melihat dari mana ia mendapatkan properti-propertinya."

# game/indepth_style.rpy:1090
translate indonesian style_inspector_ef46b86d:

    # e "By default, the inspector only shows interface elements like screens, and not images. Type shift+alt+I if you'd like to see images as well."
    e "Secara default, inspektur hanya menunjukkan elemen antarmuka seperti screen (layar), dan bukan gambar. Tekan Shift+Alt+I jika Anda ingin melihat gambar juga."

# game/indepth_style.rpy:1092
translate indonesian style_inspector_b59c6b69:

    # e "You can try the inspector right now, by hovering this text and hitting shift+I."
    e "Anda dapat mencoba inspektur tersebut sekarang juga dengan mengarahkan kursor ke teks ini dan menekan Shift+I."
    
translate indonesian strings:

    # game/indepth_style.rpy:20
    old "Button 1"
    new "Tombol 1"

    # game/indepth_style.rpy:22
    old "Button 2"
    new "Tombol 2"

    # game/indepth_style.rpy:66
    old "Style basics."
    new "Dasar-dasar gaya (style)."

    # game/indepth_style.rpy:66
    old "General style properties."
    new "Properti gaya umum."

    # game/indepth_style.rpy:66
    old "Text style properties."
    new "Properti gaya teks."

    # game/indepth_style.rpy:66
    old "Window and Button style properties."
    new "Properti gaya Jendela (Window) dan Tombol (Button)."

    # game/indepth_style.rpy:66
    old "Bar style properties."
    new "Properti gaya Bar."

    # game/indepth_style.rpy:66
    old "Box, Grid, and Fixed style properties."
    new "Properti gaya Box, Grid, dan Fixed."

    # game/indepth_style.rpy:66
    old "The Displayable Inspector."
    new "Inspektur Displayable."

    # game/indepth_style.rpy:66
    old "That's all I want to know."
    new "Itu saja yang ingin saya ketahui."

    # game/indepth_style.rpy:112
    old "This text is colored green."
    new "Teks ini berwarna hijau."

    # game/indepth_style.rpy:126
    old "Danger"
    new "Bahaya"

    # game/indepth_style.rpy:142
    old "This text is colored red."
    new "Teks ini berwarna merah."

    # game/indepth_style.rpy:170
    old "This text is colored blue."
    new "Teks ini berwarna biru."

    # game/indepth_style.rpy:248
    old "Orbiting Earth in the spaceship, I saw how beautiful our planet is.\n–Yuri Gagarin"
    new "Berorbit mengelilingi Bumi dalam pesawat ruang angkasa, saya melihat betapa indahnya planet kita.\n–Yuri Gagarin"

    # game/indepth_style.rpy:303
    old "\"Orbiting Earth in the spaceship, I saw how beautiful our planet is.\" Said by Yuri Gagarin."
    new "\"Berorbit mengelilingi Bumi dalam pesawat ruang angkasa, saya melihat betapa indahnya planet kita.\" Diucapkan oleh Yuri Gagarin."

    # game/indepth_style.rpy:326
    old "Vertical"
    new "Vertikal"

    # game/indepth_style.rpy:329
    old "Far better it is to dare mighty things, to win glorious triumphs, even though checkered by failure, than to rank with those poor spirits who neither enjoy nor suffer much, because they live in the gray twilight that knows not victory nor defeat.\n\n–Theodore Roosevelt"
    new "Jauh lebih baik berani melakukan hal-hal besar, untuk memenangkan kemenangan yang mulia, meskipun diwarnai oleh kegagalan, daripada sejajar dengan jiwa-jiwa malang yang tidak banyak menikmati maupun menderita, karena mereka hidup di senja kelabu yang tidak mengenal kemenangan maupun kekalahan.\n\n–Theodore Roosevelt"

    # game/indepth_style.rpy:561
    old "Top Choice"
    new "Pilihan Atas"

    # game/indepth_style.rpy:566
    old "Bottom Choice"
    new "Pilihan Bawah"

    # game/indepth_style.rpy:877
    old "First Child"
    new "Anak Pertama (First Child)"

    # game/indepth_style.rpy:878
    old "Second Child"
    new "Anak Kedua (Second Child)"

    # game/indepth_style.rpy:879
    old "Third Child"
    new "Anak Ketiga (Third Child)"

    # game/indepth_style.rpy:882
    old "Fourth Child"
    new "Anak Keempat (Fourth Child)"

    # game/indepth_style.rpy:883
    old "Fifth Child"
    new "Anak Kelima (Fifth Child)"

    # game/indepth_style.rpy:884
    old "Sixth Child"
    new "Anak Keenam (Sixth Child)"

