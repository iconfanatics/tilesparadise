document.addEventListener('click', function(e) {
  const btn = e.target.closest('.custom-tab-btn');
  if (!btn) return;
  
  const section = btn.closest('.custom-tabs-section');
  if (!section) return;
  
  const index = btn.getAttribute('data-index');
  
  const btns = section.querySelectorAll('.custom-tab-btn');
  const contents = section.querySelectorAll('.custom-tab-content');
  
  btns.forEach(b => b.classList.remove('active'));
  contents.forEach(c => c.classList.remove('active'));
  
  btn.classList.add('active');
  const targetContent = section.querySelector(`.custom-tab-content[data-index="${index}"]`);
  if(targetContent) {
    targetContent.classList.add('active');
  }
});
