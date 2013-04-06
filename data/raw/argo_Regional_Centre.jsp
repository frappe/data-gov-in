<script language="javascript">
function EnvokeServlet(){
	docwin=window.open("http://www.incois.gov.in/Incois/FutureDeployServlet","futures");
}
</script>









  



		 







<html>
<head>
<title>Incois Argo Present Status : Geographical Information Systems, Ocean Sciences, WEBGIS system, on-line geo-referenced data, Indian Ocean Argo Implementation, Argo Planning Process, Argo floats in Indian Ocean</title>
<meta http-equiv="Content-Type" content="text/html;">

<STYLE>
<!--
a {text-decoration:none}
//-->
</STYLE>

<style>

a {text-decoration:none}

<!--
 A:link    { COLOR: #003399; TEXT-DECORATION: none; font-weight: }
 A:visited { COLOR: #003399; TEXT-DECORATION: none; font-weight: }
 A:active  { COLOR: "maroon"; TEXT-DECORATION: none; font-weight: }
 A:hover   { COLOR: #000000; TEXT-DECORATION: underline; font-weight:
cursor: hand;}

-->
</style>

<link href="argoStyles.css" rel="stylesheet" type="text/css">
<script language="JavaScript">
	
	function openargoGIS()
	{	
		
//			var argourl ="http://www.incois.gov.in/website/argonew1/default.htm";
			var argourl ="http://www.incois.gov.in/argo/arc/present.jsp";
			var params = "toolbar=no,scrollbars=yes,resizable=yes,menubar=no,top=0,left=0,width="+ screen.width +", height= "+ (screen.height * 0.9) + ",screenX=100%, screenY=100%";

			var winGisHV = window.open(argourl,'floats',params);
			
			//var winGisHV = window.open(argourl,'Floats' ,'toolbar=no, status=yes, menubar=no,scrollbars=yes,resizable=yes, fullsize=yes,top=0, left=0, width='+ screen.width +', height=' + (screen.height * 0.9) +', screenX=100%, screenY=100% ');
			winGisHV.focus();		
	
		
	}

function openargoHelp()
	{
		//
		var urlHelp ="http://www.incois.gov.in/website/argonew1/argohelp/argo.htm";
		var w = (screen.width*0.8);
		var h = (screen.height*0.8);

		var winOptions = 'toolbar=yes,menubar=yes,resizable=yes,width='+w+',height='+h+'';

		var win = window.open(urlHelp,"",winOptions);
		win.focus();
	}
	
	function openfutureGIS(gisOption)
	{
		if(gisOption=="hv")
		{

			var futureurl ="http://www.incois.gov.in/argo/arc/future.jsp";
			var params = "status=yes,toolbar=no,scrollbars=yes,resizable=yes,menubar=no,top=0,left=0,width="+ screen.width +", height= "+ (screen.height * 0.9) + ",screenX=100%, screenY=100%";
			
			var winGisHV = window.open(futureurl,'Incois',params);
			winGisHV.focus();
		}
		else
		{
			var futureurl ="http://www.incois.gov.in/website/futuredep/ie.htm";
			var params = "toolbar=no,scrollbars=yes,resizable=yes,menubar=no,top=0,left=0,width="+ screen.width +", height= "+ (screen.height * 0.9) + ",screenX=100%, screenY=100%";

			var winGisJV = window.open(futureurl,'Incois',params);
			
			//var winGisHV = window.open(argourl,'Floats' ,'toolbar=no, status=yes, menubar=no,scrollbars=yes,resizable=yes, fullsize=yes,top=0, left=0, width='+ screen.width +', height=' + (screen.height * 0.9) +', screenX=100%, screenY=100% ');
			winGisJV.focus();		
		}
		
	}
	function openindianGIS(gisOption)
	{
		//if(gisOption=="hv")
		//{

			//var futureurl ="http://www.incois.gov.in/website/futureht/default.htm";
		var futureurl ="http://www.incois.gov.in/website/argo_india/default.htm";
			var params = "status=yes,toolbar=no,scrollbars=yes,resizable=yes,menubar=no,top=0,left=0,width="+ screen.width +", height= "+ (screen.height * 0.9) + ",screenX=100%, screenY=100%";
			
			var winGisHV = window.open(futureurl,'Incois',params);
			winGisHV.focus();
		
		
	}


function openfutureHelp()
	{
		//
		var urlHelp ="http://www.incois.gov.in/website/futureht/futhelp/webhelpstart.htm";
		var w = (screen.width*0.8);
		var h = (screen.height*0.8);

		var winOptions = 'toolbar=yes,menubar=yes,resizable=yes,width='+w+',height='+h+'';

		var win = window.open(urlHelp,"",winOptions);
		win.focus();
	}

 </script>

<script src="js/showHide1.js" type="text/javascript"></script>

<style>#topLev{position:absolute;z-index:100;left:10px;top:190px;visibility:hidden;}</style>
<style>#argoLev{position:absolute;z-index:100;left:10px;top:190px;visibility:hidden;}</style>
<style>#argoLev1{position:absolute;z-index:100;left:10px;top:190px;visibility:hidden;}</style>
<style>#dataManageLev{position:absolute;z-index:100;left:10px;top:190px;visibility:hidden;}</style>
<style>#missionLev{position:absolute;z-index:100;left:10px;top:190px;visibility:hidden;}</style>
<style>#servicesLev{position:absolute;z-index:100;left:10px;top:190px;visibility:hidden;}</style>
<style>#linksLev{position:absolute;z-index:100;left:10px;top:190px;visibility:hidden;}</style>
</head>

<body topmargin="0" leftmargin="0" marginheight="0" marginwidth="0" onLoad="JavaScript:showArea('servicesLev');" >
<!-- include accesshistory file for storing visited pages for registered users -->








<html>
<head>
<title>Incois</title>
<meta http-equiv="Content-Type" content="text/html;">
<!-- Fireworks 4.0  Dreamweaver 4.0 target.  Created Tue Jun 04 12:17:43 GMT+0530 (India Standard Time) 2002-->
<script language="JavaScript">
<!--
function MM_findObj(n, d) { //v3.0
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document); return x;
}
function MM_nbGroup(event, grpName) { //v3.0
  var i,img,nbArr,args=MM_nbGroup.arguments;
  if (event == "init" && args.length > 2) {
    if ((img = MM_findObj(args[2])) != null && !img.MM_init) {
      img.MM_init = true; img.MM_up = args[3]; img.MM_dn = img.src;
      if ((nbArr = document[grpName]) == null) nbArr = document[grpName] = new Array();
      nbArr[nbArr.length] = img;
      for (i=4; i < args.length-1; i+=2) if ((img = MM_findObj(args[i])) != null) {
        if (!img.MM_up) img.MM_up = img.src;
        img.src = img.MM_dn = args[i+1];
        nbArr[nbArr.length] = img;
    } }
  } else if (event == "over") {
    document.MM_nbOver = nbArr = new Array();
    for (i=1; i < args.length-1; i+=3) if ((img = MM_findObj(args[i])) != null) {
      if (!img.MM_up) img.MM_up = img.src;
      img.src = (img.MM_dn && args[i+2]) ? args[i+2] : args[i+1];
      nbArr[nbArr.length] = img;
    }
  } else if (event == "out" ) {
    for (i=0; i < document.MM_nbOver.length; i++) {
      img = document.MM_nbOver[i]; img.src = (img.MM_dn) ? img.MM_dn : img.MM_up; }
  } else if (event == "down") {
    if ((nbArr = document[grpName]) != null)
      for (i=0; i < nbArr.length; i++) { img=nbArr[i]; img.src = img.MM_up; img.MM_dn = 0; }
    document[grpName] = nbArr = new Array();
    for (i=2; i < args.length-1; i+=2) if ((img = MM_findObj(args[i])) != null) {
      if (!img.MM_up) img.MM_up = img.src;
      img.src = img.MM_dn = args[i+1];
      nbArr[nbArr.length] = img;
  } }
}

function MM_preloadImages() { //v3.0
 var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
   var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
   if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

function fwLoadMenus() {
  if (window.fw_menu_0) return;
  window.fw_menu_0 = new Menu("root",219,19,"Arial, Helvetica, sans-serif",12,"#2b5c86","#ffffff","#ffffff","#2b5c86");
  fw_menu_0.addMenuItem("MISSION","location='../../Incois/org_mission.jsp'");
  fw_menu_0.addMenuItem("ACTIVITY SPECTRUM","location='../../Incois/org_activity.jsp'");
    fw_menu_0.addMenuItem("STRUCTURE","location='../../Incois/org_structure.jsp'");
    fw_menu_0.addMenuItem("HUMAN CAPITAL","location='../../Incois/org_Scientific.jsp'");
  fw_menu_0.addMenuItem("ANNUAL REPORTS","location='../../Incois/org_annual_main.jsp'");
   fw_menu_0.fontWeight="bold";
   fw_menu_0.hideOnMouseOut=true;
  window.fw_menu_1 = new Menu("root",263,19,"Arial, Helvetica, sans-serif",12,"#2b5c86","#ffffff","#ffffff","#2b5c86");
  fw_menu_1.addMenuItem("POTENTIAL FISHING ZONES","window.open('../../Incois/advisory_pfz_main.jsp', '_top');");
    fw_menu_1.addMenuItem("OCEAN STATE FORECAST","window.open('../../Incois/advisory_osf_main.jsp', '_top');");
   fw_menu_1.fontWeight="bold";
   fw_menu_1.hideOnMouseOut=true;
  window.fw_menu_2 = new Menu("root",128,19,"Arial, Helvetica, sans-serif",12,"#2b5c86","#ffffff","#ffffff","#2b5c86");
  fw_menu_2.addMenuItem("ARGO","location='/argo'");
  
   fw_menu_2.fontWeight="bold";
   fw_menu_2.hideOnMouseOut=true;
  window.fw_menu_3 = new Menu("root",187,19,"Arial, Helvetica, sans-serif",12,"#2b5c86","#ffffff","#ffffff","#2b5c86");
 fw_menu_3.addMenuItem("OCEAN MODELLING","location='/Incois/oceanservices.jsp'");
  fw_menu_3.addMenuItem("SATELLITE OCEANOGRAPHY","location='/Incois/satelliteocean.jsp'");
   fw_menu_3.fontWeight="bold";
   fw_menu_3.hideOnMouseOut=true;

  fw_menu_3.writeMenus();
} // fwLoadMenus()

//-->
</script>
<script language="JavaScript1.2" src="/Images/js/fw_menu.js"></script>
</head>
<body topmargin="0" leftmargin="0" marginheight="0" marginwidth="0"  style="background:url('/Images/incois1024/home/bghd.jpg') repeat-x #ffffff;" onLoad="MM_preloadImages('top_r3_c2_f2.gif','top_r3_c2_f3.gif','top_r2_c4_f2.gif','top_r2_c4_f3.gif','top_r2_c6_f2.gif','top_r2_c6_f4.gif','top_r2_c6_f3.gif','top_r2_c8_f2.gif','top_r2_c8_f4.gif','top_r2_c8_f3.gif','top_r2_c10_f2.gif','top_r2_c10_f4.gif','top_r2_c10_f3.gif','top_r2_c12_f2.gif','top_r2_c12_f4.gif','top_r2_c12_f3.gif');">
<script language="JavaScript1.2">fwLoadMenus();</script>
<table border="0" cellpadding="0" cellspacing="0" width="1004">
<!-- fwtable fwsrc="top1024.png" fwbase="top.gif" fwstyle="Dreamweaver" fwdocid = "742308039" fwnested="1" -->
  <tr>
   <td colspan="13"><img name="top_r1_c1" src="/Images/incois1024/home/top_r1_c1.jpg" width="1004" height="60" border="0"></td>
  </tr>
  <tr>
   <td rowspan="2"><img name="top_r2_c1" src="/Images/incois1024/home/top_r2_c1.gif" width="15" height="21" border="0"></td>
   <td><table border="0" cellpadding="0" cellspacing="0" width="39">
	  <tr>
	   <td><img name="top_r2_c2" src="/Images/incois1024/home/top_r2_c2.gif" width="39" height="1" border="0"></td>
	  </tr>
	  <tr>
	   <td><a href="../../Incois/incois1024/index/index.jsp" onMouseOut="MM_nbGroup('out');"  onMouseOver="MM_nbGroup('over','top_r3_c2','/Images/incois1024/home/top_r3_c2.gif','/Images/incois1024/home/top_r3_c2.gif',1);"  onClick="MM_nbGroup('down','navbar1','top_r3_c2','/Images/incois1024/home/top_r3_c2.gif',1);" ><img name="top_r3_c2" src="/Images/incois1024/home/top_r3_c2.gif" width="39" height="10" border="0"></a></td>
	  </tr>
	</table></td>
   <td rowspan="2"><img name="top_r2_c3" src="/Images/incois1024/home/top_r2_c3.gif" width="24" height="21" border="0"></td>
   
   	
			<td><a href="../../Incois/organisation.jsp" onMouseOut="MM_nbGroup('out');FW_startTimeout();"  onMouseOver="window.FW_showMenu(window.fw_menu_0,28,80);MM_nbGroup('over','top_r2_c4','/Images/incois1024/home/top_r2_c4.gif','/Images/incois1024/home/top_r2_c4.gif',1);"  onClick="MM_nbGroup('down','navbar1','top_r2_c4','/Images/incois1024/home/top_r2_c4.gif',1);" ><img name="top_r2_c4" src="/Images/incois1024/home/top_r2_c4.gif" width="101" height="11" border="0"></a></td>
	
   
   <td rowspan="2"><img name="top_r2_c5" src="/Images/incois1024/home/top_r2_c5.gif" width="17" height="21" border="0"></td>
   
   	
         <td><a href="../../Incois/advisory.jsp" onMouseOut="MM_nbGroup('out');FW_startTimeout();"  onMouseOver="window.FW_showMenu(window.fw_menu_1,136,80);MM_nbGroup('over','top_r2_c6','/Images/incois1024/home/top_r2_c6.gif','/Images/incois1024/home/top_r2_c6.gif',1);"  onClick="MM_nbGroup('down','navbar1','top_r2_c6','/Images/incois1024/home/top_r2_c6.gif',1);" ><img name="top_r2_c6" src="/Images/incois1024/home/top_r2_c6.gif" width="137" height="11" border="0"></a></td>
	
   
   <td rowspan="2"><img name="top_r2_c7" src="/Images/incois1024/home/top_r2_c7.gif" width="19" height="21" border="0"></td>

	
      <td><a href="../../Incois/informationbank.jsp" onMouseOut="MM_nbGroup('out');"  onMouseOver="MM_nbGroup('over','top_r2_c8','/Images/incois1024/home/top_r2_c8.gif','/Images/incois1024/home/top_r2_c8.gif',1);"  onClick="MM_nbGroup('down','navbar1','top_r2_c8','/Images/incois1024/home/top_r2_c8.gif',1);" ><img name="top_r2_c8" src="/Images/incois1024/home/top_r2_c8.gif" width="133" height="11" border="0"></a></td>
	

   <td rowspan="2"><img name="top_r2_c9" src="/Images/incois1024/home/top_r2_c9.gif" width="19" height="21" border="0"></td>
   
   	
      		   <td><a href="../../Incois/oceanobservation.jsp" onMouseOut="MM_nbGroup('out');FW_startTimeout();"  onMouseOver="window.FW_showMenu(window.fw_menu_2,503,80);MM_nbGroup('over','top_r2_c10','/Images/incois1024/home/top_r2_c10.gif','/Images/incois1024/home/top_r2_c10.gif',1);"  onClick="MM_nbGroup('down','navbar1','top_r2_c10','/Images/incois1024/home/top_r2_c10.gif',1);" ><img name="top_r2_c10" src="/Images/incois1024/home/top_r2_c10.gif" width="144" height="11" border="0"></a></td>
	
   
   <td rowspan="2"><img name="top_r2_c11" src="/Images/incois1024/home/top_r2_c11.gif" width="15" height="21" border="0"></td>

	
      		 <td><a href="#" onMouseOut="MM_nbGroup('out');FW_startTimeout();"  onMouseOver="window.FW_showMenu(window.fw_menu_3,620,80);MM_nbGroup('over','top_r2_c12','/Images/incois1024/home/top_r2_c12.gif','/Images/incois1024/home/top_r2_c12.gif',1);"  onClick="MM_nbGroup('down','navbar1','top_r2_c12','/Images/incois1024/home/top_r2_c12.gif',1);" ><img name="top_r2_c12" src="/Images/incois1024/home/top_r2_c12.gif" width="118" height="11" border="0"></a></td>
	

   
  
   <td rowspan="2"><img name="top_r2_c13" src="/Images/incois1024/home/top_r2_c13.jpg" width="223" height="21" border="0"></td>
  </tr>
  <tr>
   <td><img name="top_r4_c2" src="/Images/incois1024/home/top_r4_c2.gif" width="39" height="10" border="0"></td>
   <td><img name="top_r4_c4" src="/Images/incois1024/home/top_r4_c4.gif" width="101" height="10" border="0"></td>
   <td><img name="top_r4_c6" src="/Images/incois1024/home/top_r4_c6.gif" width="137" height="10" border="0"></td>
   <td><img name="top_r4_c8" src="/Images/incois1024/home/top_r4_c8.gif" width="133" height="10" border="0"></td>
   <td><img name="top_r4_c10" src="/Images/incois1024/home/top_r4_c10.gif" width="144" height="10" border="0"></td>
   <td><img name="top_r4_c12" src="/Images/incois1024/home/top_r4_c12.gif" width="118" height="10" border="0"></td>
  </tr>
</table>
</body>
</html>



<table width="100%" border="0" cellspacing="0" bgcolor="#336699" cellpadding="0" height="87%">
  <tr> 
    <td bgcolor="#2B5C85" width="20%" align="left" valign="top" height="100%" > 
	  <BR><div align="center"><img src="images/argo_boat1.gif" border="no" align="center"></div>
	  
	  <div id="topLev" name="topLev"> 
	     <table cellpadding="0" cellspacing="0" border="0" width="100%" height="100%">
          <tr> 
            <td class="argo">
			<a STYLE="text-decoration:none" href="argo_home.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Home</font></a><BR>

			<a STYLE="text-decoration:none" href="argo_National_Centre.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo National Data Centre </font></a><BR>
			
			<a STYLE="text-decoration:none" href="argo_Regional_Centre.jsp" ><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Regional Centre</font></a></td>
          </tr>
         </table>
      </div>

      <div id="argoLev" name="argoLev"> 
	     <table cellpadding="0" cellspacing="0" border="0" width="100%" height="100%">
		<tr><td class="argo">
			<a STYLE="text-decoration:none" href="JavaScript:showArea('topLev');"><img src="images/open_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Home</font></a><br>
			
						

			<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_home.jsp"><font class="argo" color="#FFFFFF"> About Argo</font></a><BR>
			

				
			<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_objectives.jsp"><font class="argo" color="#FFFFFF"> Objectives</font></a><BR>
			

			
			
			<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_argoinfo.jsp"><font class="argo" color="#FFFFFF"> Argo Info Centre</font></a><BR>
			
			
			
			
			<img src="images/blank.gif"><a STYLE="text-decoration:none" href="argo_datamanage.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Data Management</font></a><BR>
			
			
			
			
			<img src="images/blank.gif"><a STYLE="text-decoration:none" href="argo_links.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Other Links</font></a><br>
			
									
			<a STYLE="text-decoration:none" href="argo_National_Centre.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo National Data Centre </font></a><br>

			<a STYLE="text-decoration:none" href="argo_Regional_Centre.jsp" ><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Regional Centre</font></a>
			</td></tr></table></div>

	<div id="dataManageLev" name="dataManageLev"> 
	     <table cellpadding="0" cellspacing="0" border="0" width="100%" height="100%">
		<tr><td class="argo">
			<a STYLE="text-decoration:none" href="argo_home.jsp"><img src="images/open_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Home</font></a><br>
			
			<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_index.jsp"><font class="argo" color="#FFFFFF"> About Argo</font></a><BR>
			
			<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_objectives.jsp"><font class="argo" color="#FFFFFF"> Objectives</font></a><BR>

			<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_argoinfo.jsp"><font class="argo" color="#FFFFFF">Argo Info Centre</font></a><BR>
			
				
			<img src="images/blank.gif"><a STYLE="text-decoration:none" href="JavaScript:showArea('argoLev');"><img src="images/open_folder.gif" border=0><font class="argo" color="#FFFFFF"> Data Management</font></a><BR>
			
					
					<img src="images/blank1.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_datanational.jsp"><font class="argoinner" color="#FFFFFF">National</font></a><br>
					

					
					<img src="images/blank1.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_dataregional.jsp"><font class="argoinner" color="#FFFFFF">Regional</font></a><br>
					

					
					<img src="images/blank1.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_dataglobal.jsp"><font class="argoinner" color="#FFFFFF">Global</font></a><br>
					

					
					<img src="images/blank1.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_datalongterm.jsp"><font class="argoinner" color="#FFFFFF">Long Term Archive</font></a><br>
					
			
			
			
			<img src="images/blank.gif"><a STYLE="text-decoration:none" href="argo_links.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Other Links</font></a><br>

			<a STYLE="text-decoration:none" href="argo_National_Centre.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo National Data Centre </font></a><br>

			<a STYLE="text-decoration:none" href="argo_Regional_Centre.jsp" ><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Regional Centre</font></a>
			</td></tr></table></div>

	<div id="linksLev" name="linksLev"> 
	     <table cellpadding="0" cellspacing="0" border="0" width="100%" height="100%">
		<tr><td class="argo">
			<a STYLE="text-decoration:none" href="argo_home.jsp"><img src="images/open_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Home</font></a><br>
			
			<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_index.jsp"><font class="argo" color="#FFFFFF"> About Argo</font></a><BR>
			
			<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_objectives.jsp"><font class="argo" color="#FFFFFF"> Objectives</font></a><BR>

			<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_argoinfo.jsp"><font class="argo" color="#FFFFFF">Argo Info Centre</font></a><BR>

			<img src="images/blank.gif"><a STYLE="text-decoration:none" href="argo_datamanage.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Data Management</font></a><BR>
			
			<img src="images/blank.gif"><a STYLE="text-decoration:none" href="JavaScript:showArea('argoLev');"><img src="images/open_folder.gif" border=0><font class="argo" color="#FFFFFF"> Other Links</font></a><br>

					
					<img src="images/blank1.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_links.jsp"><font class="argoinner" color="#FFFFFF"> Other programs</font></a><br>
					
					
					
					  <img src="images/blank1.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_global.jsp"><font class="argoinner" color="#FFFFFF"> Global Ocean</font></a><BR>
					  

					  
					  <img src="images/blank1.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_otherdata.jsp"><font class="argoinner" color="#FFFFFF"> Other Data Centres</font></a><BR>
					  

			 <a STYLE="text-decoration:none" href="argo_National_Centre.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo National Data Centre </font></a><br>

			<a STYLE="text-decoration:none" href="argo_Regional_Centre.jsp" ><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Regional Centre</font></a>
			</td></tr></table></div>

		<div id="argoLev1" name="argoLev1"> 
	     <table cellpadding="0" cellspacing="0" border="0" width="100%" height="100%">
          <tr> 
            <td class="argo">
			<a STYLE="text-decoration:none" href="argo_home.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Home</font></a><BR>

			<a STYLE="text-decoration:none" href="JavaScript:showArea('topLev');"><img src="images/open_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo National Data Centre </font></a><BR>


					
						<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_organise.jsp"><font class="argo" color="#FFFFFF"> Organisation</font></a><BR>
						
						
					  <img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_scope.jsp"><font class="argo" color="#FFFFFF"> Scope </font></a><BR>
					  
					  
						<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_imperatives.jsp"><font class="argo" color="#FFFFFF"> Scientific&nbsp;Imperatives</font></a><BR>
						 
					  
						<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="products/argo_frames_national.html" target="_blank"><font class="argo" color="#FFFFFF">National Argo Products</font></a><BR>
						 
						 
						<img src="images/blank.gif" border=0><img src="images/dot4.gif" border=0>
						<a STYLE="text-decoration:none" href='#' onClick='javascript:openindianGIS()'><font class="argo" color="#FFFFFF"> Present Status of Argo Floats<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in Indian Ocean</font></a>&nbsp;
						<a STYLE="text-decoration:none" href='#'><img src="images/help.gif" border=0 alt='Help' title='Help' onClick='javascript:openfutureHelp()'></a><br>
						
						
						<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_othercentres.jsp"> <font class="argo" color="#FFFFFF">Other Data Centers</font></a><BR>
						 
						 
						 <a STYLE="text-decoration:none" href="argo_Floatmission.jsp"><img src="images/blank.gif" border=0><img src="images/closed_folder.gif" border=0>&nbsp;<font class="argo" color="#FFFFFF"> Float Mission </font></a><br>
			
			<a STYLE="text-decoration:none" href="argo_Regional_Centre.jsp" ><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Regional Centre</font></a></td>
          </tr>
         </table>
      </div>
	     <div id="missionLev" name="missionLev"> 
	     <table cellpadding="0" cellspacing="0" border="0" width="100%" height="100%">
          <tr> 
            <td class="argo">
			<a STYLE="text-decoration:none" href="argo_home.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Home</font></a><BR>

			<a STYLE="text-decoration:none" href="JavaScript:showArea('topLev');"><img src="images/open_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo National Data Centre </font></a><BR>


				<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_organise.jsp"><font class="argo" color="#FFFFFF"> Organization</font></a><BR>
					
				 <img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_scope.jsp"><font class="argo" color="#FFFFFF"> Scope </font></a><BR>
				
				<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_imperatives.jsp"><font class="argo" color="#FFFFFF">Scientific Imperatives</font></a><BR>

				<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;
				<a STYLE="text-decoration:none" href="products/argo_frames_national.html"><font class="argo" color="#FFFFFF">National Argo Products</font></a><br>

				<img src="images/blank.gif" border=0><img src="images/dot4.gif" border=0>
				<a STYLE="text-decoration:none" href='#' onClick='javascript:openargoGIS()'><font class="argo" color="#FFFFFF"> Present Status of Argo Floats in Indian Ocean</font></a>&nbsp;
				<a STYLE="text-decoration:none" href='#'><img src="images/help.gif" border=0 alt='Help' title='Help' onClick='javascript:openfutureHelp()'></a><br>
				
				<img src="images/blank.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_othercentres.jsp"><font class="argo" color="#FFFFFF">Other Data Centers</font></a><BR>
					
				<a STYLE="text-decoration:none" href="JavaScript:showArea('argoLev1');"><img src="images/blank.gif" border=0><img src="images/open_folder.gif" border=0>&nbsp;<font class="argo" color="#FFFFFF"> Float Mission </font>
				</a><br>
					
			    		<img src="images/blank1.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_missn1.jsp"><font class="argoinner"color="#FFFFFF"> Mission 1</font></a><br>
					
						 
					
			    		<img src="images/blank1.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_missn2.jsp"><font class="argoinner"color="#FFFFFF"> Mission 2 </font></a><br>
					
						
					
			    		<img src="images/blank1.gif"><img src="images/dot4.gif">&nbsp;<a STYLE="text-decoration:none" href="argo_missn3.jsp"><font class="argoinner"color="#FFFFFF"> Mission 3 </font></a><br>
					
						
											
			
			<a STYLE="text-decoration:none" href="argo_Regional_Centre.jsp" ><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Regional Centre</font></a></td>
          </tr>
		          </table>
      </div>
	  <div id="servicesLev" name="servicesLev"> 
	     <table cellpadding="0" cellspacing="0" border="0" width="100%" height="100%">
          <tr><td class="argo"> 
			<a STYLE="text-decoration:none" href="argo_home.jsp"><img src="images/closed_folder.gif" border=0><font class="argo" color="#FFFFFF"> Argo Home</font></a><BR>
            <a STYLE="text-decoration:none" href="argo_National_Centre.jsp"><img src="images/closed_folder.gif" border=0><font color="#FFFFFF"> Argo National Data Centre </font></a><br>
			
			
			<a STYLE="text-decoration:none" href="JavaScript:showArea('topLev');"><img src="images/open_folder.gif" border=0><font color="#FFCC33"> Argo Regional Centre</font></a><br>
			
			<img src="images/blank.gif" border=0><img src="images/dot4.gif" border=0>
			<a STYLE="text-decoration:none" href='#' onClick='javascript:openargoGIS()'><font class="argoinner" color="#FFFFFF"> Present Status of Argo Floats in <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Indian Ocean</font></a>&nbsp;
			<a STYLE="text-decoration:none" href='#'><img src="images/help.gif" border=0 alt='Help' title='Help' onClick='javascript:openfutureHelp()'></a><br>

			<img src="images/blank.gif" border=0><img src="images/dot4.gif" border=0>
			<a STYLE="text-decoration:none" href='#' onClick='#' ><font class="argoinner" color="#FFFFFF"> Delayed Mode Quality Control </font></a>
			<a STYLE="text-decoration:none" href='argo_Hyd_report.pdf' target="docwindow"><img src="images/help.gif" border=0 alt='India Ocean Implementation Meeting' ></a><br>
					
			<img src="images/blank.gif" border=0><img src="images/dot4.gif" border=0>
			<a STYLE="text-decoration:none" href="products/argo_frames.html" target="docwindow"><font class="argoinner" color="#FFFFFF"> Argo Value added Products </font></a>&nbsp;
			<a STYLE="text-decoration:none" href='products/writeup.htm' target="docwindow"><img src="images/help.gif" border=0 alt='About data Processing' ></a><br>

			<img src="images/blank.gif" border=0><img src="images/dot4.gif" border=0>
			<a STYLE="text-decoration:none" href="http://las.incois.gov.in/" target="_blank" ><font class="argoinner" color="#FFFFFF"> Live Access Server </font></a>&nbsp;
			<a STYLE="text-decoration:none" href='argo_Hyd_report.pdf' target="docwindow"><img src="images/help.gif" border=0 alt='About Live access Server' ></a><br>
			
			<img src="images/blank.gif" border=0><img src="images/dot4.gif" border=0>
			
			<a STYLE="text-decoration:none" href="http://www.incois.gov.in/Incois/argo/argostats_index.jsp" target="_blank"><font class="argoinner" color="#FFFFFF">Statistics of the Floats </font></a>&nbsp;
			<a STYLE="text-decoration:none" href='#'><img src="images/help.gif" border=0 alt='Statistics of Floats' ></a><br>

			<img src="images/blank.gif" border=0><img src="images/dot4.gif" border=0>
			<a STYLE="text-decoration:none" href="#"><font class="argoinner" color="#FFFFFF"> Reference data / Consistancy of<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; the Floats </font></a>&nbsp;
			<a STYLE="text-decoration:none" href='#'><img src="images/help.gif" border=0 alt='India Ocean Implementation Meeting' ></a><br>

			<img src="images/blank.gif" border=0><img src="images/dot4.gif" border=0>
			<a STYLE="text-decoration:none" href='#' onClick='javascript:openfutureGIS()' ><font class="argoinner" color="#FFFFFF"> Basin Level Deployement <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Co-ordination</font></a>&nbsp;
			<a STYLE="text-decoration:none" href='#'><img src="images/help.gif" border=0 alt='Help' title='Help' onClick='javascript:openfutureHelp()'></a><br>

			<img src="images/blank.gif" border=0><img src="images/dot4.gif" border=0>
			<a STYLE="text-decoration:none" href='/Incois/incois_argo_apex_manual.jsp'><font class="argoinner" color="#FFFFFF">INCOIS APEX Profilers <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;User Manuals</font></a>
  			</td>
          </tr>
        </table>
      </div>
			
	</td>
    <td bgcolor="#FFFFFF" align="left" width="62%" valign="top" rowspan="2" height="100%" > 
      
      <table width="100%" border="0" cellspacing="10" cellpadding="0"  align="center" height="100%">
        <tr valign="top"> 
          <td  > 
            <p align="justify"><font face="Arial, Helvetica, sans-serif" size="2" ><font class="argo" color="#000000"> 
              <form name='frmargowebgis'><table width='100%' border='0' cellspacing='3' cellpadding='0' align='center'><tr> <td height='500' align='left' valign='top'><br><CENTER><font face='Arial, Helvetica, sans-serif' size='2'><b>ARGO FLOATS IN INDIAN OCEAN</b></font></CENTER><br> <P ALIGN='JUSTIFY'><font face='Arial, Helvetica, sans-serif' size=2><ul><li><a href='#' onClick='javascript:openargoGIS()'>Present Status of Argo Floats in Indian Ocean.</a></li><li><a  href='#' onClick='javascript:openfutureGIS()' >Future Deployment Status of Argo floats in Indian Ocean.</a></li><li><a target='_blank' href='products/argo_frames.html' >Argo Value added Products.</a></li><li><a target='_blank'  href='http://las.incois.gov.in/' >Live Access Server.</a></li>			<li><a target='_blank' href='/Incois/ArgoEEZ.jsp'>Argo Floats in EEZ.</a></li>			</ul></p></td></tr></table></form> </font></font></p>
          </td>
        </tr>
      </table>
      
    </td>
    <td bgcolor="#2B5C85" width="18%" align="center" valign="top" rowspan="2" height="100%" > 
      
  <body link="#FFFF00" alink="#FFFF00" vlink="#FFFF00">
     
<SCRIPT language="JavaScript">

// Function for searching within the site
function SearchInSite_click(form)
{   
	// Check for null search criteria
	if (form.txtSearch.value == "")
	{
		alert("Enter search criteria");
		return false;
	}
	
	//Check for search criteria less than 3 letters
	if (form.txtSearch.value.length <= 2)
	{
		alert("Enter search criteria with more than two letters");
		return false;
	}
	//Submits Search form
	form.submit();
}

// Function for searching in the web
function SearchOnWeb_click()
{   
	// Check for null search criteria
	if (document.frmSearch.txtSearch.value == "")
	{
		alert("Enter search criteria");
		return false;
	}

	//Sending the search criteria to searchonweb.jsp
	if (document.frmSearch.txtSearch.value)
	{   
		var url;
		url = "searchonweb.jsp?txtSearch=" + document.frmSearch.txtSearch.value 
		  window.open(url);
	}
}

</SCRIPT>

<BODY>
    <!-- Form for Search callin Search servlet on submission -->
    <FORM NAME="frmSearch" METHOD="post" ACTION="/Incois/Search">
	    <TABLE BORDER=0 WIDTH=100%>
            <TR>
			    <TD ALIGN=CENTER><FONT FACE="Arial, Helvetica, sans-serif" size="2"><FONT COLOR="#FFFFFF">Search For</FONT></FONT><BR>
				    <!-- Text box for containing Search Criteria -->
					<INPUT NAME="txtSearch" TYPE="TEXT" STYLE="WIDTH:90%" SIZE="14" ALIGN=CENTER>
	       		</TD>
		   </TR>
	 	   <TR>
			    <TD>
				    <!-- Radio button to search within site -->
					<INPUT TYPE="RADIO" NAME="radsearch"  VALUE="site" ONCLICK="SearchInSite_click(frmSearch);" >
        			<FONT FACE="Arial, Helvetica, sans-serif" SIZE="2"><FONT COLOR="#FFFFFF">In this site</FONT></FONT>
					<BR>
				    <!-- Radio button to search in the web -->
       				<INPUT TYPE="radio" NAME="radsearch" VALUE="web" ONCLICK="SearchOnWeb_click();" ><FONT FACE="Arial, Helvetica, sans-serif" SIZE="2"><FONT COLOR="#FFFFFF"> On Web </FONT></FONT>
			    </TD>
		   </TR>		
	    </TABLE>
    </FORM>


	 
	 
	  





<table width="10%" border="0" align="center">
  <tr> 
    <td colspan="2"> 
      <div align="center"><font face="Arial, Helvetica, sans-serif" size="2" color="#FFFFFF">Home</font></div>
    </td>
  </tr>
  
	  <tr> 
		<td colspan="2" align=center><img src="vert_line.gif" width="16" height="16"></td>
	  </tr>
	  <tr>
	  
	  <td align="center" colspan="2" ><font face="Arial, Helvetica, sans-serif" size="2" color="#FFFFFF">Ocean&nbsp;Observation</font></td>
	  </tr>
	  
	  <tr> 
		<td colspan="2" align="center"><img src="vert_line.gif" width="16" height="16"></td>
	  </tr>
	  <tr>
	  
	  <td align="center" colspan=2><font face="Arial, Helvetica, sans-serif" size="2" color="#FFFFFF">Argo</font></td>
	  
	  </tr>
	  
  <tr> 
    <td colspan="2" align="center"><img src="vert_line.gif" width="16" height="16"></td>
  </tr>
  <tr> 
    <td align="right"><img src="blink.gif"></td>
    <td align="center"><font face="Arial, Helvetica, sans-serif" size="2" color="#FFFFFF">Argo&nbsp;Regional&nbsp;Center</font></td>
  </tr>
  
</table>


	  
		
		<br>
		<br>

</body>
    </td>
  </tr>
</table>

</body>
</html>


<!--
<html>
<head>
<title>Incois Argo Present Status : Geographical Information Systems, Ocean Sciences, WEBGIS system, on-line geo-referenced data, Indian Ocean Argo Implementation, Argo Planning Process,Argo floats in Indian Ocean</title> 

<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">

<meta name="Description" content="The Indian National Centre for Ocean Information Services (INCOIS) provides ocean information and advisory services to the society, industry, government and scientific community through sustained ocean observations and constant improvement through systematic and focused research.">

<meta name="Keywords" content="Ocean Sciences, Geographical Information Systems, WEBGIS system, on-line geo-referenced data, Indian Ocean Argo Implementation, Argo Planning Process,Argo floats in Indian Ocean">

-->


<script>
function openargoGIS(gisOption)
	{	
		/*if(gisOption=="jv")
		{

			var argourl ="http://www.incois.gov.in/website/jrehelp_argo.html";
			var params = "toolbar=no,scrollbars=yes,resizable=yes,menubar=no,top=0,left=0,width="+ screen.width +", height= "+ (screen.height * 0.9) + ",screenX=100%, screenY=100%";
			
			var winGisJV = window.open(argourl,'JREHelp',params);
			winGisJV.focus();
		}*/
		//else
		//{
			var argourl ="http://www.incois.gov.in/website/argonew1/default_reg.htm";
			var params = "toolbar=no,scrollbars=yes,resizable=yes,menubar=no,top=0,left=0,width="+ screen.width +", height= "+ (screen.height * 0.9) + ",screenX=100%, screenY=100%";

			var winGisHV = window.open(argourl,'floats',params);
			
			//var winGisHV = window.open(argourl,'Floats' ,'toolbar=no, status=yes, menubar=no,scrollbars=yes,resizable=yes, fullsize=yes,top=0, left=0, width='+ screen.width +', height=' + (screen.height * 0.9) +', screenX=100%, screenY=100% ');
			winGisHV.focus();		
		//}
		
	}

function openfutureGIS(gisOption)
	{
		//if(gisOption=="hv")
		//{

			//var futureurl ="http://www.incois.gov.in/website/futureht/default.htm";
//		var futureurl ="http://www.incois.gov.in/website/futureextended1/viewerdefault.htm";
		var futureurl ="http://www.incois.gov.in/argo/arc/future.jsp";
			var params = "status=yes,toolbar=no,scrollbars=yes,resizable=yes,menubar=no,top=0,left=0,width="+ screen.width +", height= "+ (screen.height * 0.9) + ",screenX=100%, screenY=100%";
			
			var winGisHV = window.open(futureurl,'Incois',params);
			winGisHV.focus();
		//}
		/*else
		{
			var futureurl ="http://www.incois.gov.in/website/futuredep/ie.htm";
			var params = "toolbar=no,scrollbars=yes,resizable=yes,menubar=no,top=0,left=0,width="+ screen.width +", height= "+ (screen.height * 0.9) + ",screenX=100%, screenY=100%";

			var winGisJV = window.open(futureurl,'Incois',params);
			
			//var winGisHV = window.open(argourl,'Floats' ,'toolbar=no, status=yes, menubar=no,scrollbars=yes,resizable=yes, fullsize=yes,top=0, left=0, width='+ screen.width +', height=' + (screen.height * 0.9) +', screenX=100%, screenY=100% ');
			winGisJV.focus();		
		}*/
		
	}
	function openindiaGIS(gisOption)
	{
		//if(gisOption=="hv")
		//{

			//var futureurl ="http://www.incois.gov.in/website/futureht/default.htm";
		var futureurl ="http://www.incois.gov.in/website/argo_india/default.htm";
			var params = "status=yes,toolbar=no,scrollbars=yes,resizable=yes,menubar=no,top=0,left=0,width="+ screen.width +", height= "+ (screen.height * 0.9) + ",screenX=100%, screenY=100%";
			
			var winGisHV = window.open(futureurl,'Incois',params);
			winGisHV.focus();
		//}
		/*else
		{
			var futureurl ="http://www.incois.gov.in/website/futuredep/ie.htm";
			var params = "toolbar=no,scrollbars=yes,resizable=yes,menubar=no,top=0,left=0,width="+ screen.width +", height= "+ (screen.height * 0.9) + ",screenX=100%, screenY=100%";

			var winGisJV = window.open(futureurl,'Incois',params);
			
			//var winGisHV = window.open(argourl,'Floats' ,'toolbar=no, status=yes, menubar=no,scrollbars=yes,resizable=yes, fullsize=yes,top=0, left=0, width='+ screen.width +', height=' + (screen.height * 0.9) +', screenX=100%, screenY=100% ');
			winGisJV.focus();		
		}*/
		
	}



</script>
<!--
</head>
</html>
-->