f='/home/konerleonard/.openclaw/workspace/kdp-j/docs/index.html'
h=open(f).read()
old="function start(){grid=emptyGrid();score=0;lines=0;level=1;dropMs=800;acc=0;last=0;over=false;paused=false;started=true;softHold=false;holdAcc=0;cur=spawn(randShape());next=spawn(randShape());updateStats();drawNext();draw();document.getElementById('overlay').style.display='none';cancelAnimationFrame(raf);raf=requestAnimationFrame(loop);}"
new="function start(){try{var eb=document.getElementById('errbox');if(eb)eb.textContent+=' START';}catch(e){}grid=emptyGrid();score=0;lines=0;level=1;dropMs=800;acc=0;last=0;over=false;paused=false;started=true;softHold=false;holdAcc=0;cur=spawn(randShape());next=spawn(randShape());updateStats();drawNext();draw();var ov=document.getElementById('overlay');if(ov)ov.style.display='none';try{var eb2=document.getElementById('errbox');if(eb2)eb2.textContent+=' started='+started+' cur='+(cur?cur.s:'null')+' ov='+(ov?ov.style.display:'na');}catch(e){}cancelAnimationFrame(raf);raf=requestAnimationFrame(loop);}"
if old in h:\n    h=h.replace(old,new)\n    open(f,'w').write(h)\n    print("patched")
else:
    print("START not found")
