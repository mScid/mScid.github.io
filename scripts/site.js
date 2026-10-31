// Progressive enhancement for code blocks retained from the original pages.
document.querySelectorAll('.highlight-wrapper').forEach((wrapper) => {
  const button = wrapper.querySelector('.js-btn-copy-code');
  const code = wrapper.querySelector('.highlight');
  if (!button || !code) return;
  button.classList.remove('hide');
  button.setAttribute('aria-live', 'polite');
  const lines = [...code.querySelectorAll('.cl')];
  const text = lines.length ? lines.map(line => line.textContent).join('') : code.textContent;
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(text);
      button.textContent = 'Copied!';
    } catch {
      // Keep the code selectable when clipboard permissions are unavailable.
      const range = document.createRange();
      range.selectNodeContents(code);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      button.textContent = 'Select and copy';
    }
    setTimeout(() => { button.textContent = 'Copy'; }, 2000);
  });
});
