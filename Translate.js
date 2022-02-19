var allText = '';
function t(s)
{
    allText = '';
	var arr = s.split(`\n`);
	var res = arr.join(' ');

	const copyToClipboard = str => {
	  const el = document.createElement('textarea');
	  el.value = str;
	  document.body.appendChild(el);
	  el.select();
	  document.execCommand('copy');
	  document.body.removeChild(el);
	};	
    allText += res + `

`;
 copyToClipboard(allText);
}
