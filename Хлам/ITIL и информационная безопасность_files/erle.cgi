
function httplize(s){return ((/^\/\//).test(s) ? ((location.protocol == 'https:')?'https:':'http:') : '') + s} 
var ar_q = '';
if(ar_q.indexOf("ad_google")!=-1){
	var ar_e = ar_q.indexOf("100=");ar_q = ar_q.slice(ar_e+4); ar_q=ar_q.split(';');
	var CgiHref =unescape(ar_q[0])+httplize('//ad.adriver.ru/cgi-bin/click.cgi?sid=126751&ad=0&bid=545568&bt=49&bn=0&pz=0&nid=0&ref=http:%2f%2fcitforum.ru%2fgazeta%2f42%2f&custom=&xpid=CzZCXsu2HxgG1oO2paFgLAz0V8I09tLvA');
}else{
	var CgiHref = httplize('//ad.adriver.ru/cgi-bin/click.cgi?sid=126751&ad=0&bid=545568&bt=49&bn=0&pz=0&nid=0&ref=http:%2f%2fcitforum.ru%2fgazeta%2f42%2f&custom=&xpid=CzZCXsu2HxgG1oO2paFgLAz0V8I09tLvA');
}
var ar_bt=49;
var ar_siteid = 126751;
var Mirror = httplize('//masterh2.adriver.ru');
var bid = 545568;
var sliceid = 0;
var ar_adid = 0;
var ar_pz=0;
var ar_sz='%2fgazeta%2f42%2f';
var ar_nid=0;
var ar_pass='';
var ar_bn=0;
var ar_geozoneid=44;
var Path = '/images/0000545/0000545568/';
var Comp0 = '0/script.js';
var Width = 240;
var Height = 400;
var date = 'Tue, 08 Mar 2016 15:39:18 GMT';
var Uid = 41760000250;
var Target = '_blank';
var Alt = 'AdRiver';
var CompPath = Mirror + Path + '0/';
var RndNum4NoCash = 399121797;
var ar_ntype = 0;
var ar_tns = 1;
var ar_rhost='ad.adriver.ru';
var ar_exposure_price = -1;
var ar_xpid = 'CzZCXsu2HxgG1oO2paFgLAz0V8I09tLvA';
if (typeof(ar_tansw) != 'undefined') clearInterval(ar_tansw);
var ar_script = '<script src="' + Mirror + Path + Comp0 + '?399121797" type="text/javascript" charset="windows-1251"><\/script>';
document.write(ar_script);


function httplize(s){return ((/^\/\//).test(s) ? ((location.protocol == 'https:')?'https:':'http:') : '') + s}
document.write('<iframe src="'+httplize('//content.a'+'driver.ru/banners/0002186/0002186173/0/0.html?0&4&6&0&399121797&1&41760000250&44&46.72.126.9&javascript')+'" style="position:absolute;top:-10000px;left:-10000px;width:10px;height:10px;border:0;"></iframe>');
