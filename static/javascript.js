function invokeCmd(param) {
  var http = new XMLHttpRequest();
  http.open("GET", "{{ url_for('runcmd') }}" + param, true);
  
  http.send(null);
  http.send(null);
  http.onreadystatechange = function()
{
   if(this.readyState == 4 && this.status == 200) 
     {
     document.getElementById('freq').value = this.responseText;  
     }  
}
http.open("GET", "{{ url_for('runcmd') }}" + param, true);
http.send(null);
}
