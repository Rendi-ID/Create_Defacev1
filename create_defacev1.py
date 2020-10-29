#coding: utf-8
import os,sys,time
# mengetik otomatis speed
def sp(a):
  for e in a + '\n':
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.001)
# mengetik otomatis slow
def sl(a):
  for e in a + '\n':
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.05)
# version python
if sys.version_info.major < 3:
  sl("Tools ini menggunakan python3");time.sleep(1)
  sl("Ketik: python3 create_script.py");time.sleep(1);exit()

# clear
clear = lambda : os.system('clear')
# menu
def menu():
  clear()
  sp("\033[1;92m+\033[1;91m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[1;92m+")
  sp(" \033[1;90m{\033[1;92m•\033[1;90m} \033[1;93mAuthor     \033[1;91m: \033[1;95mRandiansyah")
  sp(" \033[1;90m{\033[1;92m•\033[1;90m} \033[1;93mFacebook   \033[1;91m: \033[1;95mRendi Kun")
  sp(" \033[1;90m{\033[1;92m•\033[1;90m} \033[1;93mYoutube    \033[1;91m: \033[1;95mRendi Noober")
  sp(" \033[1;90m{\033[1;92m•\033[1;90m} \033[1;93mGithub     \033[1;91m: \033[4;92mhttps://github.com/Rendi-ID\033[1;0m")
  sp(" \033[1;90m{\033[1;92m•\033[1;90m} \033[1;93mSupport by \033[1;91m: \033[1;95mJempol")
  sp(" \033[1;90m{\033[1;92m•\033[1;90m} \033[1;93mVersion    \033[1;91m: \033[1;95m1.0")
  sp(" \033[1;90m{\033[1;92m•\033[1;90m} \033[1;93mThanks To  \033[1;91m: \033[1;97mALLAH\033[1;95m, \033[1;96mMAMA\033[1;95m, \033[1;96mABAH")
  sp("\033[1;92m+\033[1;91m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[1;92m+")
  sp(" \033[1;90m{\033[1;96m01\033[1;90m} \033[1;93mScript Deface 1")
  sp(" \033[1;90m{\033[1;96m02\033[1;90m} \033[1;93mScript Deface 2")
  sp(" \033[1;90m{\033[1;96m03\033[1;90m} \033[1;93mScript Deface 3")
  sp(" \033[1;90m{\033[1;96m04\033[1;90m} \033[1;93mScript Deface 4")
  sp(" \033[1;90m{\033[1;96m05\033[1;90m} \033[1;93mScript Deface 5")
  sp("\033[1;92m+\033[1;91m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[1;92m+")
  pil = input(" \033[1;90m{\033[1;96m+\033[1;90m} \033[1;97mPilih Menu \033[1;90m~\033[1;91m•\033[1;92m>\033[1;96m ")
  sp("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
  if pil == "1" or pil == "01":
    judul = input(" {+} Judul : ")
    hacked = input(" {+} Hacked by (NICKNAME): ")
    pesan_1 = input(" {+} Pesan 1 : ")
    pesan_2 = input(" {+} Pesan 2 : ")
    pesan_3 = input(" {+} Pesan 3 : ")
    sp("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    ubah1 = judul1.replace("JUDUL",str(judul))
    ubah2 = hacked1.replace("NICKNAME",str(hacked))
    ubah3 = pesan11.replace("PESAN1",str(pesan_1))
    ubah4 = pesan21.replace("PESAN2",str(pesan_2))
    ubah5 = pesan31.replace("PESAN3",str(pesan_1))
    os.system('print "'+ubah1+'" > DEFACE_1.html;print "'+ubah2+'" >> DEFACE_1.html;print "'+ubah3+'" >> DEFACE_1.html;print "'+ubah4+'" >> DEFACE_1.html;print "'+ubah5+'" >> DEFACE_1.html;')
    print("Success create | File save DEFACE_1.html")
  elif pil == "2" or pil == "02":
    judul = input(" {+} Judul : ")
    halaman = input(" {+} Halaman meyatakan : ")
    background = input(" {+} Warna background : ")
    hacked = input(" {+} Hacked by (NICKNAME) : ")
    gambar = input(" {+} Link gambar : ")
    pesan_1 = input(" {+} Pesan 1 : ")
    pesan_2 = input(" {+} Pesan 2 : ")
    thanks = input(" {+} Thanks to : ")
    sp("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    ubah1 = judul2.replace("JUDUL21",str(judul))
    ubah2 = menyatakan2.replace("MEYATAKAN21", str(halaman))
    ubah3 = background2.replace("BACKGROUND21",str(background))
    ubah4 = hacked2.replace("NICKNAME21",str(hacked))
    ubah5 = gambar2.replace("LINK_GAMBAR21",str(gambar))
    ubah6 = pesan21.replace("PESAN1",str(pesan_1))
    ubah7 = pesan22.replace("PESAN2",str(pesan_2))
    os.system("touch DEFACE_2.html")
    os.system('print "'+ubah1+'" > DEFACE_2.html;print "'+ubah2+'" >> DEFACE_2.html;print "'+ubah3+'" >> DEFACE_2.html;print "'+ubah4+'" >> DEFACE_2.html;print "'+ubah5+'" >> DEFACE_2.html;print "'+ubah6+'" >> DEFACE_2.html;print "'+ubah7+'" >> DEFACE_2.html')
    print(" {√} Success create | File save as DEFACE_2.html")
  elif pil == "3" or pil == "03":
    judul = input(" {+} Judul : ")
    gambar = input(" {+} Link Gambar : ")
    hacked = input(" {+} Hacked by (NICKNAME) : ")
    pesan = input(" {+} Pesan : ")
    thanks = input(" {+} Thanks to : ")
    musik = input(" {+} Link musik : ")
    sp("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    ubah1 = judul3.replace("JUDUL",str(judul))
    ubah2 = gambar3.replace("GAMBAR",str(gambar))
    ubah3 = hacked3.replace("NICKNAME",str(hacked))
    ubah4 = pesan3.replace("PESAN",str(pesan))
    ubah5 = thanks3.replace("THANKS",str(thanks))
    ubah6 = lagu3.replace("MUSIK",str(musik))
    os.system("touch DEFACE_3.html")
    os.system('print "'+ubah1+'" >> DEFACE_3.html;print "'+ubah2+'" >> DEFACE_3.html;print "'+ubah3+'" >> DEFACE_3.html;print "'+ubah4+'" >> DEFACE_3.html;print "'+ubah5+'" >> DEFACE_3.html;print "'+ubah6+'" >> DEFACE_3.html')
    print(" {√} Success create | File save as DEFACE_3.html")
  elif pil == "4" or pil == "04":
    judul = input(" {+} Judul : ")
    gambarsh = input(" {+} Link gambar (shortcut) : ")
    textsh = input(" {+} Text (shortcur) : ")
    teamsh = input(" {+} Team (shortcut) : ")
    hacked = input(" {+} Hacked by (NICKNAME) : ")
    lagu_1 = input(" {+} Link Lagu 1 : ")
    team = input(" {+} Team : ")
    pesan = input(" {+} Pesan : ")
    lagu_2 = input(" {+} Link Lagu 2 : ")
    thanks = input(" {+} Thanks : ")
    lagu_3 = input(" {+} Link Lagu 3 : ")
    sp("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    ubah1 = author4.replace("JUDUL",str(judul))
    ubah2 = gambar_sh.replace("GAMBAR_CONTENT",str(gambarsh))
    ubah3 = text_sh.replace("TEXT_CONTENT",str(textsh))
    ubah4 = team_sh.replace("TEAM_CONTENT",str(teamsh))
    ubah5 = hacked4.replace("NICKNAME",str(hacked))
    ubah6 = lagu41.replace("MUSIK",str(lagu_1))
    ubah7 = team4.replace("TEAM",str(team))
    ubah8 = pesan4.replace("PESAN",str(pesan))
    ubah9 = lagu42.replace("MUSIK",str(lagu_2))
    ubah10 = thanks4.replace("THANKS",str(thanks))
    ubah11 = lagu43.replace("MUSIK",str(lagu_3))
    os.system("touch DEFACE_4.html")
    os.system('print "'+ubah1+'" > DEFACE_4.html;print "'+ubah2+'" >> DEFACE_4.html;print "'+ubah3+'" >> DEFACE_4.html;print "'+ubah4+'" >> DEFACE_4.html;print "'+ubah5+'" >> DEFACE_4.html;print "'+ubah6+'" >> DEFACE_4.html;print "'+ubah7+'" >> DEFACE_4.html;print "'+ubah8+'" >> DEFACE_4.html;print "'+ubah9+'" >> DEFACE_4.html;print "'+ubah10+'" >> DEFACE_4.html;print "'+ubah11+'" >> DEFACE_4.html')
    print(" {√} Success create | File save as DEFACE_4.html")
  elif pil == "5" or pil == "05":
    judulsh = input(" {+} Judul Shortcut : ")
    textsh = input(" {+} Text Shortcut : ")
    gambarcn = input(" {+} Link Gambar Content : ")
    gambarsh = input(" {+} Link Gambar Shortcut : ")
    judul = input(" {+} Judul : ")
    author = input(" {+} Author : ")
    copyright = input(" {+} Copyright : ")
    halaman = input(" {+} Halaman Menyatakan : ")
    gambar = input(" {+} Link Gambar : ")
    hacked = input(" {+} Hacked By (NICKNAME) : ")
    team = input(" {+} Team : ")
    pesan = input(" {+} Pesan : ")
    thanks = input(" {+} Thanks To : ")
    lagu = input(" {+} Link Musik : ")
    sp("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    ubah1 = judulsh5.replace("JUDUL_SH",str(judulsh))
    ubah2 = textsh5.replace("TEXT_SH",str(textsh))
    ubah3 = gambarcn5.replace("GAMBAR_CONTENT",str(gambarcn))
    ubah4 = gambarsh5.replace("GAMBAR_SHORTCUT",str(gambarsh))
    ubah5 = judul5.replace("JUDUL",str(judul))
    ubah6 = author5.replace("AUTHOR",str(author))
    ubah7 = copyright5.replace("COPYRIGHT",str(copyright))
    ubah8 = halaman5.replace("HALAMAN_MENYATAKAN",str(halaman))
    ubah9 = gambar5.replace("GAMBAR",str(gambar))
    ubah10 = hacked5.replace("NICKNAME",str(hacked))
    ubah11 = team5.replace("TEAM",str(team))
    ubah12 = pesan5.replace("PESAN",str(pesan))
    ubah13 = thanks5.replace("THANKS",str(thanks))
    ubah14 = lagu5.replace("MUSIK",str(lagu))
    os.system("touch DEFACE_5.html")
    os.system('print "'+ubah1+'" >> DEFACE_5.html;print "'+ubah2+'" >> DEFACE_5.html;print "'+ubah3+'" >> DEFACE_5.html;print "'+ubah4+'" >> DEFACE_5.html;print "'+ubah5+'" >> DEFACE_5.html;print "'+ubah6+'">> DEFACE_5.html;print "'+ubah7+'" >> DEFACE_5.html;print "'+ubah8+'" >> DEFACE_5.html;print "'+ubah9+'" >> DEFACE_5.html;print "'+ubah10+'" >> DEFACE_5.html;print "'+ubah11+'" >> DEFACE_5.html;print "'+ubah12+'" >> DEFACE_5.html;print "'+ubah13+'" >> DEFACE_5.html;print "'+ubah14+'" >> DEFACE_5.html')
    print(" {√} Success create | File save as DEFACE_5.html")
# (1)
judul1 = """<!DOCTYPE html>
<html lang='en'>

<style>
@import url('https://fonts.googleapis.com/css?family=Amatic+SC:400,700');
body {
  font-family: 'Amatic SC', sans-serif;
  font-size: 100px;
}
.test {
  -webkit-animation: squiggly-anim 0.34s linear infinite;
          animation: squiggly-anim 0.34s linear infinite;
}
body {
  line-height: 100vh;
  background: #111;
  color: #fff;
}
.test {
  display: inline-block;
  vertical-align: middle;
  width: 100%;
  outline: none;
  text-align: center;
  line-height: 1;
}
.small {
  font-size: 0.5em;
}
.smaller {
  font-size: 0.4em;
}
p {
  margin: 0;
}
@-webkit-keyframes squiggly-anim {
  0% {
    -webkit-filter: url('#squiggly-0');
            filter: url('#squiggly-0');
  }
  25% {
    -webkit-filter: url('#squiggly-1');
            filter: url('#squiggly-1') ;
  }
  50% {
    -webkit-filter: url('#squiggly-2');
            filter: url('#squiggly-2');
  }
  75% {
    -webkit-filter: url('#squiggly-3');
            filter: url('#squiggly-3');
  }
  100% {
    -webkit-filter: url('#squiggly-4');
            filter: url('#squiggly-4');
  }
}
@keyframes squiggly-anim {
  0% {
    -webkit-filter: url('#squiggly-0');
            filter: url('#squiggly-0');
  }
  25% {
    -webkit-filter: url('#squiggly-1');
            filter: url('#squiggly-1');
  }
  50% {
    -webkit-filter: url('#squiggly-2');
            filter: url('#squiggly-2');
  }
  75% {
    -webkit-filter: url('#squiggly-3');
            filter: url('#squiggly-3');
  }
  100% {
    -webkit-filter: url(/#squiggly-4');
            filter: url('#squiggly-4');
  }
}
</style>

<head>
  <meta charset='UTF-8'>
  <title>JUDUL</title>
  
    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css'>

  
      <link rel='stylesheet' href='css/style.css'>

  
</head>

<body>

  <div class='test' contenteditable>"""
hacked1 = """  Hacked? by NICKNAME"""
pesan11 = """  <p class='small'>– PESAN1 – <p/>"""
pesan21 = """  <p class='small'>[+] PESAN2 [+]</p>"""
pesan31 = """  <p class='smaller'>(PESAN3)</p>
</div>

<svg xmlns='http://www.w3.org/2000/svg' version='1.1'>
  <defs>

    
    <filter id='squiggly-0'>
      <feTurbulence id='turbulence' baseFrequency='0.02' numOctaves='3' result='noise' seed='0'/>
      <feDisplacementMap id='displacement' in='SourceGraphic' in2='noise' scale='6'/>
    </filter>
    <filter id='squiggly-1'>
      <feTurbulence id='turbulence' baseFrequency='0.02' numOctaves='3' result='noise' seed='1'/>
<feDisplacementMap in='SourceGraphic' in2='noise' scale='8'/>
    </filter>
    
    <filter id='squiggly-2'>
      <feTurbulence id='turbulence' baseFrequency='0.02' numOctaves='3' result='noise' seed='2'/>
<feDisplacementMap in='SourceGraphic' in2='noise' scale='6'/>
    </filter>
    <filter id='squiggly-3'>
      <feTurbulence id='turbulence' baseFrequency='0.02' numOctaves='3' result='noise' seed='3'/>
<feDisplacementMap in='SourceGraphic' in2='noise' scale='8'/>
    </filter>
    
    <filter id='squiggly-4'>
      <feTurbulence id='turbulence' baseFrequency='0.02' numOctaves='3' result='noise' seed='4'/>
<feDisplacementMap in='SourceGraphic'  in2='noise' scale='6' />
    </filter>
  </defs> 
</svg>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

  

</body>

</html>"""

# (2)
judul2 = """<html>
<head>
<meta charset='UTF-8' />
<title>JUDUL21</title>
<font class='hk2' style='text-shadow: 1px -1px 8px;' face='tahoma'>
<font color='green'>
<font size='5'>
<link rel='stylesheet' id'skebggallery-css' href='http://shop4brides.ru/wp-content/themes/irex-lite/SketchBoard/functions/sketch-background-gallery/inc/front/css/skebggallery.css?ver=4.0.1' type='text/css' media='all' />
			  <script type='text/javascript' src='http://shop4brides.ru/wp-includes/js/jquery/jquery.js?ver=1.11.1'></script>
              <script type='text/javascript' src='http://shop4brides.ru/wp-content/themes/irex-lite/SketchBoard/functions/sketch-background-gallery/inc/front/js/skebggallery.js?ver=4.0.1'></script> 
			  <style> .error { text-align: center; font-family: 'Gilda Display', serif; -webkit-animation: noise-3 1s linear infinite; animation: noise-3 1s linear infinite; overflow: default; } .info { text-align: center; width: 200px; height: 60px; margin: auto; position: absolute; top: 280px; bottom: 0; left: 20px; right: 0; -webkit-animation: noise-3 1s linear infinite; animation: noise-3 1s linear infinite; } .info:after { content: 'OWNED'; font-family: OCR-A; font-size: 100px; text-align: center; width: 800px; margin: auto; position: absolute; top: 20px; bottom: 0; left: 40px; right: 0; opacity: 0; color: white; -webkit-animation: noise-1 .2s linear infinite; animation: noise-1 .2s linear infinite; } @-webkit-keyframes noise-1 { 0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;} 10% {opacity: .1;} 50% {opacity: .5; left: -6px;} 80% {opacity: .3;} 100% {opacity: .6; left: 2px;} } @keyframes noise-1 { 0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;} 10% {opacity: .1;} 50% {opacity: .5; left: -6px;} 80% {opacity: .3;} 100% {opacity: .6; left: 2px;} } @-webkit-keyframes noise-2 { 0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;} 10% {opacity: .1;} 50% {opacity: .5; left: 6px;} 80% {opacity: .3;} 100% {opacity: .6; left: -2px;} } @keyframes noise-2 { 0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;} 10% {opacity: .1;} 50% {opacity: .5; left: 6px;} 80% {opacity: .3;} 100% {opacity: .6; left: -2px;} } @-webkit-keyframes noise { 0%, 3%, 5%, 42%, 44%, 100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);} 4.3% {opacity: 1; -webkit-transform: scaleY(1.7); transform: scaleY(1.7);} 43% {opacity: 1; -webkit-transform: scaleX(1.5); transform: scaleX(1.5);} } @keyframes noise { 0%, 3%, 5%, 42%, 44%, 100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);} 4.3% {opacity: 1; -webkit-transform: scaleY(1.7); transform: scaleY(1.7);} 43% {opacity: 1; -webkit-transform: scaleX(1.5); transform: scaleX(1.5);} } @-webkit-keyframes noise-3 { 0%,3%,5%,42%,44%,100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);} 4.3% {opacity: 1; -webkit-transform: scaleY(4); transform: scaleY(4);} 43% {opacity: 1; -webkit-transform: scaleX(10) rotate(60deg); transform: scaleX(10) rotate (60deg);} } @keyframes noise-3 { 0%,3%,5%,42%,44%,100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);} 4.3% {opacity: 1; -webkit-transform: scaleY(4); transform: scaleY(4);} 43% {opacity: 1; -webkit-transform: scaleX(10) rotate(60deg); transform: scaleX(10) rotate (60deg);} } .wrap { top: 30%; left: 25%; height: 200px; margin-top: -100px; position: absolute; } code { color: white; } span.blue { color: #48beef; } span.comment { color: #7f8c8d; } span.orange { color: #f39c12; } span.green { color: #33cc33; } .viewFull { font-family:OCR-A; color:orange; text-decoration:; } 	 } @media only screen and (min-height: 500px) { .viewFull{ display:none; 	 	} } 	</style> <center> <style> img { filter:alpha(opacity=70); -moz-opacity:0.7; opacity:0.7; } img:hover { filter:alpha(opacity=100); -moz-opacity:.0; opacity:1.0; } </style>
			   <link href='https://fonts.googleapis.com/css?family=Chicle|Yatra+One' rel='stylesheet' type='text/css' >
<script>"""
menyatakan2 = """alert('MENYATAKAN21');
</script>"""
background2 = """<body bgcolor=BACKGROUND21>


<script type='text/javascript' src='http://htmlfreecodes.com/codes/rain.js'></script><br><div class='error'>
<font color='green'>"""
hacked2 = """<h5 align='center' face='Chicle'><font color='red'>Hacked by?  NICKNAME21</h5>
<center>
</font>"""
gambar2 = """<img src='LINK_GAMBAR21' width='150px'>
<font color=green>
<br>"""
pesan21 = """<b><font face='courier new' ><font size='3'>PESAN1"""
pesan22 = """<h5><font color='yellow'>PESAN2</font>
<marquee behavior='scroll' direction='left' scrollamount='90' scrolldelay='40' width='100%'>
<font color='green'>___________________________________________________________</font></marquee>"""
thanks2 = """<div style='text-shadow: 0px 0px 10px green;'><span style='color: white;'><font face='transformers'><b>Thanks To : R<marquee scrollamount='5' direction='left' width='50%'><span style='color: red;'> <span style='color: red;'>THANKS21<span style='color: red;'></b></marquee></font></div><script type='text/rocketscript'>/*<![CDATA[*/new TypingText(document.getElementById('message'), 90, function(i){ var ar= new Array('_', ' ', '_', ' '); return '' +ar[i.length % ar.length]; });//Type out examples:TypingText.runAll();/*]]>*/</script>
<marquee behavior='scroll' direction='right' scrollamount='90' scrolldelay='40' width='100%'>
<font color='green'></font></marquee>
</body>
</html>	"""

# (3)
judul3 = """<!DOCTYPE html>
<html>
<head>
s
	<title>JUDUL</title>
<meta name='description' content='[ Your Site Not Safe]'> <meta name='keywords' content='[ERROR THE SYSTEM]'>

	<link href='https://fonts.googleapis.com/css2?family=Comic+Neue&display=swap' rel='stylesheet'>

	<link href='https://fonts.googleapis.com/css2?family=Metal+Mania&display=swap' rel='stylesheet'>

	<link href='https://fonts.googleapis.com/css2?family=Indie+Flower&family=Metal+Mania&display=swap' rel='stylesheet'>

	<link href='https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap' rel='stylesheet'> 

	<script language=JavaScript> message='White Cyber Illusion';function clickIE4(){if (event.button==2){alert(message);return false;}}function clickNS4(e){if (document.layers||document.getElementById&&!document.all){if (e.which==2||e.which==3){alert(message);return false;}}}if (document.layers){document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS4;}else if (document.all&&!document.getElementById){document.onmousedown=clickIE4;}document.oncontextmenu=new Function('alert(message);return false')// --></script> 

	<style type='text/css'>

		body{

			background:url(https://f.top4top.io/p_1577h5txv0.gif);
		}

		.shining {

		font-size: 25px;

		font-family: Gloria Hallelujah;

		  text-align:center;

		  text-transform:uppercase;

		  letter-spacing:5px;

		  background:linear-gradient(90deg, #000,#f5f5f5,#000);

		  -webkit-background-clip:text;

		  -webkit-text-fill-color:transparent;

		  background-repeat:no-repeat;

		  background-size:80%;

		  position:relative;

		  animation:shine 6s ease-in-out infinite;

}

.shining h1{

		font-size: 50px;

}

@keyframes shine {

  from {

    background-position-x:-500%;

  }

  to {

    background-position-x:500%;

  }

}

p{

	font-size: 15px;

	font-family: Indie Flower;

	color: white;

}

	</style>

</head>

<body>

	<center>

		<br>

		<br>

		<br>

		<br>

		<br>

		<br>

		<br>
"""
gambar3 = """	<img src='GAMBAR'width='450' height='400'>

	

	<div class='shining'>
"""
hacked3 = """		<h1 color='red'>Hacked by? NICKNAME</h1>

	</div>

<!--
.ahgcrewstyle {
        color: #F00;
}
/.ahg {
        color: #0F0;
}
#message font strong {
        font-family: Tahoma, Geneva, sans-serif;
        font-size: 18px;
}
.gre {
        color: #9F3;
        font-size: 36px;
}
#message font {
        font-size: 16px;
}
-->
</style>
</head><body alink='gray' bgcolor='black' vlink='gray' link='gray' text='gray'>
<p></p><center>
<center></center>
<script type='text/javascript'>
TypingText = function(element, interval, cursor, finishedCallback) {
  if((typeof document.getElementById == 'undefined') || (typeof element.innerHTML == 'undefined')) {
    this.running = true;
    return;
  }
  this.element = element;
  this.finishedCallback = (finishedCallback ? finishedCallback : function() { return; });
  this.interval = (typeof interval == 'undefined' ? 100 : interval);
  this.origText = this.element.innerHTML;
  this.unparsedOrigText = this.origText;
  this.cursor = (cursor ? cursor : '');
  this.currentText = '';
  this.currentChar = 0;
  this.element.typingText = this;
  if(this.element.id == '') this.element.id = 'typingtext' + TypingText.currentIndex++;
  TypingText.all.push(this);
  this.running = false;
  this.inTag = false;
  this.tagBuffer = '';
  this.inHTMLEntity = false;
  this.HTMLEntityBuffer = '';
}
TypingText.all = new Array();
TypingText.currentIndex = 0;
TypingText.runAll = function() {
  for(var i = 0; i < TypingText.all.length; i++) TypingText.all[i].run();
}
TypingText.prototype.run = function() {
 if(this.running) return;
 if(typeof this.origText == 'undefined') {
   setTimeout('document.getElementById('' + this.element.id + '').typingText.run()', this.interval);
   return;
 }
 if(this.currentText == '') this.element.innerHTML = '';
 if(this.currentChar < this.origText.length) {
   if(this.origText.charAt(this.currentChar) == '<' && !this.inTag) {
     this.tagBuffer = '<';
     this.inTag = true;
     this.currentChar++;
     this.run();
     return;
   } else if(this.origText.charAt(this.currentChar) == '>' && this.inTag) {
     this.tagBuffer += '>';
      this.inTag = false;
      this.currentText += this.tagBuffer;
      this.currentChar++;
      this.run();
      return;
    } else if(this.inTag) {
      this.tagBuffer += this.origText.charAt(this.currentChar);
      this.currentChar++;
      this.run();
      return;
    } else if(this.origText.charAt(this.currentChar) == '&' && !this.inHTMLEntity) {
     this.HTMLEntityBuffer = '&';
      this.inHTMLEntity = true;
      this.currentChar++;
      this.run();
      return;
    } else if(this.origText.charAt(this.currentChar) == ';' && this.inHTMLEntity) {
     this.HTMLEntityBuffer += ';';
      this.inHTMLEntity = false;
      this.currentText += this.HTMLEntityBuffer;
      this.currentChar++;
      this.run();
      return;
    } else if(this.inHTMLEntity) {
      this.HTMLEntityBuffer += this.origText.charAt(this.currentChar);
      this.currentChar++;
      this.run();
      return;
    } else {
      this.currentText += this.origText.charAt(this.currentChar);
    }
    this.element.innerHTML = this.currentText;
    this.element.innerHTML += (this.currentChar < this.origText.length - 1 ? (typeof this.cursor == 'function' ? this.cursor(this.currentText) : this.cursor) : '');
   this.currentChar++;
   setTimeout('document.getElementById('' + this.element.id + '').typingText.run()', this.interval);
 } else {
        this.currentText = '';
        this.currentChar = 0;
       this.running = false;
       this.finishedCallback();
 }
}
</script>
<center>
  <b class='Gre'>From Newbie To Mastah</b>
  <br>
  <font>"""
pesan3 = """</font><p id='message'><font> <strong><br> PESAN <br>
 <br>
  </strong><br>
<br>
We Are  <span class='ahgcrewstyle'><strong><strong> Legion </strong></strong></span><strong> </strong> <br>
</font></p>
<p align='center'><em></em> <b><font size='10'><span class='ahgcrewstyle'></span></font></b></p>
<p><font><br></font></p>
 <br>
 <p align='center'><font color='red' size='5' face='Times New Roman'> </font><br><br><br><br><br><br></p>
<body>


	<br>"""
thanks3 = """       <marquee direction='right' ><font face='Courier' color='red' size='5'>[] THANKS []</font></marquee>

	<br>
	
	
"""
lagu3 = """	<iframe width='200' height='100' scrolling='no' frameborder='no' allow='autoplay' src='MUSIK'></iframe>

	</center>

</body>

</html>
<script>(function(d, s, id) {
 var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = '//connect.facebook.net/en_US/all.js#xfbml=1&appId=384191914936497';
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
<p align='center'><font size='+8' face='Times New Roman'><font color='green'><font color='white'>  <font color='red'> </font></font></font></font></p>
<script>alert{} PROGRAMER BY ./randiXploit{}</script>
<p align='center'> <img > </p>
  <script type='text/javascript'>
new TypingText(document.getElementById('message'), 50, function(i){ var ar = new Array('\\', '|', '/', '-'); return ' ' + ar[i.length % ar.length]; });
//Type out examples:
TypingText.runAll();
  </script>
</font></p>
<center></center>
<br>

</br>
</body></html>
<!-- aghaze larzeshe safhe-->
<meta http-equiv='Content-Language' content='en-us'>
<SCRIPT language=JavaScript>
<!-- Begin
function shake(n) {
if (parent.moveBy) {
for (i = 10; i > 0; i--) {
for (j = n; j > 0; j--) {
parent.moveBy(-i,0);
parent.moveBy(0,-i);
parent.moveBy(-i,0);
parent.moveBy(0,i);
parent.moveBy(i,0);
parent.moveBy(0,-i);
parent.moveBy(-i,0);
parent.moveBy(0,i);
parent.moveBy(i,0);
parent.moveBy(0,-i);
parent.moveBy(-i,0);
parent.moveBy(0,-i);
parent.moveBy(i,0);
parent.moveBy(0,i);
parent.moveBy(i,0);
parent.moveBy(0,i);
        }
     }
  }
}
//  End -->
<!--
shake(1);
//-->
</SCRIPT>
<!-- p align='center'><font size='7' color='#FF0000'>chi?</font></p> -->
<!--payan--></SCRIPT>
</body>
</html>
</body>
</html>
<P align=center></P>
<body bgcolor='#333366' background='' text='#FFFFFF' link='#0066CC' vlink='#999999' alink='#993300' style=''><style>
body {
    padding:0;
    margin:0;
    background-image:;
    background-repeat: no-repeat;
    background-position:top;
background-color: black;
color: white;
font: normal 110% courier;
margin-top: 5px;
margin-left: 5px;
padding: 0;
margin-right: 5px;
}
td{font-family: verdana; font-size: 20pt; color: green}
a{font-family: verdana; font-size: 30pt; color: silver}
</style>
<center><img src=''></center>
<style>
#navbar-iframe {
display: none;
<style>

</div>
<style>
.animasi {
  color: #EBE3AA;
  font-family:sans-serif;
  font-weight:lighter;
  font-size: 2em;
  white-space: nowrap;
  overflow: hidden;
  width: 30em;
  animation: keyframes 5s steps(500) infinite;
}

@keyframes keyframes{
 
  from{ width: 0px;}
 
}
</style>
 
<link href='http://fonts.googleapis.com/css?family=Bevan' rel='stylesheet' type='text/css'>
</head>
</body>
</DOCTYPE>

<div class='animasi'>"""

#(4)
author4 = """<html><head> <title>JUDUL</title>"""
gambar_sh = """<link rel='shortcut icon' href='GAMBAR_CONTENT'>
</head><body oncontextmenu='return false;' onkeydown='return false;' onmousedown='return false;' align='center' bgcolor='black'>
<meta charset='utf-8'>"""
text_sh = """<meta name='description' og:content='TEXT_CONTENT'>"""
team_sh = """<meta name='og:description' content='TEAM_CONTENT'>
<link href='https://fonts.googleapis.com/css?family=Kelly+Slab' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Allan|Chakra+-Petch|Iceland|Orbitron|Grenze' rel='stylesheet'> 
<style type='text/css'> body{ background: #0a0a0a; height: 100vh; width: 100%; margin: 0; padding: 12px; display: flex; flex-direction: column; justify-content: center; align-items: center; background: linear-gradient(rgba(20, 10, 10, 0.3), rgba(0, 0, 0, 0.3)), repeating-linear-gradient(0, transparent, transparent 4px, black 4px, black 2px), url('https://4.bp.blogspot.com/-5iJUcVAV5YI/Xuk0bn26UEI/AAAAAAAAAGc/PMy5WOn3nXYcqb9jf83s7Ap83HBiGmWhACK4BGAYYCw/s1024/20200616_144703.jpg'); background-size: cover; background-position: center; z-index: 1; } </style> 

<script type='text/javascript' src='https://cdn.rawgit.com/FicriPebriyana/efek/0a935a6c/efek%20salju.js'></script>
<style type='text/css'>
h3{-webkit-text-stroke-width: 0px; -webkit-text-stroke-color: white; }
.f{
  text-align: center;
  color: whitesmoke;
  animation: koclok 2s infinite alternate ease-in-out;
@keyframes koclok {
25%{
    text-shadow:0 0 5px #757575;
}
35%{
    text-shadow:0 0 20px whitesmoke;
}
  50% {
    text-shadow: 0 10 20px transparent;}
    
    60%{
        text-shadow:0 30 30px black;
    }
  }
  75%{
      text-shadow: 0 20 40px grey;
  }
  100%{
    text-shadow: 0 30px 50px black;
  }
}
}
</style>
<style type='text/css'>
.blink_text {
-webkit-animation-name: blinker;
-webkit-animation-duration: 2s;
-webkit-animation-timing-function: linear;
-webkit-animation-iteration-count: infinite;

-moz-animation-name: blinker;
-moz-animation-duration: 2s;
-moz-animation-timing-function: linear;
-moz-animation-iteration-count: infinite;

 animation-name: blinker;
 animation-duration: 2s;
 animation-timing-function: linear;
 animation-iteration-count: infinite;

 color: white;
}
@-moz-keyframes blinker { 
 0% { opacity: 5.0;
 }
 50% { opacity: 0.0;
 }
 100% { opacity: 5.0;
 }
 }
@-webkit-keyframes blinker { 
 0% { opacity: 5.0;
 }
 50% { opacity: 0.0;
 }
 100% { opacity: 5.0;
 }
 }
@keyframes blinker { 
 0% { opacity: 5.0;
 }
 50% { opacity: 0.0;
 }
 100% { opacity: 5.0;
 }
 }
 
 #copy {
   color: lime;
   font-weight: bold;
   font-family: Kelly Slab;
 }
 #copy a {
   color: white;
 }
 #copy a:hover {
   color: blue;
 }

body{
font-family: Kelly Slab;
background-color: black;
color:white;
}
#content tr:hover{
background-color: blue;
text-shadow:0px 0px 10px #fff;
}
#content .first{
background-color: #15CFF4;
}
table{
border: 1px #000000;
}
.s_tb{
border:1px silver;
}
a{
color:white;
font-size: 19px;
text-decoration:none;
}
a:hover{
color:green;
text-shadow:0px 0px 10px #ffffff;
}
input,select,textarea{
border: 2px #000000 solid;
-moz-border-radius: 5px;
-webkit-border-radius:5px;
border-radius:5px;
}
h2{
font-family:Kelly Slab;
font-size:25px;
color:white;
}
h3{
font-size:35px;
}
h4{
font-size:15px;
font-family:Kelly Slab;
color:white;
}
</style>

<style type='text/css'>
.lagu{
     background:transparent;
  border:2px solid silver;
  font-family:Share Tech Mono;
  color:white;
  font-size:18x;
  font-weight:bold;
  padding:3px 29px;
  text-decoration:none;
  text-shadow:0px 0px 20px #15CFF4;
  }
</style>
<script> function play(){ var audio = document.getElementById('lagu'); audio.play(); } function liat(){ document.getElementById('galiat').style.visibility='visible'; } 
</script>

<center>

<div class='stars'><div class='twinkling'>
<div class='flex-center position-ref full-height'> <div class='content'> 
<div class='text'>
<font color='white'> 
<p class='blink_text' style='font-size:70px;color: white;text-shadow: 0px 0px 0px #00ffff, 3px 3px 5px   #87CEEB;font-family:Kelly Slab;'>HACKED BY :"""
hacked4 = """<style='font-size:45px;color: orange;text-shadow: 0px 29px white , white;'>NICKNAME</style='font-size:45px;color:></p> """
lagu41 = """<button class='lagu' onclick='play();liat();'><font face='Kelly Slab' size='5' color='white'>MUSIC</font></button><audio id='lagu' src='MUSIK'></audio><br>  
<h1 class='f' style='font-family: 'Kelly Slab'; font-size: 30px; line-height:30px;padding: 3%; font-weight: 1000;'>"""
team4 = """TEAM </h1><p></p>"""
pesan4 = """<button class='lagu' onclick='play();liat();'><font face='Kelly Slab' size='5' color='white'>PESAN</font></button>"""
lagu42 = """<audio id='lagu' src='MUSIK'></audio><br>  
  
<br>"""
thanks4 = """<button class='lagu' <font size='4'><marquee width='600' <font color='white'>Thanks to: THANKS
</marquee></button></font></div></div></div></div></div></center><font color='white'> """
lagu43 = """<iframe width='0%' height='0' scrolling='no' frameborder='no' src='MUSIK'></iframe>  
<br>
</font></body></html>"""

# (5)
judulsh5 = """<html>
<head>
	<title>JUDUL_SH</title>"""
textsh5 = """        <meta property='og:description' content='TEXT_SH'/>"""
gambarcn5 = """        <meta property='og:image' content='GAMBAR_CONTENT'/>"""
gambarsh5 = """        <link rel='shortcut icon' href='GAMBAR_SHORTCUT'/>
</head>
<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml'>"""
judul5 = """<html><head><head><title>JUDUL</title>
	<meta charset='UTF-8'>"""
author5 = """        <meta name='Author' content='AUTHOR'/>"""
copyright5 = """        <meta name='copyright' content='COPYRIGHT'/>
<link href='http://fonts.googleapis.com/css?family=Megrim' rel='stylesheet' type='text/css'>   <link href='http://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet' type='text/css'>     <script src='http://e-mete.com/js/kdsnow.js'></script>  <style>    body{     background-image: url(index.html);     background-repeat: no-repeat;      background-attachment: fixed;      background-position: top;     background-color:#000000;     position: relative;     background-size:100% 100vh;          }    .logo {     width: 300px;     height: 300px;     margin: 0 auto;     margin-top: 50px;     -webkit-filter: drop-shadow(0px 0px 7px #0080FF);     filter: drop-shadow(0px 0px 7px #0080FF);    }    .logo:hover{     width: 300px;     height: 300px;     -webkit-filter: drop-shadow(0px 0px 10px #0080FF);     opacity:0.4;     filter:alpha(opacity=40);     transition: opacity .2s ease-out;     -moz-transition: opacity .2s ease-out;     -webkit-transition: opacity .2s ease-out;     -o-transition: opacity .2s ease-out;    }    .defacedby{     font-family: Megrim;     text-align: center;     color: black;     font-weight: bold;     font-size: 40px;   text-shadow: #0080FF 1px 2px 1px;        }    .glow {     font-family: Quicksand;     text-align: center;     color: grey;     font-style: bold;     font-size: 20px;    margin-top: 16px;    text-shadow: black 1px 2px 1px;        }    .greetings{     font-family: Quicksand;     text-align: center;     color: #ffffff;     font-size: 20px;     margin-top: 50px; text-shadow: black 1px 2px 1px;    }    </style>   
<body>"""
halaman5 = """<script> alert('HALAMAN_MENYATAKAN')</script>
<center>
<center>
<script type='text/javascript'>
//Define first typing example:
new TypingText(document.getElementById('example1'));
//Define second typing example (use 'slashing' cursor at the end):
new TypingText(document.getElementById('example2'), 80, function(i){
var ar = new Array('_',' ','_','_'); return ' ' + ar[i.length %
ar.length]; });
//Type out examples:
TypingText.runAll();
</script>
<style type='text/css'>body {cursor:url(''),default}</style>
<div align='center'><table border='0' width='100%'><tr><td>
<font size='200'>
<b><font face='times'><b><center><SCRIPT>
farbbibliothek = new Array();
farbbibliothek[0] = new Array('#FF0000','#FF1100','#FF2200','#FF3300','#FF4400','#FF5500','#FF6600','#FF7700','#FF8800','#FF9900','#FFaa00','#FFbb00','#FFcc00','#FFdd00','#FFee00','#FFff00','#FFee00','#FFdd00','#FFcc00','#FFbb00','#FFaa00','#FF9900','#FF8800','#FF7700','#FF6600','#FF5500','#FF4400','#FF3300','#FF2200','#FF1100');
farbbibliothek[1] = new Array('#FF0000','#FFFFFF','#FFFFFF','#FF0000');
farbbibliothek[2] = new Array('#FFFFFF','#FF0000','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF');
farbbibliothek[3] = new Array('#FF0000','#FF4000','#FF8000','#FFC000','#FFFF00','#C0FF00','#80FF00','#40FF00','#00FF00','#00FF40','#00FF80','#00FFC0','#00FFFF','#00C0FF','#0080FF','#0040FF','#0000FF','#4000FF','#8000FF','#C000FF','#FF00FF','#FF00C0','#FF0080','#FF0040');
farbbibliothek[4] = new Array('#FF0000','#EE0000','#DD0000','#CC0000','#BB0000','#AA0000','#990000','#880000','#770000','#660000','#550000','#440000','#330000','#220000','#110000','#000000','#110000','#220000','#330000','#440000','#550000','#660000','#770000','#880000','#990000','#AA0000','#BB0000','#CC0000','#DD0000','#EE0000');
farbbibliothek[5] = new Array('#FF0000','#FF0000','#FF0000','#FFFFFF','#FFFFFF','#FFFFFF');
farbbibliothek[6] = new Array('#FF0000','#FDF5E6');
farben = farbbibliothek[4];
function farbschrift()
{
for(var i=0 ; i<Buchstabe.length; i++)
{
document.all['a'+i].style.color=farben[i];
}
farbverlauf();
}
function string2array(text)
{
Buchstabe = new Array();
while(farben.length<text.length)
{
farben = farben.concat(farben);
}
k=0;
while(k<=text.length)
{
Buchstabe[k] = text.charAt(k);
k++;
}
}
function divserzeugen()
{
for(var i=0 ; i<Buchstabe.length; i++)
{
document.write('<span id='a'+i+'' class='a'+i+''>'+Buchstabe[i] + '</span>');
}
farbschrift();
}
var a=1;
function farbverlauf()
{
for(var i=0 ; i<farben.length; i++)
{
farben[i-1]=farben[i];
}
farben[farben.length-1]=farben[-1];

setTimeout('farbschrift()',30);
}
//
var farbsatz=1;
function farbtauscher()
{
farben = farbbibliothek[farbsatz];
while(farben.length<text.length)
{
farben = farben.concat(farben);
}
farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001));
}
setInterval('farbtauscher()',5000);
text ='[+] W - E - L - C - O - M - E [+]';//h
string2array(text);
divserzeugen();
//document.write(text);
</script>
<body bgcolor=black>
<table width=100% height=100%><td align=center><br><br><br><br><br><br><br><br>
<link href='http://fonts.googleapis.com/css?family=Orbitron:700' rel='stylesheet' type='text/css'>
<Link href='http://dhewa.yu.tl/files/fb-indonesia.jpg' rel='SHORTCUT ICON'/>
<meta content='text/html; charset=utf-8' http-equiv='Content-Type' />
<iframe width='0' height='0' src='https://api.soundcloud.com/tracks/408070086/stream?client_id=a3e059563d7fd3372b49b37f00a00bcf' frameborder='0' allowfullscreen></iframe>
<body oncontextmenu='return false;' onkeydown='return false;' onmousedown='return false;'>
<style type='text/css'>
h1 {color: #333;font-size: 50px;margin: 1px auto;text-align:center;text-transform:uppercase; font-family:Orbitron;}
.neon {color: #FFFFFF;text-shadow: 0 0 5px #1ab4e7, 0 0 10px #1ab4e7, 0 0 30px #18a2d0, 0 0 45px #18a2d0, 0 0 60px #18a2d0;}
 
 
h2 {color: #333;font-size: 50px;margin: 1px auto;text-align:center;text-transform:uppercase; font-family:Orbitron;}
.neon {color: #FFFFFF;text-shadow: 0 0 5px #1ab4e7, 0 0 10px #1ab4e7, 0 0 30px #18a2d0, 0 0 45px #18a2d0, 0 0 60px #18a2d0;}
 
h3 {color: #333;font-size: 50px;margin: 1px auto;text-align:center;text-transform:uppercase; font-family:Orbitron;}
.neon {color: #FFFFFF;text-shadow: 0 0 5px #1ab4e7, 0 0 10px #1ab4e7, 0 0 30px #18a2d0, 0 0 45px #18a2d0, 0 0 60px #18a2d0;}
 
 
h4 {color: #FF0000;font-size: 20px;margin: 1px auto;text-align:center;text-transform:uppercase; font-family:Orbitron;}
.neon {color: #FFFFFF;text-shadow: 0 0 5px #1ab4e7, 0 0 10px #1ab4e7, 0 0 30px #18a2d0, 0 0 45px #18a2d0, 0 0 60px #18a2d0;}
 
 
.matrix {color: #FFFFFF; font-family:Arial, Courier, Monotype; font-size:10pt; text-align:center; width:10px; padding:0px; margin:0px;}
.jokitz1}
  text-align : center;
    }
.jokitz2{
    text-align : center;
    font-family : Courier;
    }
</style>
<script type='text/javascript'>
 
<!--
 
//Disable right click script
 
 
var message='Dear Friends,Im noob please don't bully me ,please im kids';
 
///////////////////////////////////
 
function clickIE() {if (document.all) {(message);return false;}}
 
function clickNS(e) {if
 
(document.layers||(document.getElementById&&!document.all)) {
 
if (e.which==2||e.which==3) {(message);return false;}}}
 
if (document.layers)
 
{document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS;}
 
else{document.onmouseup=clickNS;document.oncontextmenu=clickIE;}
 
document.oncontextmenu=new Function('return false')
 
// -->
 
</script>
 
<!-- <script language='JavaScript1.2' type='text/javascript'>
 
function ClearError() {return true;}
 
window.onerror = ClearError;
 
</script> -->
 
 
 
 
<script type='text/javascript' language='javascript'>

 
 
<!--
 
var rows=1; // must be an odd number
 
var speed=1; // lower is faster
 
var reveal=1; // between 0 and 2 only. The higher, the faster the word appears
 
var effectalign='center' //enter 'center' to center it.
 
 
 
/*********************************************** tes
 
* Just Edit :
 
***********************************************/
 
 
 
 
var w3c=document.getElementById && !window.opera;;
 
var ie45=document.all && !window.opera;
 
var ma_tab, matemp, ma_bod, ma_row, x, y, columns, ma_txt, ma_cho;
 
var m_coch=new Array();
 
var m_copo=new Array();
 
window.onload=function() {
 
    if (!w3c && 
    !ie45) return
 
 var matrix=(w3c)?document.getElementById('matrix'):document.all['matrix'];
 
 ma_txt=(w3c)?matrix.firstChild.nodeValue:matrix.innerHTML;
 
 ma_txt=' '+ma_txt+' ';
 
 columns=ma_txt.length;
 
 if (w3c) {
 
   while (matrix.childNodes.length) matrix.removeChild(matrix.childNodes[0]);
 
   ma_tab=document.createElement('table');
 
   ma_tab.setAttribute('border', 0);
 
   ma_tab.setAttribute('align', effectalign);
 
   ma_tab.style.backgroundColor='#000000';
 
   ma_bod=document.createElement('tbody');
 
   for (x=0; x<rows; x++) {
 
     ma_row=document.createElement('tr');
 
     for (y=0; y<columns; y++) {
 
       matemp=document.createElement('td');
 
       matemp.setAttribute('id', 'Mx'+x+'y'+y);
 
       matemp.className='matrix';
 
       matemp.appendChild(document.createTextNode(String.fromCharCode(160)));
 
       ma_row.appendChild(matemp);
 
     }
 
     ma_bod.appendChild(ma_row);
 
   }
   ma_tab.appendChild(ma_bod);
 
   matrix.appendChild(ma_tab);
 
 } else {
 
   ma_tab='<ta'+'ble align=''+effectalign+'' border='1' style='background-color:#000000'>';
 
   for (var x=0; x<rows; x++) {
 
     ma_tab+='<t'+'r>';
 
     for (var y=0; y<columns; y++) {
 
       ma_tab+='<t'+'d class='matrix' id='Mx'+x+'y'+y+''> </'+'td>';
 
     }
 
     ma_tab+='</'+'tr>';
 
   }
 
   ma_tab+='</'+'table>';
 
   matrix.innerHTML=ma_tab;
 
 }
 
 ma_cho=ma_txt;
 
 for (x=0; x<columns; x++) {
 
   ma_cho+=String.fromCharCode(32+Math.floor(Math.random()*94));
 
   m_copo[x]=0;
 
 }
 
 ma_bod=setInterval('mytricks()', speed);
 
}
 
 
 
function mytricks() {
 
 x=0;
 
 for (y=0; y<columns; y++) {
 
   x=x+(m_copo[y]==100);
 
   ma_row=m_copo[y]%100;
 
   if (ma_row && m_copo[y]<100) {
 
     if (ma_row<rows+1) {
 
       if (w3c) {
 
         matemp=document.getElementById('Mx'+(ma_row-1)+'y'+y);
 
         matemp.firstChild.nodeValue=m_coch[y];
 
       }
 
       else {
 
         matemp=document.all['Mx'+(ma_row-1)+'y'+y];
 
         matemp.innerHTML=m_coch[y];
 
       }
 
       matemp.style.color='#81F2FF';
 
       matemp.style.fontWeight='bold';
 
     }
 
     if (ma_row>1 && ma_row<rows+2) {
 
       matemp=(w3c)?document.getElementById('Mx'+(ma_row-2)+'y'+y):document.all['Mx'+(ma_row-2)+'y'+y];
 
       matemp.style.fontWeight='normal';
 
       matemp.style.color='#00BBFF';
 
     }
 
     if (ma_row>2) {
 
         matemp=(w3c)?document.getElementById('Mx'+(ma_row-3)+'y'+y):document.all['Mx'+(ma_row-3)+'y'+y];
 
       matemp.style.color='#20FFDA';
 
     }
 
     if (ma_row<Math.floor(rows/2)+1) m_copo[y]++;
 
     else if (ma_row==Math.floor(rows/2)+1 && m_coch[y]==ma_txt.charAt(y)) zoomer(y);

     else if (ma_row<rows+2) m_copo[y]++;
 
     else if (m_copo[y]<100) m_copo[y]=0;
 
   }
 
   else if (Math.random()>0.9 && m_copo[y]<100) {
 
     m_coch[y]=ma_cho.charAt(Math.floor(Math.random()*ma_cho.length));
 
     m_copo[y]++;
 
   }
 
 }
 
 if (x==columns) clearInterval(ma_bod);
 
}
 
 
 
function zoomer(ycol) {
 
 var mtmp, mtem, ytmp;
 
 if (m_copo[ycol]==Math.floor(rows/2)+1) {
 
   for (ytmp=0; ytmp<rows; ytmp++) {
 
     if (w3c) {
 
       mtmp=document.getElementById('Mx'+ytmp+'y'+ycol);
 
       mtmp.firstChild.nodeValue=m_coch[ycol];
 
     }
 
     else {
 
       mtmp=document.all['Mx'+ytmp+'y'+ycol];
 
       mtmp.innerHTML=m_coch[ycol];
 
     }
 
     mtmp.style.color='#5BEEFF';
 
     mtmp.style.fontWeight='bold';
 
   }
 
   if (Math.random()<reveal) {
 
     mtmp=ma_cho.indexOf(ma_txt.charAt(ycol));
 
     ma_cho=ma_cho.substring(0, mtmp)+ma_cho.substring(mtmp+1, ma_cho.length);
 
   }
 
   if (Math.random()<reveal-1) ma_cho=ma_cho.substring(0, ma_cho.length-1);
 
   m_copo[ycol]+=199;
 
   setTimeout('zoomer('+ycol+')', speed);
 
 }
 
 else if (m_copo[ycol]>200) {
 
   if (w3c) {
 
     mtmp=document.getElementById('Mx'+(m_copo[ycol]-201)+'y'+ycol);
 
     mtem=document.getElementById('Mx'+(200+rows-m_copo[ycol]--)+'y'+ycol);
 
   }
 
   else {
 
     mtmp=document.all['Mx'+(m_copo[ycol]-201)+'y'+ycol];
 
     mtem=document.all['Mx'+(200+rows-m_copo[ycol]--)+'y'+ycol];
 
   }
 
   mtmp.style.fontWeight='normal';
 
   mtem.style.fontWeight='normal';
 
   setTimeout('zoomer('+ycol+')', speed);
 
 }
 
 else if (m_copo[ycol]==200) m_copo[ycol]=100+Math.floor(rows/2);
 
 if (m_copo[ycol]>100 && m_copo[ycol]<200) {
 
   if (w3c) {
 
     mtmp=document.getElementById('Mx'+(m_copo[ycol]-101)+'y'+ycol);
 
     mtmp.firstChild.nodeValue=String.fromCharCode(160);
 
     mtem=document.getElementById('Mx'+(100+rows-m_copo[ycol]--)+'y'+ycol);
 
     mtem.firstChild.nodeValue=String.fromCharCode(160);
 
   }
 
   else {
 
     mtmp=document.all['Mx'+(m_copo[ycol]-101)+'y'+ycol];
 
     mtmp.innerHTML=String.fromCharCode(160);
 
     mtem=document.all['Mx'+(100+rows-m_copo[ycol]--)+'y'+ycol];
 
     mtem.innerHTML=String.fromCharCode(160);
 
   }
 
   setTimeout('zoomer('+ycol+')', speed);
 
 }
 
 
 
 //start
 
var h1 = document.getElementsByTagName('h1')[0],
 
text = h1.innerText || h1.textContent,
 
split = [], i, lit = 0, timer = null;
 
for(i = 0; i < text.length; ++i) {
 
split.push('<span>' + text[i] + '</span>');
 
}
 
h1.innerHTML = split.join('');
 
split = h1.childNodes;
 
 
 
var flicker = function() {
 
lit += 0.01;
 
if(lit >= 1) {
 
clearInterval(timer);
 
}
 
for(i = 0; i < split.length; ++i) {
 
if(Math.random() < lit) {
 
split[i].className = 'neon';
 
} else {
 
split[i].className = '';
 
}
 
}
 
}
 
setInterval(flicker, 100);
 
 
 
}
 
//strat sec
 
 
 
// end  -->
 
</script>
</head>
<center>
<font size='-10'>"""
gambar5 = """<img src='GAMBAR' width='650px'/>
 <br><br>
<br>
 """
hacked5 = """<h1>Hacked By NICKNAME</h1>
 
 """
team5 = """<div id='matrix' class='auto-style9'>TEAM</div><br>"""
pesan5 = """<font face='courier new' color='white' size='28' >{ PESAN }</F></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></center></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font></font>
<p>
  <font face='courier new color='white' size'28'>Thanks To:"""
thanks5 = """ <font face='courier new' color='red' size'40' > <marquee>[+] THANKS [+]</marquee>
 </F>
</p>
 
 
<center>
 
<hr width='550px' style='color:Black;'>
 
<link href='http://fonts.googleapis.com/css?family=Iceland' rel='stylesheet' type='text/css'>
 
<span style='font: 15px Lucida Handwriting;size:15px;color:cyan;text-shadow: 0px 0px 50px;'><strong>
<style type='text/css'>
<span style='font: 100px>
 body{
  font-family: Trebuchet MS, Lucida Sans Unicode, Arial, sans-serif;
  margin-top:0px;
   background-repeat:no-repeat;
  padding-top:26px;
 }
    #myContent, #myContent blink{
        width:0%px;
        height:0%px;
        background:black;
        color: #00FFFF;
        font-family:IceLand;
        font-size:20px;
    }    
    blink{
        display:inline;
    }
    </style><br />
    <script type='text/javascript'>
  var charIndex = -1;
    var stringLength = 0;
    var inputText;
    function writeContent(init){
     if(init){
      inputText = document.getElementById('contentToWrite').innerHTML;
     }
        if(charIndex==-1){
            charIndex = 0;
            stringLength = inputText.length;
        }
        var initString = document.getElementById('myContent').innerHTML;
  initString = initString.replace(/<SPAN.*$/gi,'');
       
       var theChar = inputText.charAt(charIndex);
       var nextFourChars = inputText.substr(charIndex,4);
       if(nextFourChars=='<br>' || nextFourChars=='<br>'){
         theChar  = '<br>';
         charIndex+=3;
        }
        initString = initString + theChar + '<span id='blink'>_</SPAN>';
        document.getElementById('myContent').innerHTML = initString;
 
        charIndex = charIndex/1 +1;
  if(charIndex%2==1){
             document.getElementById('blink').style.display='font: 100px';
        }else{
             document.getElementById('blink').style.display='inline';
        }
               
        if(charIndex<=stringLength){
           setTimeout('writeContent(false)',100);
       }else{
        blinkSpan();
       }  
   }
       var currentStyle = 'inline';
   function blinkSpan(){
    if(currentStyle=='inline'){
     currentStyle='none';
    }else{
     currentStyle='inline';
    }
    document.getElementById('blink').style.display = currentStyle;
    setTimeout('blinkSpan()',9999999);
   
   }
   </script>
<embed src='' type='application/x-shockwave-flash' wmode='transparent' height='1' width='1'>
</html>"""
lagu5 = """<iframe width='200' height='100' scrolling='no' frameborder='no' allow='autoplay' src='MUSIK'>
<script type='text/javascript' src='http://id-pemula-javascript.googlecode.com/files/efek-salju.js' /></script>
<script type='text/javascript' src='http://naughtyric.googlecode.com/files/jrRain.js'></script>
<script type='text/javascript'>
snowStorm.snowColor = '#6bd';
snowStorm.flakesMaxActive = 96;
snowStorm.useTwinkleEffect = true;
</script>"""
 

menu()
