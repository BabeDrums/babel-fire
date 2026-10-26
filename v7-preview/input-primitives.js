/* G7 shared text-input primitives
   Owns generic text-entry assistance without changing specialized numeric/input-mode controls.

   Legacy fixture markup may still carry restrictive attributes. Normalize ordinary `.field`
   text inputs as soon as a sheet renders so iOS/Safari can provide its normal predictive,
   correction, and spelling assistance while the app keeps its explicit capitalization and
   Enter-key progression behavior.
*/

const sheetRoot = document.getElementById("sheetRoot");

function enableTextAssistance(root = sheetRoot) {
  if (!root) return;
  root.querySelectorAll('input.field:not([inputmode])').forEach((input) => {
    input.removeAttribute("autocomplete");
    input.setAttribute("autocorrect", "on");
    input.setAttribute("spellcheck", "true");
  });
}

if (sheetRoot) {
  enableTextAssistance();
  new MutationObserver(() => enableTextAssistance()).observe(sheetRoot, {
    childList: true,
    subtree: true,
  });
}
