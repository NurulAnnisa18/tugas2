<!DOCTYPE html>
<!-- saved from url=(0095)https://colab.research.google.com/drive/1CUMTCVRW9nOVHMuuwKrgU3artqtnwy6v#scrollTo=mKGBJ5aE778h -->
<html lang="id" theme="dark" editor="Default Dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><script type="text/javascript" async="" charset="utf-8" src="./class_Restoran.ipynb - Colab_files/recaptcha__id.js.download" crossorigin="anonymous" integrity="sha384-Q2vCH+kRnM1/kscuawcISlvR5DnrBbxS3g/fdt0cVmergJ1zVQdsNOWFHrJBozbZ" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./class_Restoran.ipynb - Colab_files/recaptcha__id.js.download" crossorigin="anonymous" integrity="sha384-Q2vCH+kRnM1/kscuawcISlvR5DnrBbxS3g/fdt0cVmergJ1zVQdsNOWFHrJBozbZ" nonce=""></script><script src="./class_Restoran.ipynb - Colab_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./class_Restoran.ipynb - Colab_files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="https://www.google-analytics.com/analytics.js"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>class_Restoran.ipynb - Colab</title><style type="text/css">:root, :host {
  --fa-font-solid: normal 900 1em/1 "Font Awesome 6 Free";
  --fa-font-regular: normal 400 1em/1 "Font Awesome 6 Free";
  --fa-font-light: normal 300 1em/1 "Font Awesome 6 Pro";
  --fa-font-thin: normal 100 1em/1 "Font Awesome 6 Pro";
  --fa-font-duotone: normal 900 1em/1 "Font Awesome 6 Duotone";
  --fa-font-brands: normal 400 1em/1 "Font Awesome 6 Brands";
  --fa-font-sharp-solid: normal 900 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-regular: normal 400 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-light: normal 300 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-thin: normal 100 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-duotone-solid: normal 900 1em/1 "Font Awesome 6 Sharp Duotone";
}

svg:not(:root).svg-inline--fa, svg:not(:host).svg-inline--fa {
  overflow: visible;
  box-sizing: content-box;
}

.svg-inline--fa {
  display: var(--fa-display, inline-block);
  height: 1em;
  overflow: visible;
  vertical-align: -0.125em;
}
.svg-inline--fa.fa-2xs {
  vertical-align: 0.1em;
}
.svg-inline--fa.fa-xs {
  vertical-align: 0em;
}
.svg-inline--fa.fa-sm {
  vertical-align: -0.0714285705em;
}
.svg-inline--fa.fa-lg {
  vertical-align: -0.2em;
}
.svg-inline--fa.fa-xl {
  vertical-align: -0.25em;
}
.svg-inline--fa.fa-2xl {
  vertical-align: -0.3125em;
}
.svg-inline--fa.fa-pull-left {
  margin-right: var(--fa-pull-margin, 0.3em);
  width: auto;
}
.svg-inline--fa.fa-pull-right {
  margin-left: var(--fa-pull-margin, 0.3em);
  width: auto;
}
.svg-inline--fa.fa-li {
  width: var(--fa-li-width, 2em);
  top: 0.25em;
}
.svg-inline--fa.fa-fw {
  width: var(--fa-fw-width, 1.25em);
}

.fa-layers svg.svg-inline--fa {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
}

.fa-layers-counter, .fa-layers-text {
  display: inline-block;
  position: absolute;
  text-align: center;
}

.fa-layers {
  display: inline-block;
  height: 1em;
  position: relative;
  text-align: center;
  vertical-align: -0.125em;
  width: 1em;
}
.fa-layers svg.svg-inline--fa {
  transform-origin: center center;
}

.fa-layers-text {
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  transform-origin: center center;
}

.fa-layers-counter {
  background-color: var(--fa-counter-background-color, #ff253a);
  border-radius: var(--fa-counter-border-radius, 1em);
  box-sizing: border-box;
  color: var(--fa-inverse, #fff);
  line-height: var(--fa-counter-line-height, 1);
  max-width: var(--fa-counter-max-width, 5em);
  min-width: var(--fa-counter-min-width, 1.5em);
  overflow: hidden;
  padding: var(--fa-counter-padding, 0.25em 0.5em);
  right: var(--fa-right, 0);
  text-overflow: ellipsis;
  top: var(--fa-top, 0);
  transform: scale(var(--fa-counter-scale, 0.25));
  transform-origin: top right;
}

.fa-layers-bottom-right {
  bottom: var(--fa-bottom, 0);
  right: var(--fa-right, 0);
  top: auto;
  transform: scale(var(--fa-layers-scale, 0.25));
  transform-origin: bottom right;
}

.fa-layers-bottom-left {
  bottom: var(--fa-bottom, 0);
  left: var(--fa-left, 0);
  right: auto;
  top: auto;
  transform: scale(var(--fa-layers-scale, 0.25));
  transform-origin: bottom left;
}

.fa-layers-top-right {
  top: var(--fa-top, 0);
  right: var(--fa-right, 0);
  transform: scale(var(--fa-layers-scale, 0.25));
  transform-origin: top right;
}

.fa-layers-top-left {
  left: var(--fa-left, 0);
  right: auto;
  top: var(--fa-top, 0);
  transform: scale(var(--fa-layers-scale, 0.25));
  transform-origin: top left;
}

.fa-1x {
  font-size: 1em;
}

.fa-2x {
  font-size: 2em;
}

.fa-3x {
  font-size: 3em;
}

.fa-4x {
  font-size: 4em;
}

.fa-5x {
  font-size: 5em;
}

.fa-6x {
  font-size: 6em;
}

.fa-7x {
  font-size: 7em;
}

.fa-8x {
  font-size: 8em;
}

.fa-9x {
  font-size: 9em;
}

.fa-10x {
  font-size: 10em;
}

.fa-2xs {
  font-size: 0.625em;
  line-height: 0.1em;
  vertical-align: 0.225em;
}

.fa-xs {
  font-size: 0.75em;
  line-height: 0.0833333337em;
  vertical-align: 0.125em;
}

.fa-sm {
  font-size: 0.875em;
  line-height: 0.0714285718em;
  vertical-align: 0.0535714295em;
}

.fa-lg {
  font-size: 1.25em;
  line-height: 0.05em;
  vertical-align: -0.075em;
}

.fa-xl {
  font-size: 1.5em;
  line-height: 0.0416666682em;
  vertical-align: -0.125em;
}

.fa-2xl {
  font-size: 2em;
  line-height: 0.03125em;
  vertical-align: -0.1875em;
}

.fa-fw {
  text-align: center;
  width: 1.25em;
}

.fa-ul {
  list-style-type: none;
  margin-left: var(--fa-li-margin, 2.5em);
  padding-left: 0;
}
.fa-ul > li {
  position: relative;
}

.fa-li {
  left: calc(-1 * var(--fa-li-width, 2em));
  position: absolute;
  text-align: center;
  width: var(--fa-li-width, 2em);
  line-height: inherit;
}

.fa-border {
  border-color: var(--fa-border-color, #eee);
  border-radius: var(--fa-border-radius, 0.1em);
  border-style: var(--fa-border-style, solid);
  border-width: var(--fa-border-width, 0.08em);
  padding: var(--fa-border-padding, 0.2em 0.25em 0.15em);
}

.fa-pull-left {
  float: left;
  margin-right: var(--fa-pull-margin, 0.3em);
}

.fa-pull-right {
  float: right;
  margin-left: var(--fa-pull-margin, 0.3em);
}

.fa-beat {
  animation-name: fa-beat;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, ease-in-out);
}

.fa-bounce {
  animation-name: fa-bounce;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.28, 0.84, 0.42, 1));
}

.fa-fade {
  animation-name: fa-fade;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
}

.fa-beat-fade {
  animation-name: fa-beat-fade;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
}

.fa-flip {
  animation-name: fa-flip;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, ease-in-out);
}

.fa-shake {
  animation-name: fa-shake;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, linear);
}

.fa-spin {
  animation-name: fa-spin;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 2s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, linear);
}

.fa-spin-reverse {
  --fa-animation-direction: reverse;
}

.fa-pulse,
.fa-spin-pulse {
  animation-name: fa-spin;
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, steps(8));
}

@media (prefers-reduced-motion: reduce) {
  .fa-beat,
.fa-bounce,
.fa-fade,
.fa-beat-fade,
.fa-flip,
.fa-pulse,
.fa-shake,
.fa-spin,
.fa-spin-pulse {
    animation-delay: -1ms;
    animation-duration: 1ms;
    animation-iteration-count: 1;
    transition-delay: 0s;
    transition-duration: 0s;
  }
}
@keyframes fa-beat {
  0%, 90% {
    transform: scale(1);
  }
  45% {
    transform: scale(var(--fa-beat-scale, 1.25));
  }
}
@keyframes fa-bounce {
  0% {
    transform: scale(1, 1) translateY(0);
  }
  10% {
    transform: scale(var(--fa-bounce-start-scale-x, 1.1), var(--fa-bounce-start-scale-y, 0.9)) translateY(0);
  }
  30% {
    transform: scale(var(--fa-bounce-jump-scale-x, 0.9), var(--fa-bounce-jump-scale-y, 1.1)) translateY(var(--fa-bounce-height, -0.5em));
  }
  50% {
    transform: scale(var(--fa-bounce-land-scale-x, 1.05), var(--fa-bounce-land-scale-y, 0.95)) translateY(0);
  }
  57% {
    transform: scale(1, 1) translateY(var(--fa-bounce-rebound, -0.125em));
  }
  64% {
    transform: scale(1, 1) translateY(0);
  }
  100% {
    transform: scale(1, 1) translateY(0);
  }
}
@keyframes fa-fade {
  50% {
    opacity: var(--fa-fade-opacity, 0.4);
  }
}
@keyframes fa-beat-fade {
  0%, 100% {
    opacity: var(--fa-beat-fade-opacity, 0.4);
    transform: scale(1);
  }
  50% {
    opacity: 1;
    transform: scale(var(--fa-beat-fade-scale, 1.125));
  }
}
@keyframes fa-flip {
  50% {
    transform: rotate3d(var(--fa-flip-x, 0), var(--fa-flip-y, 1), var(--fa-flip-z, 0), var(--fa-flip-angle, -180deg));
  }
}
@keyframes fa-shake {
  0% {
    transform: rotate(-15deg);
  }
  4% {
    transform: rotate(15deg);
  }
  8%, 24% {
    transform: rotate(-18deg);
  }
  12%, 28% {
    transform: rotate(18deg);
  }
  16% {
    transform: rotate(-22deg);
  }
  20% {
    transform: rotate(22deg);
  }
  32% {
    transform: rotate(-12deg);
  }
  36% {
    transform: rotate(12deg);
  }
  40%, 100% {
    transform: rotate(0deg);
  }
}
@keyframes fa-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.fa-rotate-90 {
  transform: rotate(90deg);
}

.fa-rotate-180 {
  transform: rotate(180deg);
}

.fa-rotate-270 {
  transform: rotate(270deg);
}

.fa-flip-horizontal {
  transform: scale(-1, 1);
}

.fa-flip-vertical {
  transform: scale(1, -1);
}

.fa-flip-both,
.fa-flip-horizontal.fa-flip-vertical {
  transform: scale(-1, -1);
}

.fa-rotate-by {
  transform: rotate(var(--fa-rotate-angle, 0));
}

.fa-stack {
  display: inline-block;
  vertical-align: middle;
  height: 2em;
  position: relative;
  width: 2.5em;
}

.fa-stack-1x,
.fa-stack-2x {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
  z-index: var(--fa-stack-z-index, auto);
}

.svg-inline--fa.fa-stack-1x {
  height: 1em;
  width: 1.25em;
}
.svg-inline--fa.fa-stack-2x {
  height: 2em;
  width: 2.5em;
}

.fa-inverse {
  color: var(--fa-inverse, #fff);
}

.sr-only,
.fa-sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.sr-only-focusable:not(:focus),
.fa-sr-only-focusable:not(:focus) {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.svg-inline--fa .fa-primary {
  fill: var(--fa-primary-color, currentColor);
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa .fa-secondary {
  fill: var(--fa-secondary-color, currentColor);
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-primary {
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-secondary {
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa mask .fa-primary,
.svg-inline--fa mask .fa-secondary {
  fill: black;
}

.fad.fa-inverse,
.fa-duotone.fa-inverse {
  color: var(--fa-inverse, #fff);
}</style><link href="./class_Restoran.ipynb - Colab_files/css2" rel="stylesheet"><link href="./class_Restoran.ipynb - Colab_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_2d{font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Qa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_Qa:hover::after,a.gb_Qa:focus::after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Qa:hover,a.gb_Qa:focus{text-decoration:none}a.gb_Qa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Ra{background-color:#4285f4;color:#fff}a.gb_Ra:active{background-color:#0043b2}.gb_Sa{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Qa,.gb_Ra,.gb_Ta,.gb_Ua{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Ta{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ua{background:#f8f8f8}.gb_Ta,#gb a.gb_Ta.gb_Ta,.gb_Ua{color:#666;cursor:default;text-decoration:none}#gb a.gb_Ua{cursor:default;text-decoration:none}.gb_Ua{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Ua{color:#fff}.gb_Ua:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ua:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_Va{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Va:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Va:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Va:active,#gb .gb_Va:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Va.gb_H{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Va.gb_H:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Va.gb_H:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Va.gb_H:active,#gb .gb_Va.gb_H:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_cd{display:inline-block;vertical-align:middle}.gb_Ne .gb_Q{bottom:-3px;right:-5px}.gb_D{position:relative}.gb_B{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_B{cursor:pointer;text-decoration:none}.gb_B,a.gb_B{color:#000}.gb_dd{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_ed{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_ed{border-bottom-color:#ccc}.gb_la{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_cd.gb_Tc .gb_dd,.gb_cd.gb_Tc .gb_ed,.gb_cd.gb_Tc .gb_la,.gb_Tc.gb_la{display:block}.gb_cd.gb_Tc.gb_fd .gb_dd,.gb_cd.gb_Tc.gb_fd .gb_ed{display:none}.gb_Oe{position:absolute;right:8px;top:62px;z-index:-1}.gb_gd .gb_dd,.gb_gd .gb_ed,.gb_gd .gb_la{margin-top:-10px}.gb_cd:first-child,#gbsfw:first-child+.gb_cd{padding-left:4px}.gb_Fa.gb_Pe .gb_cd:first-child{padding-left:0}.gb_Qe{position:relative}.gb_2c .gb_Qe,.gb_Jd .gb_Qe{float:right}.gb_B{padding:8px;cursor:pointer}.gb_B::after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Fa .gb_hd:not(.gb_Qa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_id button svg,.gb_B{-webkit-border-radius:50%;border-radius:50%}.gb_id button:focus:not(:focus-visible) svg,.gb_id button:hover svg,.gb_id button:active svg,.gb_B:focus:not(:focus-visible),.gb_B:hover,.gb_B:active,.gb_B[aria-expanded=true]{outline:none}.gb_Lc .gb_id.gb_jd button:focus-visible svg,.gb_id button:focus-visible svg,.gb_B:focus-visible{outline:1px solid #202124}.gb_Lc .gb_id button:focus-visible svg,.gb_Lc .gb_B:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Lc .gb_id.gb_jd button:focus-visible svg,.gb_id button:focus-visible svg,.gb_Lc .gb_id button:focus-visible svg{outline:1px solid currentcolor}}.gb_Lc .gb_id.gb_jd button:focus svg,.gb_Lc .gb_id.gb_jd button:focus:hover svg,.gb_id button:focus svg,.gb_id button:focus:hover svg,.gb_B:focus,.gb_B:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Lc .gb_id.gb_jd button:active svg,.gb_id button:active svg,.gb_B:active{background-color:rgba(60,64,67,.12)}.gb_Lc .gb_id.gb_jd button:hover svg,.gb_id button:hover svg,.gb_B:hover{background-color:rgba(60,64,67,.08)}.gb_Wa .gb_B.gb_Za:hover{background-color:transparent}.gb_B[aria-expanded=true],.gb_B:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_B[aria-expanded=true] .gb_F{fill:#5f6368;opacity:1}.gb_Lc .gb_id button:hover svg,.gb_Lc .gb_B:hover{background-color:rgba(232,234,237,.08)}.gb_Lc .gb_id button:focus svg,.gb_Lc .gb_id button:focus:hover svg,.gb_Lc .gb_B:focus,.gb_Lc .gb_B:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Lc .gb_id button:active svg,.gb_Lc .gb_B:active{background-color:rgba(232,234,237,.12)}.gb_Lc .gb_B[aria-expanded=true],.gb_Lc .gb_B:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Lc .gb_B[aria-expanded=true] .gb_F{fill:#fff;opacity:1}.gb_cd{padding:4px}.gb_Fa.gb_Pe .gb_cd{padding:4px 2px}.gb_Fa.gb_Pe .gb_z.gb_cd{padding-left:6px}.gb_la{z-index:991;line-height:normal}.gb_la.gb_kd{left:0;right:auto}@media (max-width:350px){.gb_la.gb_kd{left:0}}.gb_Re .gb_la{top:56px}.gb_R{display:none!important}.gb_nd{visibility:hidden}.gb_J .gb_B,.gb_ka .gb_J .gb_B{background-position:-64px -29px}.gb_1 .gb_J .gb_B{background-position:-29px -29px;opacity:1}.gb_J .gb_B,.gb_J .gb_B:hover,.gb_J .gb_B:focus{opacity:1}.gb_L{display:none}@media screen and (max-width:319px){.gb_ld:not(.gb_md) .gb_J{display:none;visibility:hidden}}.gb_Q{display:none}.gb_9c{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_9c.gb_ad{color:#3c4043}.gb_Fa.gb_cc .gb_9c{margin-bottom:0}.gb_sd.gb_ud .gb_9c{padding-left:4px}.gb_Fa.gb_cc .gb_vd{position:relative;top:-2px}.gb_bd{display:none}.gb_Fa{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Fa.gb_Sc{min-width:120px}.gb_Fa.gb_wd .gb_xd{display:none}.gb_Fa.gb_wd .gb_ld{height:56px}header.gb_Fa{display:block}.gb_Fa svg{fill:currentColor}.gb_Dd{position:fixed;top:0;width:100%}.gb_yd{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Ed{height:64px}.gb_ld{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Fa:not(.gb_cc) .gb_ld{padding:8px}.gb_Fa.gb_Fd .gb_ld{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa .gb_ld.gb_md.gb_Hd{min-width:0}.gb_Fa.gb_cc .gb_ld{padding:4px;padding-left:8px;min-width:0}.gb_xd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_Ad>.gb_xd{display:table-cell;width:100%}.gb_sd{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa.gb_cc .gb_sd{padding-right:14px}.gb_Bd{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_Bd>:only-child{display:inline-block}.gb_Cd.gb_3c{padding-left:4px}.gb_Cd.gb_Id,.gb_Fa.gb_Fd .gb_Cd,.gb_Fa.gb_cc:not(.gb_Jd) .gb_Cd{padding-left:0}.gb_Fa.gb_cc .gb_Cd.gb_Id{padding-right:0}.gb_Fa.gb_cc .gb_Cd.gb_Id .gb_Wa{margin-left:10px}.gb_3c{display:inline}.gb_Fa.gb_Wc .gb_Cd.gb_Kd,.gb_Fa.gb_Jd .gb_Cd.gb_Kd{padding-left:2px}.gb_9c{display:inline-block}.gb_Cd{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Jd{height:48px}.gb_Fa.gb_Jd{min-width:auto}.gb_Jd .gb_Cd{float:right;padding-left:32px}.gb_Jd .gb_Cd.gb_Ld{padding-left:0}.gb_Md{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_pd{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Nd{color:black}.gb_Lc{color:white}.gb_Fa a,.gb_Pc a{color:inherit}.gb_ba{color:rgba(0,0,0,.87)}.gb_Fa svg,.gb_Pc svg,.gb_sd .gb_td,.gb_2c .gb_td{color:#5f6368;opacity:1}.gb_Lc svg,.gb_Pc.gb_Uc svg,.gb_Lc .gb_sd .gb_td,.gb_Lc .gb_sd .gb_Kc,.gb_Lc .gb_sd .gb_vd,.gb_Pc.gb_Uc .gb_td{color:rgba(255,255,255,.87)}.gb_Lc .gb_sd .gb_Od:not(.gb_Pd){opacity:.87}.gb_ad{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Lc .gb_ad,.gb_Nd .gb_ad{opacity:1}.gb_Qd{position:relative}.gb_M{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_X,span.gb_X{color:rgba(0,0,0,.87);text-decoration:none}.gb_Lc a.gb_X,.gb_Lc span.gb_X{color:white}a.gb_X:focus{outline-offset:2px}a.gb_X:hover{text-decoration:underline}.gb_Z{display:inline-block;padding-left:15px}.gb_Z .gb_X{display:inline-block;line-height:24px;vertical-align:middle}.gb_qd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Fa.gb_Jd .gb_qd{margin-left:8px}#gb a.gb_Ua.gb_qd{cursor:pointer}.gb_Ua.gb_qd:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_qd:focus,.gb_Ua.gb_qd:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_qd:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_qd{background:#1a73e8;border:1px solid transparent}.gb_Fa.gb_cc .gb_qd{padding:9px 15px;min-width:80px}.gb_Rd{text-align:left}#gb .gb_Lc a.gb_qd:not(.gb_H),#gb.gb_Lc a.gb_qd{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_Ua.gb_H.gb_qd{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Lc a.gb_qd:hover:not(.gb_H),#gb.gb_Lc a.gb_qd:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ua.gb_H.gb_qd:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Lc a.gb_qd:focus:not(.gb_H),#gb .gb_Lc a.gb_qd:focus:hover:not(.gb_H),#gb.gb_Lc a.gb_qd:focus:not(.gb_H),#gb.gb_Lc a.gb_qd:focus:hover:not(.gb_H){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ua.gb_H.gb_qd:focus,#gb a.gb_Ua.gb_H.gb_qd:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Lc a.gb_qd:active:not(.gb_H),#gb.gb_Lc a.gb_qd:active{background:#ecf3fe}#gb a.gb_Ua.gb_H.gb_qd:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_K{display:none}@media screen and (max-width:319px){.gb_ld .gb_J{display:none;visibility:hidden}}.gb_Wa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Wa.gb_H{background-color:transparent;border:1px solid #5f6368}.gb_3a{display:inherit}.gb_Wa.gb_H .gb_3a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Wa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Wa.gb_H:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Wa:focus-visible,.gb_Wa:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Wa.gb_H:focus-visible,.gb_Wa.gb_H:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Wa.gb_H:active,.gb_Wa.gb_Tc.gb_H:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_4a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Wa.gb_H .gb_4a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_4a.gb_5a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_4a.gb_5a .gb_Ic{vertical-align:middle}.gb_Fa:not(.gb_cc) .gb_Wa{margin-left:10px;margin-right:4px}.gb_Sd{max-height:32px;width:78px}.gb_Wa.gb_H .gb_Sd{max-height:26px;width:72px}.gb_P{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_eb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_eb.gb_P{height:30px;width:30px}.gb_eb.gb_P:hover,.gb_eb.gb_P:active{-webkit-box-shadow:none;box-shadow:none}.gb_fb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_wc{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_P::before,.gb_gb::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_3 .gb_gb::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_P:hover,.gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_P:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_P:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_hb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_B.gb_hb{width:auto}.gb_hb:hover,.gb_hb:focus{opacity:.85}.gb_gd .gb_hb,.gb_gd .gb_Ud{line-height:26px}#gb#gb.gb_gd a.gb_hb,.gb_gd .gb_Ud{font-size:11px;height:auto}.gb_ib{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Za:hover .gb_ib{opacity:.85}.gb_Wa>.gb_z{padding:3px 3px 3px 4px}.gb_Vd.gb_nd{color:#fff}.gb_1 .gb_hb,.gb_1 .gb_ib{opacity:1}#gb#gb.gb_1.gb_1 a.gb_hb,#gb#gb .gb_1.gb_1 a.gb_hb{color:#fff}.gb_1.gb_1 .gb_ib{border-top-color:#fff;opacity:1}.gb_ka .gb_P:hover,.gb_1 .gb_P:hover,.gb_ka .gb_P:focus,.gb_1 .gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_Wd .gb_z,.gb_Xd .gb_z{position:absolute;right:1px}.gb_z.gb_0,.gb_jb.gb_0,.gb_Za.gb_0{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_Zd.gb_0d .gb_hb{width:30px!important}.gb_1d{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_2d .gb_1d,.gb_3d .gb_1d{right:0;top:0}.gb_z .gb_B{padding:4px}.gb_S{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.eebVy_fNKiM.2019.O","co.id","id","425",0,[4,2,"","","","735207307","0"],null,"yKXRZ5RvtJrA3g-NhZypDw",null,0,"og.qtm.sDa5bc0wD58.L.W.O","AA2YrTv9PWxAWOkNMB0THY2YxYWamdWWtA","AA2YrTucClwlLUqaQmlTybxGncrc_XS2Pg","",2,1,200,"IDN",null,null,"425","425",1,null,null,114591953,null,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","dhiyaulhaq010705@gmail.com","","AKeJmwtMpfGFg6DXTdwDmwAB3poZaALWN51GS1FIxasBJR2PoKwYwT8gMmwZLBgM5SHVNiD6oJcS9ftm_GStWQzc29unJPO4PQ",0,0,0,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Akun bisnis",1,"%1$s (terdelegasi)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=id\u0026ts=250",0,"dashboard",null,null,null,null,"Profil","",1,null,"Telah logout","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Hapus","Login",0,1,1,0,1,1,0,null,null,null,"Sesi berakhir",null,null,null,"Pengunjung",null,"Default","Terdelegasi","Logout dari semua akun",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","id"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.uiLLJjqnhCQ.O/d=1/rs=AHpOoo8NP2y291iiPDmfAN0GV3dvCuqlYA/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20250210.0_p0","id",null,0],[0.009999999776482582,"co.id","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"IDN","id","735207307.0",8,null,1,0,null,null,null,null,"3700942,102797341,102797343,102839464,102839466",null,null,null,"yKXRZ5RvtJrA3g-NhZypDw",0,0,0,null,2,5,"nn",43,0,0,0,0,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.eebVy_fNKiM.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTv9PWxAWOkNMB0THY2YxYWamdWWtA"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.sDa5bc0wD58.L.W.O/m=qcwid,qba/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTucClwlLUqaQmlTybxGncrc_XS2Pg"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?yac=1\u0026bac=1\u0026amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=id\u0026continue=https://colab.research.google.com/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Terjadi error.%1$s Muat ulang untuk mencoba lagi atau %2$spilih akun lain%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Notifikasi keamanan penting","Notifikasi akun penting","Peringatan penggunaan penyimpanan",1,1],0,1,null,1,1,1,1,null,null,0,0,0,null,0,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"id",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=id\u0026continue=https://colab.research.google.com/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=id\u0026continue=https://colab.research.google.com/\u0026timeStmp=1741792712\u0026secTok=.AG5fkS-Qm5O7mgGAdpAYse27OfPhzD5FXQ\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=id\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F\u0026ec=GAZAqQM",1,1,0,0,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,1,null,0,null,0,0,"8559284470"],0,null,null,null,1,0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ca,ka,la,qa,sa,ta,Aa,Ia,Ja,Na,Qa,Ka,Pa,Oa,Ma,La,Ra,hb,lb,ib,mb,xb,yb,zb,Ab;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.Gj=!0;return a};ca=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};
_.ea=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ha=function(){return _.fa().toLowerCase().indexOf("webkit")!=-1};_.fa=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};ka=function(a){if(!ia||!ja)return!1;for(let b=0;b<ja.brands.length;b++){const {brand:c}=ja.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};_.u=function(a){return _.fa().indexOf(a)!=-1};la=function(){return ia?!!ja&&ja.brands.length>0:!1};_.ma=function(){return la()?!1:_.u("Opera")};
_.oa=function(){return la()?!1:_.u("Trident")||_.u("MSIE")};_.pa=function(){return _.u("Firefox")||_.u("FxiOS")};_.ra=function(){return _.u("Safari")&&!(qa()||(la()?0:_.u("Coast"))||_.ma()||(la()?0:_.u("Edge"))||(la()?ka("Microsoft Edge"):_.u("Edg/"))||(la()?ka("Opera"):_.u("OPR"))||_.pa()||_.u("Silk")||_.u("Android"))};qa=function(){return la()?ka("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(la()?0:_.u("Edge"))||_.u("Silk")};sa=function(){return ia?!!ja&&!!ja.platform:!1};
ta=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.ua=function(){return ta()||_.u("iPad")||_.u("iPod")};_.va=function(){return sa()?ja.platform==="macOS":_.u("Macintosh")};_.xa=function(a,b){return _.wa(a,b)>=0};_.ya=function(a){let b="",c=0;const d=a.length-10240;for(;c<d;)b+=String.fromCharCode.apply(null,a.subarray(c,c+=10240));b+=String.fromCharCode.apply(null,c?a.subarray(c):a);return btoa(b)};_.za=function(a){return a!=null&&a instanceof Uint8Array};
Aa=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Ba=function(a){a=Error(a);Aa(a,"warning");return a};_.Da=function(a,b){if(a!=null){var c;var d=(c=Ca)!=null?c:Ca={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Aa(a,"incident"),_.ea(a))}};_.Ea=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};_.Fa=function(a,b){a[_.v]&=~b};
_.Ga=function(a){return a!==null&&typeof a==="object"&&!Array.isArray(a)&&a.constructor===Object};_.Ha=function(a){if(a&2)throw Error();};Ia=function(a){return a};Ja=function(a){return a};Na=function(a,b,c,d){return Ka(a,b,c,d,La,Ma)};Qa=function(a,b,c,d){return Ka(a,b,c,d,Oa,Pa)};
Ka=function(a,b,c,d,e,f){if(!c.length&&!d)return 1;var g=0;let h=0,k=0;var l=0;let m=0;for(var n=c.length-1;n>=0;n--){var r=c[n];d&&n===c.length-1&&r===d||(l++,r!=null&&k++)}if(d)for(var q in d)n=+q,isNaN(n)||(m+=Ra(n),h++,n>g&&(g=n));l=e(l,k)+f(h,g,m);q=k;n=h;r=g;let w=m;for(let I=c.length-1;I>=0;I--){var B=c[I];if(B==null||d&&I===c.length-1&&B===d)continue;B=I-b;const N=e(B,q)+f(n,r,w);N<l&&(a=1+B,l=N);n++;q--;w+=Ra(B);r=Math.max(r,B)}b=e(0,0)+f(n,r,w);b<l&&(a=1,l=b);if(d){n=h;r=g;w=m;q=k;for(const I in d)d=
+I,isNaN(d)||d>=1024||(n--,q++,w-=I.length,g=e(d,q)+f(n,r,w),g<l&&(a=1+d,l=g))}return a};Pa=function(a,b,c){return c+a*3+(a>1?a-1:0)};Oa=function(a,b){return(a>1?a-1:0)+(a-b)*4};Ma=function(a,b){return a==0?0:9*Math.max(1<<32-Math.clz32(a+a/2-1),4)<=b?a==0?0:a<4?100+(a-1)*16:a<6?148+(a-4)*16:a<12?244+(a-6)*16:a<22?436+(a-12)*19:a<44?820+(a-22)*17:52+32*a:40+4*b};La=function(a){return 40+4*a};Ra=function(a){return a>=100?a>=1E4?Math.ceil(Math.log10(1+a)):a<1E3?3:4:a<10?1:2};
_.Ta=function(a){if(typeof a!=="boolean")throw Error("s`"+_.Sa(a)+"`"+a);return a};_.Va=function(a){if(!(0,_.Ua)(a))throw _.Ba("enum");return a|0};_.Wa=function(a){if(typeof a!=="number")throw _.Ba("int32");if(!(0,_.Ua)(a))throw _.Ba("int32");return a|0};_.Xa=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};_.Ya=function(a){return a==null||typeof a==="string"?a:void 0};
_.$a=function(a,b,c){if(a!=null&&typeof a==="object"&&a.Ed===_.Za)return a;if(Array.isArray(a)){var d=a[_.v]|0,e=d;e===0&&(e|=c&32);e|=c&2;e!==d&&(a[_.v]=e);return new b(a)}};_.cb=function(a){const b=_.ab(_.bb);return b?a[b]:void 0};
_.fb=function(a,b,c,d,e){const f=d?!!(b&32):void 0;d=[];var g=a.length;let h,k,l,m=!1;if(b&64){if(b&256?(g--,h=a[g],k=g):(k=4294967295,h=void 0),!(e||b&512)){m=!0;var n;l=((n=db)!=null?n:Ja)(h?k- -1:b>>15&1023||536870912,-1,a,h);k=l+-1}}else k=4294967295,b&1||(h=g&&a[g-1],_.Ga(h)?(g--,k=g,l=0):h=void 0);n=void 0;for(let q=0;q<g;q++){let w=a[q];if(w!=null&&(w=c(w,f))!=null)if(q>=k){var r=void 0;((r=n)!=null?r:n={})[q- -1]=w}else d[q]=w}if(h)for(let q in h)if(r=h[q],r!=null&&(r=c(r,f))!=null)if(g=+q,
g<l)d[g+-1]=r;else{let w;((w=n)!=null?w:n={})[q]=r}n&&(m?d.push(n):d[k]=n);e&&(d[_.v]=b&33522241|(n!=null?290:34),_.ab(_.bb)&&(a=_.cb(a))&&"function"==typeof _.eb&&a instanceof _.eb&&(d[_.bb]=a.j()));return d};
hb=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.gb)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){const b=a[_.v]|0;return a.length===0&&b&1?void 0:_.fb(a,b,hb,!1,!1)}if(a.Ed===_.Za)return ib(a);if("function"==typeof _.jb&&a instanceof _.jb)return a.j();if(_.za(a))return _.za(a)&&_.Da(kb,5),_.ya(a);return}return a};lb=function(a,b){if(b){db=b===Ja||b!==Ia&&b!==Na&&b!==Qa?Ja:b;try{return ib(a)}finally{db=void 0}}return ib(a)};
ib=function(a){a=a.ha;return _.fb(a,a[_.v]|0,hb,void 0,!1)};
_.nb=function(a,b,c,d){if(a==null){var e=96;c?(a=[c],e|=512):a=[];b&&(e=e&-33521665|(b&1023)<<15)}else{if(!Array.isArray(a))throw Error("v");e=a[_.v]|0;8192&e||!(64&e)||2&e||mb();if(e&1024)throw Error("x");if(e&64)return d!==3||e&16384||(a[_.v]=e|16384),a;d===1||d===2||(e|=64);if(c&&(e|=512,c!==a[0]))throw Error("y");a:{c=a;var f=c.length;if(f){var g=f-1;const k=c[g];if(_.Ga(k)){e|=256;b=e&512?0:-1;g-=b;if(g>=1024)throw Error("A");for(var h in k)if(f=+h,f<g)c[f+b]=k[h],delete k[h];else break;e=e&
-33521665|(g&1023)<<15;break a}}if(b){h=Math.max(b,f-(e&512?0:-1));if(h>1024)throw Error("B");e=e&-33521665|(h&1023)<<15}}}d===3&&(e|=16384);a[_.v]=e;return a};mb=function(){_.Da(ob,5)};
_.pb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){const d=a[_.v]|0;if(a.length===0&&d&1)return;if(d&2)return a;var c;if(c=b)c=d===0||!!(d&32)&&!(d&64||!(d&16));return c?(a[_.v]|=34,d&4&&Object.freeze(a),a):_.fb(a,d,_.pb,b!==void 0,!0)}if(a.Ed===_.Za)return b=a.ha,c=b[_.v]|0,c&2?a:_.fb(b,c,_.pb,!0,!0);if("function"==typeof _.jb&&a instanceof _.jb)return a;if(_.za(a))return _.za(a)&&_.Da(kb,5),new Uint8Array(a)};
_.qb=function(a){const b=a.ha;if(!((b[_.v]|0)&2))return a;a=new a.constructor(_.fb(b,b[_.v]|0,_.pb,!0,!0));_.Fa(a.ha,2);return a};_.rb=function(a,b,c,d){const e=b&512?0:-1,f=c+e;var g=a.length-1;if(f>=g&&b&256)return a[g][c]=d,b;if(f<=g)return a[f]=d,b;d!==void 0&&(g=b>>15&1023||536870912,c>=g?d!=null&&(a[g+e]={[c]:d},b|=256,a[_.v]=b):a[f]=d);return b};_.tb=function(a,b,c){a=a.ha;let d=a[_.v]|0;const e=_.sb(a,d,c);b=_.$a(e,b,d);b!==e&&b!=null&&_.rb(a,d,c,b);return b};
_.ub=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.x=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.vb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.wb=function(a){for(const b in a)return!1;return!0};xb=Object.defineProperty;
yb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};zb=yb(this);Ab=function(a,b){if(b)a:{var c=zb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&xb(c,a,{configurable:!0,writable:!0,value:b})}};Ab("globalThis",function(a){return a||zb});
Ab("Symbol.dispose",function(a){return a?a:Symbol("b")});Ab("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});
Ab("Array.prototype.flat",function(a){return a?a:function(b){b=b===void 0?1:b;var c=[];Array.prototype.forEach.call(this,function(d){Array.isArray(d)&&b>0?(d=Array.prototype.flat.call(d,b-1),c.push.apply(c,d)):c.push(d)});return c}});var Cb,Gb;_.Bb=_.Bb||{};_.t=this||self;Cb=_.t._F_toggles||[];_.Db=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Sa=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Eb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Fb="closure_uid_"+(Math.random()*1E9>>>0);Gb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Gb;return _.z.apply(null,arguments)};
_.Hb=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.ab=function(a){return a};
_.C=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.yj=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.C(_.aa,Error);_.aa.prototype.name="CustomError";_.Ib=_.ba(a=>typeof a==="number");_.Jb=_.ba(a=>typeof a==="string");_.Kb=_.ba(a=>typeof a==="boolean");_.Lb=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Ob,Mb,Pb,Nb;_.gb=_.ba(a=>_.Lb?a>=Mb&&a<=Nb:a[0]==="-"?ca(a,Ob):ca(a,Pb));Ob=Number.MIN_SAFE_INTEGER.toString();Mb=_.Lb?BigInt(Number.MIN_SAFE_INTEGER):void 0;Pb=Number.MAX_SAFE_INTEGER.toString();Nb=_.Lb?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.Qb=typeof TextDecoder!=="undefined";_.Rb=typeof TextEncoder!=="undefined";var Sb=!!(Cb[0]&2048);var Tb;if(Cb[0]&1024)Tb=Sb;else{var Ub=_.Db("WIZ_global_data.oxN3nb"),Vb=Ub&&Ub[610401301];Tb=Vb!=null?Vb:!1}var ia=Tb;var ja,Wb=_.t.navigator;ja=Wb?Wb.userAgentData||null:null;_.wa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.Xb=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.Yb=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.Zb=function(a){_.Zb[" "](a);return a};_.Zb[" "]=function(){};var lc;_.$b=_.ma();_.ac=_.oa();_.bc=_.u("Edge");_.cc=_.u("Gecko")&&!(_.ha()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.dc=_.ha()&&!_.u("Edge");_.ec=_.va();_.fc=sa()?ja.platform==="Windows":_.u("Windows");_.gc=sa()?ja.platform==="Android":_.u("Android");_.hc=ta();_.ic=_.u("iPad");_.jc=_.u("iPod");_.kc=_.ua();
a:{let a="";const b=function(){const c=_.fa();if(_.cc)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.bc)return/Edge\/([\d\.]+)/.exec(c);if(_.ac)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.dc)return/WebKit\/(\S+)/.exec(c);if(_.$b)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.ac){var mc;const c=_.t.document;mc=c?c.documentMode:void 0;if(mc!=null&&mc>parseFloat(a)){lc=String(mc);break a}}lc=a}_.nc=lc;_.oc=_.pa();_.pc=ta()||_.u("iPod");_.qc=_.u("iPad");_.rc=_.u("Android")&&!(qa()||_.pa()||_.ma()||_.u("Silk"));_.sc=qa();_.tc=_.ra()&&!_.ua();var Ca=void 0;var ob,kb;_.bb=_.Ea();_.uc=_.Ea();ob=_.Ea();kb=_.Ea();_.v=_.Ea("jas",!0);var wc;_.Za={};wc=[];wc[_.v]=55;_.vc=Object.freeze(wc);_.xc=Object.freeze({});_.yc=typeof BigInt==="function"?BigInt.asIntN:void 0;_.zc=Number.isSafeInteger;_.Ua=Number.isFinite;_.Ac=Math.trunc;var db;_.Bc=function(a,b){a=a.ha;return _.sb(a,a[_.v]|0,b)};_.sb=function(a,b,c){if(c===-1)return null;const d=c+(b&512?0:-1),e=a.length-1;if(d>=e&&b&256)return a[e][c];if(d<=e)return a[d]};_.Cc=function(a,b,c){const d=a.ha;let e=d[_.v]|0;_.Ha(e);_.rb(d,e,b,c);return a};_.D=function(a,b,c){b=_.tb(a,b,c);if(b==null)return b;a=a.ha;let d=a[_.v]|0;if(!(d&2)){const e=_.qb(b);e!==b&&(b=e,_.rb(a,d,c,b))}return b};_.E=function(a,b,c){c==null&&(c=void 0);return _.Cc(a,b,c)};
_.F=function(a,b){a=_.Bc(a,b);return a==null||typeof a==="boolean"?a:typeof a==="number"?!!a:void 0};_.G=function(a,b){return _.Ya(_.Bc(a,b))};_.H=function(a,b){let c;return(c=_.F(a,b))!=null?c:!1};_.J=function(a,b){let c;return(c=_.G(a,b))!=null?c:""};_.K=function(a,b,c){return _.Cc(a,b,c==null?c:_.Ta(c))};_.L=function(a,b,c){return _.Cc(a,b,c==null?c:_.Wa(c))};_.M=function(a,b,c){return _.Cc(a,b,_.Xa(c))};_.O=function(a,b,c){return _.Cc(a,b,c==null?c:_.Va(c))};_.P=class{constructor(a,b,c){this.ha=_.nb(a,b,c,3)}toJSON(){return lb(this)}ya(a){return JSON.stringify(lb(this,a))}qc(){return!!((this.ha[_.v]|0)&2)}};_.P.prototype.Ed=_.Za;_.P.prototype.toString=function(){return this.ha.toString()};_.Dc=_.ub();_.Ec=_.ub();_.Fc=_.ub();_.Gc=Symbol();var Jc=class extends _.P{constructor(a){super(a)}};_.Kc=class extends _.P{constructor(a){super(a)}D(a){return _.L(this,3,a)}};var Lc=class extends _.P{constructor(a){super(a)}Ic(a){return _.M(this,24,a)}};_.Mc=class extends _.P{constructor(a){super(a)}};_.Q=function(){this.qa=this.qa;this.Y=this.Y};_.Q.prototype.qa=!1;_.Q.prototype.isDisposed=function(){return this.qa};_.Q.prototype.dispose=function(){this.qa||(this.qa=!0,this.P())};_.Q.prototype[Symbol.dispose]=function(){this.dispose()};_.Q.prototype.P=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Nc=class extends _.Q{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}ob(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].ob(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Pc=class extends _.Q{constructor(){var a=_.Oc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Qc=class extends _.P{constructor(a){super(a)}};var Rc=class extends _.P{constructor(a){super(a)}};var Tc;_.Sc=function(a,b,c=98,d=new _.Kc){if(a.i){const e=new Jc;_.M(e,1,b.message);_.M(e,2,b.stack);_.L(e,3,b.lineNumber);_.O(e,5,1);_.E(d,40,e);a.i.log(c,d)}};Tc=class{constructor(){this.i=null}log(a,b,c=new _.Kc){_.Sc(this,a,98,c)}};var Uc,Vc;Uc=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.Xb(c,b,a)}catch(d){console.error(d)}}}};_.Wc=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new Vc(a,b,c));Uc(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("F");this.i=a;Uc(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("F");this.j=a;Uc(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
Vc=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.Xc=a=>{var b="lc";if(a.lc&&a.hasOwnProperty(b))return a.lc;b=new a;return a.lc=b};_.R=class{constructor(){this.v=new _.Wc;this.i=new _.Wc;this.D=new _.Wc;this.B=new _.Wc;this.C=new _.Wc;this.A=new _.Wc;this.o=new _.Wc;this.j=new _.Wc;this.F=new _.Wc}Y(){return this.v}M(){return this.i}N(){return this.D}L(){return this.B}qa(){return this.C}K(){return this.A}J(){return this.o}G(){return this.j}static i(){return _.Xc(_.R)}};var ad;_.Zc=function(){return _.D(_.Yc,Lc,1)};_.$c=function(){return _.D(_.Yc,_.Mc,5)};ad=class extends _.P{constructor(a){super(a)}};var bd;window.gbar_&&window.gbar_.CONFIG?bd=window.gbar_.CONFIG[0]||{}:bd=[];_.Yc=new ad(bd);_.D(_.Yc,Rc,3)||new Rc;_.Zc()||new Lc;_.Oc=new Tc;_.A("gbar_._DumpException",function(a){_.Oc?_.Oc.log(a):console.error(a)});_.cd=new Pc;var ed;_.fd=function(a,b){var c=_.dd.i();if(a in c.i){if(c.i[a]!=b)throw new ed;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.wb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.dd=class{constructor(){this.i={};this.j={}}static i(){return _.Xc(_.dd)}};_.gd=class extends _.aa{constructor(){super()}};ed=class extends _.gd{};_.A("gbar.A",_.Wc);_.Wc.prototype.aa=_.Wc.prototype.then;_.A("gbar.B",_.R);_.R.prototype.ba=_.R.prototype.M;_.R.prototype.bb=_.R.prototype.N;_.R.prototype.bd=_.R.prototype.qa;_.R.prototype.bf=_.R.prototype.Y;_.R.prototype.bg=_.R.prototype.L;_.R.prototype.bh=_.R.prototype.K;_.R.prototype.bj=_.R.prototype.J;_.R.prototype.bk=_.R.prototype.G;_.A("gbar.a",_.R.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var hd=new Nc;_.fd("api",hd);var id=_.$c()||new _.Mc;window.__PVT=_.y(_.G(id,8));
_.fd("eq",_.cd);
}catch(e){_._DumpException(e)}
try{
_.jd=class extends _.P{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var kd=class extends _.P{constructor(a){super(a)}};var ld=class extends _.Q{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.G(a,1));_.F(a,12)!=null&&(d.dpo=_.x(_.H(a,12)));d.ms=_.y(_.G(a,2));d.m=_.y(_.G(a,3));d.l=[];_.J(b,1)&&(a=_.G(b,3))&&this.i.push(a);_.J(c,1)&&(c=_.G(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var md=_.D(_.Yc,_.Qc,14);if(md){var nd=_.D(_.Yc,_.jd,9)||new _.jd,od=new kd,pd=new ld;pd.init(md,nd,od);_.fd("gs",pd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_dhiyaulhaq010705@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./class_Restoran.ipynb - Colab_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20250310-060129_RC00_735288242'; var colabScsVersion = '95405dac7bc91085246f91af064fab09'; var hl = 'id'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_prompt_cell\x22: false, \x22agent_scroll_delay_ms\x22: 200, \x22ai_banner\x22: false, \x22ai_unsubscribed_warning\x22: false, \x22ai_user_input_char_limit\x22: 2000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22\x22, \x22aida_generate_code_model_id\x22: \x22\x22, \x22allow_dsa_page_interaction\x22: true, \x22allow_readonly_cells\x22: true, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22auto_open_chat_on_empty_notebook\x22: false, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22cell_markdown_toolbar_tooltips\x22: true, \x22cell_output_actions_tooltip\x22: true, \x22cell_tags\x22: false, \x22cell_toolbar_ai_menu\x22: true, \x22cell_toolbar_tooltips\x22: true, \x22cell_ui_refresh\x22: false, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22chat_reduce_refusals\x22: true, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_text_compose\x22: true, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22code_report_millis\x22: 600000, \x22commands_in_toolbar\x22: true, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: false, \x22converse_server_side_history\x22: false, \x22converse_temp\x22: \x22\x22, \x22corp_third_party_widgets\x22: false, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22dbu\x22: \x22\x22, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: false, \x22development\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: true, \x22dsa_sample_datasets_toast\x22: true, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_completions_backend_switching\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_rt_on_create\x22: false, \x22execution_announcements\x22: true, \x22execution_status_propagation\x22: true, \x22explain_cell\x22: true, \x22explain_error\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22filter_repetitive_suggestions\x22: false, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_name_errors\x22: false, \x22generate_temp\x22: \x22\x22, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22granular_browser_permissions\x22: true, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22i18n_runtime_labels\x22: true, \x22import_data\x22: false, \x22import_gemini_api_key\x22: true, \x22include_df_vars_in_ai_conversation_context\x22: false, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22interactive_sheet_next_steps\x22: true, \x22is_prober\x22: false, \x22jsraw\x22: \x22compiled\x22, \x22key_promoter\x22: false, \x22kr\x22: false, \x22latest_notebook_context_for_converse\x22: true, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mlpp_multiline\x22: false, \x22mobile\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: false, \x22no_fun\x22: false, \x22notebook_context_length\x22: 40000, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22parallel_prompting\x22: true, \x22pds_minting\x22: false, \x22prereq_cells_next_steps\x22: true, \x22prevent_ai_long_response_generate\x22: false, \x22prevent_ai_long_response_generate_with_df\x22: false, \x22prevent_ai_long_response_suggest_fix\x22: false, \x22prompt_for_dsa_trusted_tester_consent\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22remove_ai_generate_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kws\x22: true, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: false, \x22rp_socketio_fallback\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_empty_notebook_actions\x22: true, \x22show_gemini_button_text_label\x22: false, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_serving_config\x22: \x22pl_700m_smart_paste_3.0.32_60\x22, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22task_service_max_poll_count\x22: 45, \x22task_service_poll_interval_ms\x22: 2000, \x22task_service_wait_before_polling_ms\x22: 5000, \x22term4all\x22: false, \x22terminate_session_on_connect_to_new_vm\x22: false, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22toolbar_above_left_pane\x22: true, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22tpu_v5e1\x22: true, \x22transform_code\x22: false, \x22transform_code_context_file_per_cell\x22: false, \x22turn_off_agent_mode_when_safe\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22updated_inline_cell_diff\x22: false, \x22use_corplogin\x22: true, \x22use_tpu_eligibility_lists\x22: false, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22, \x22V28\x22, \x22V5E1\x22\x5d, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22want_completions_ai_consent_campaign\x22: true, \x22workstations\x22: false, \x22ids\x22: \x5b20730177, 20730230, 20730324, 20730186, 20730182, 20730265, 20730363, 20730297, 20730150, 20730369, 20730315\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_prompt_cell\x22: 45644995, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_unsubscribed_warning\x22: 45504730, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_generate_code_model_id\x22: 45427663, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_readonly_cells\x22: 45671718, \x22allowed_public_url_domains\x22: 45425558, \x22auto_open_chat_on_empty_notebook\x22: 45669599, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22cell_markdown_toolbar_tooltips\x22: 45654223, \x22cell_output_actions_tooltip\x22: 45650940, \x22cell_tags\x22: 45425779, \x22cell_toolbar_ai_menu\x22: 45647581, \x22cell_toolbar_tooltips\x22: 45649981, \x22cell_ui_refresh\x22: 45673630, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22chat_reduce_refusals\x22: 45656767, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_text_compose\x22: 45425512, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22code_report_millis\x22: 45658073, \x22commands_in_toolbar\x22: 45425502, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22converse_server_side_history\x22: 45634472, \x22converse_temp\x22: 45425509, \x22corp_third_party_widgets\x22: 45678906, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22dbu\x22: 45425545, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22development\x22: 45425544, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22dsa_sample_datasets_toast\x22: 45682045, \x22enable_adhoc_backends\x22: 45425506, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_completions_backend_switching\x22: 45662651, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_rt_on_create\x22: 45667583, \x22execution_announcements\x22: 45651325, \x22execution_status_propagation\x22: 45644828, \x22explain_cell\x22: 45425505, \x22explain_error\x22: 45425487, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22filter_repetitive_suggestions\x22: 45615781, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22generate_temp\x22: 45425508, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22granular_browser_permissions\x22: 45630936, \x22hats_surveys\x22: 45425559, \x22i18n_runtime_labels\x22: 45662916, \x22import_data\x22: 45430411, \x22import_gemini_api_key\x22: 45654551, \x22include_df_vars_in_ai_conversation_context\x22: 45676033, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22interactive_sheet_next_steps\x22: 45634324, \x22is_prober\x22: 45429104, \x22jsraw\x22: 45425557, \x22key_promoter\x22: 45425570, \x22latest_notebook_context_for_converse\x22: 45668776, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mlpp_multiline\x22: 45425623, \x22mobile\x22: 45425562, \x22mpp_orc_temperature_override\x22: 45649914, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22notebook_context_length\x22: 45633457, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22parallel_prompting\x22: 45666384, \x22pds_minting\x22: 45648255, \x22prereq_cells_next_steps\x22: 45640400, \x22prevent_ai_long_response_generate\x22: 45680972, \x22prevent_ai_long_response_generate_with_df\x22: 45681123, \x22prevent_ai_long_response_suggest_fix\x22: 45681124, \x22prompt_for_dsa_trusted_tester_consent\x22: 45670923, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22remove_ai_generate_fencing\x22: 45673079, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kws\x22: 45650184, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_empty_notebook_actions\x22: 45677304, \x22show_gemini_button_text_label\x22: 45681647, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_poll_interval_ms\x22: 45669591, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22term4all\x22: 45425542, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22toolbar_above_left_pane\x22: 45683504, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22tpu_v5e1\x22: 45652002, \x22transform_code\x22: 45667102, \x22transform_code_context_file_per_cell\x22: 45671260, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22updated_inline_cell_diff\x22: 45667103, \x22use_corplogin\x22: 45425606, \x22use_tpu_eligibility_lists\x22: 45682573, \x22user_visible_accelerator_models\x22: 45682571, \x22user_visible_gpu_types\x22: 45620529, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22want_completions_ai_consent_campaign\x22: 45671138, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'dhiyaulhaq010705@gmail.com'; var colabRenderDataToken = 'AFWLbD25eG6FLHsyEbSfl4Gs5xVMaPUnZ26hz5a40Vdnnl7WUtmyPYS2qXqbEtrK3i_p4NIgH1uR6pxGw-L6tub9Hrl-P5LqDLus'; var colabConfig = '\x5b\x5b\x22dhiyaulhaq010705@gmail.com\x22,\x5b1,\x22AHXL0D2hyjOQ2gR2e7OCWqi5VpVdxY+40pFavDbb2kdvbSVTMRXf1k\/+jNuRn+zxkA8aFwlAbprZD6mfQe\/ha69RESX+0o0LYTqOUkwQWeOXql7LzqeRLqNjaDhGRr766w0xX73ZeCovTOlhBj\/HKfle3S1kHhEs9ZjYGbjt5v7tM5x67ucCiYggrglkxJ+rndhhCvIfXug3XkejW3QqActD2gCm2mgEdwzYxwpa9ZbTeItKBS\/s8HtXV9EGz7caansDDrxiIHDb3ruVzG+3XqVETqVqsiOfrUdxaYpbt\/qzXePsOvWfSTZIjNocZTL73cuBQVgyJ2JL971WXV36W1q54rjW7cKha7TcqMo7uQebVQrfZozCpmv5mFgho1nT2uccICUGSE11NDSMWbrzVuIKEW6ALH+8etL5e+iydNd\/THbIDKiiChm10bZXEDD+kmFQ9FuJB0DnLpf2kOT85B4a+j2S6SngSETXQcgDJjwsiXwS85TF1zeWL91M3dZvZddY7mXEhIYNdgZa1LiUIdgXS+tuKDahCH5T3ABTgYDkEndELcWbvO3Wtg19soHY430k29X6GGVwswcCjSiY+0KJov+jv0SrBVFe4OLw9QsuhZe1Y2gVFEZnGISrIvnF9UnZvxraOzF\/C4ihaYqaWbEneNqoV\/dEdATRrEoQjsiyeS7IU2G1xcsPWru4uGsw8I36KVyhG5moMwj5yQncuTIMUT06dAeqMVJ3\/lYHTMeuKTaLu6xf\/Kgt4LhUSoRXilSCtgvB3vpkY82MEljwyswP4vszReY5Q8aFEjsMx45aNp3zZaRXw49yT0s6wbXUZas2fApQT5Xw8U2Xh4QaA9cstT2bw3kTXJzqM42FzavijeKx0gSVTN3L59SUPUCdA\/fYW+O+OOw4nzDrpN6NizUsgPITNwYKtF+Hv\/ntVYLOBStFQ16B7OTBorv0TA+vTrGfuknITiNwrS9B88pPyi5QVl4ZGCfBqaBO1XwTcywzv5sCmEwAVVxBFbjlAaD4JOHX+OFC1Mf5Bf1Rz4ZaXxRky8eicca8z56FNqCwc6oQ8yB9OQwLW8WklDfhaa8L1B1+gEbfFwTUVEx54r3le3\/Gi48C64ehUAh1HDn7lIFb3EcPIiZHjxikaOCoty0ItiGNKKg4gh6D30PDa4k3xWyrLuQoWlU5FO3h9Z0nzT9flOMGLnbMIvTl8XBxvHdwH9ynbzRO+CTONNfbfAe3HOxQ30XqV6PMrDlnzZDJU8VpPUTvtNg+vZyWxGQplSt0FYl40rRXS7N7OCIkQAb9bFueu3TfoqFE6BeOFSvE00sauSmu3S1zwDko0NKLr2fp6O4RsLEhL6IJLOZE1X3Oh14E+yyH3IJtVK3+OaL1VJzT36FpDQYUGOyQ2N2g0yk+RojfzMvExjSFJEBxZS+EBcAu9ZMUPepWFBJssBLOv68DHDLU3\/jxIefk1X1ZMYUuf382R7EzGmT6\/1kTpPHKJUn80xDLSkVUg0FUBpEWiOvjNnjDgcN9mNGuH2qk9LNO2UV4gx+yhNvgl5KJqT8On5+MmEs\/vgdclN\/U2tlzcUA71f\/7FQcoaaJKZzuemgPgFUl\/DwL07aj6XcymNvPXNLG2U6A+BWKVy3z4uKWYy8G2kgQXc9KLfnPHl+SlWG1KcRk8ylzngZt5DYf1ee3DBDd8nWuHNWXzDGogjAhaCNzbmuNq90oh2Z4+ahrBPQ5Vx6U\/lnhGN5mqkQsNxcAsr1RwVnHluVvUqw4Iu1sCYd7QFn4ecIYB0vWntUH2O8dWsrWzoC5FZHReETrIWw2\/hbcLEX3KQLFRLI4U7Wtjnnks6Z\/NXHWIJRia3oh3QV2ukSI3B39ZpPjQn+VKPlOe4XR0h8EV6j9\/Ym3tVmrDtwFYVEzAhXwHqcjHdRcUIf8wn31xYFf+nQOsLd4qEg\/Qlu9kOhKdjrGwhw\x3d\x3d\x22,\x22AJ9oCCzw8JHHyEaQxxAzWH6eGoiEJ2sH2AKsz6MZ6R7op53+HKO5zTakoGVJJkuN+7hBcepzUHGhprNNiwavCP9lKiYDNK+wQabT08eH8s7mgV+Sv5c+uwPl8DjEpidA2ky7mpZvCuUn\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22US$9,99\x22,\x22US$49,99\x22,\x22US$9,99\x22,\x22US$49,99\x22\x5d,\x5b1,5\x5d,\x22ID\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/95405dac7bc91085246f91af064fab09/img%2Ffavicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="sNOroO9gXrazN-oMODOm0Bs0_vw1R5QwZ-BfrSHn8Io"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="8P-D5fVWgUIhw8X2BxnKJbf5itK0zxX0QhoBjbJFTe8"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="v2MQvJk6wTiBarKTbe1mdivqYCVtw-5m6w0HDzV5X_4"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./class_Restoran.ipynb - Colab_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="" type="text/javascript" charset="UTF-8" src="./class_Restoran.ipynb - Colab_files/rs=AA2YrTv9PWxAWOkNMB0THY2YxYWamdWWtA" nonce=""></script><link type="text/css" href="./class_Restoran.ipynb - Colab_files/rs=AA2YrTucClwlLUqaQmlTybxGncrc_XS2Pg" rel="stylesheet"><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><link rel="preconnect" href="https://fonts.googleapis.com/"><link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin=""><link href="./class_Restoran.ipynb - Colab_files/css2(1)" rel="stylesheet"><script async="async" type="text/javascript" src="./class_Restoran.ipynb - Colab_files/editor.main.js.download"></script><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./class_Restoran.ipynb - Colab_files/editor.main.css"><script async="async" type="text/javascript" src="./class_Restoran.ipynb - Colab_files/editor.main.nls.js.download"></script><script src="./class_Restoran.ipynb - Colab_files/api.js.download" nonce=""></script><script src="./class_Restoran.ipynb - Colab_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #1e1e1e; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #1e1e1e;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #1e1e1e;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: rgba(156, 204, 44, 0.13);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.14);
--vscode-diffEditor-insertedLineBackground: rgba(156, 204, 44, 0.13);
--vscode-diffEditor-removedLineBackground: rgba(255, 0, 0, 0.14);
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #1e1e1e;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #1e1e1e;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #1e1e1e;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #1e1e1e; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #6aa94f; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #f28b82; }
.mtk11 { color: #d7ba7d; }
.mtk12 { color: #dcdcdc; }
.mtk13 { color: #808080; }
.mtk14 { color: #4ec9b0; }
.mtk15 { color: #dcdcaa; }
.mtk16 { color: #f44747; }
.mtk17 { color: #82c6ff; }
.mtk18 { color: #c586c0; }
.mtk19 { color: #a79873; }
.mtk20 { color: #dd6a6f; }
.mtk21 { color: #5bb498; }
.mtk22 { color: #909090; }
.mtk23 { color: #778899; }
.mtk24 { color: #ff00ff; }
.mtk25 { color: #b46695; }
.mtk26 { color: #ff0000; }
.mtk27 { color: #4f76ac; }
.mtk28 { color: #3dc9b0; }
.mtk29 { color: #74b0df; }
.mtk30 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><link type="text/css" rel="stylesheet" href="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/css/mcafee_fonts.css"><script async="async" type="text/javascript" src="./class_Restoran.ipynb - Colab_files/python.js.download"></script></head><body class="" style="overscroll-behavior: contain; overflow: hidden;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./class_Restoran.ipynb - Colab_files/gapi_loader.js.download" nonce=""></script><script src="./class_Restoran.ipynb - Colab_files/socketio_binary.js.download" nonce=""></script><script src="./class_Restoran.ipynb - Colab_files/analytics_binary.js.download" nonce=""></script><script src="./class_Restoran.ipynb - Colab_files/MathJax.js.download" nonce=""></script><script src="./class_Restoran.ipynb - Colab_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./class_Restoran.ipynb - Colab_files/external_binary_l10n__id.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$105441083$-->
      <div class="mdc-snackbar  mdc-snackbar--leading ">
        <div class="mdc-snackbar__surface">
          <!--?lit$105441083$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Tutup" data-aria-label="Tutup" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tutup">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$105441083$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$105441083$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Tutup" data-aria-label="Tutup" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tutup">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_S" ng-non-bindable=""><div class="gb_Bc"><div>Akun Google</div><div class="gb_g">Dhiyaulhaq</div><div>dhiyaulhaq010705@gmail.com</div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var vd;vd=class extends _.gd{};_.wd=function(a,b){if(b in a.i)return a.i[b];throw new vd;};_.xd=function(a){return _.wd(_.dd.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Ad;_.yd=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Ad=function(a){return new _.zd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Bd=globalThis.trustedTypes;_.Cd=class{constructor(a){this.i=a}toString(){return this.i}};_.Dd=new _.Cd("about:invalid#zClosurez");_.zd=class{constructor(a){this.lh=a}};_.Ed=[Ad("data"),Ad("http"),Ad("https"),Ad("mailto"),Ad("ftp"),new _.zd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Fd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Gd=new _.Fd(_.Bd?_.Bd.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Ld,Zd,Kd,Md,Rd;_.Hd=function(a){return a==null?a:(0,_.Ua)(a)?a|0:void 0};_.Id=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Ua)(a)?a|0:void 0};_.Jd=function(a,b){return a.lastIndexOf(b,0)==0};Ld=function(){let a=null;if(!Kd)return a;try{const b=c=>c;a=Kd.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.Nd=function(){Md===void 0&&(Md=Ld());return Md};
_.Pd=function(a){const b=_.Nd();return new _.Od(b?b.createScriptURL(a):a)};_.Qd=function(a){if(a instanceof _.Od)return a.i;throw Error("H");};_.Sd=function(a){if(Rd.test(a))return a};_.Td=function(a){if(a instanceof _.Cd)if(a instanceof _.Cd)a=a.i;else throw Error("H");else a=_.Sd(a);return a};_.Ud=function(a,b=document){let c;const d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};_.Vd=function(a,b,c){return _.tb(a,b,c)!==void 0};
_.Wd=function(a,b){return _.Id(_.Bc(a,b))};_.S=function(a,b){return _.Hd(_.Bc(a,b))};_.T=function(a,b,c=0){let d;return(d=_.Wd(a,b))!=null?d:c};_.Xd=function(a,b,c=0){let d;return(d=_.S(a,b))!=null?d:c};_.Yd=function(a){var b=_.Sa(a);return b=="array"||b=="object"&&typeof a.length=="number"};Kd=_.Bd;_.Od=class{constructor(a){this.i=a}toString(){return this.i+""}};Rd=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var de,he,$d;_.be=function(a){return a?new $d(_.ae(a)):Zd||(Zd=new $d)};_.ce=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.U=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a?a=(b||c).querySelector(a?"."+a:""):(b=b||c,a=(a?b.querySelectorAll(a?"."+a:""):b.getElementsByTagName("*"))[0]||null));return a||null};
_.ee=function(a,b){_.vb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:de.hasOwnProperty(d)?a.setAttribute(de[d],c):_.Jd(d,"aria-")||_.Jd(d,"data-")?a.setAttribute(d,c):a[d]=c})};de={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.fe=function(a){return a?a.defaultView:window};_.ie=function(a,b){const c=b[1],d=_.ge(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.ee(d,c));b.length>2&&he(a,d,b);return d};he=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.Yd(f)||_.Eb(f)&&f.nodeType>0?d(f):_.Xb(f&&typeof f.length=="number"&&typeof f.item=="function"?_.yd(f):f,d)}};
_.je=function(a){return _.ge(document,a)};_.ge=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.ke=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.le=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.me=function(a,b){return a&&b?a==b||a.contains(b):!1};_.ae=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};$d=function(a){this.i=a||_.t.document||document};_.p=$d.prototype;
_.p.H=function(a){return _.ce(this.i,a)};_.p.Ua=function(a,b,c){return _.ie(this.i,arguments)};_.p.appendChild=function(a,b){a.appendChild(b)};_.p.ue=_.ke;_.p.Nf=_.le;_.p.Mf=_.me;
}catch(e){_._DumpException(e)}
try{
_.wi=function(a){const b=_.Ud("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.xi=function(a){if(!a)return null;a=_.G(a,4);var b;a===null||a===void 0?b=null:b=_.Pd(a);return b};_.yi=class extends _.P{constructor(a){super(a)}};_.zi=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Bi=function(a,b,c){a<b?Ai(a+1,b):_.Oc.log(Error("fa`"+a+"`"+b),{url:c})},Ai=function(a,b){if(Ci){const c=_.je("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.Qd(Ci);_.wi(c);c.onerror=_.Hb(Bi,a,b,c.src);_.zi("HEAD")[0].appendChild(c)}},Di=class extends _.P{constructor(a){super(a)}};var Ei=_.D(_.Yc,Di,17)||new Di,Fi,Ci=(Fi=_.D(Ei,_.yi,1))?_.xi(Fi):null,Gi,Hi=(Gi=_.D(Ei,_.yi,2))?_.xi(Gi):null,Ii=function(){Ai(1,2);if(Hi){const a=_.je("LINK");a.setAttribute("type","text/css");a.href=_.Qd(Hi).toString();a.rel="stylesheet";let b=_.Ud("style",document);b&&a.setAttribute("nonce",b);_.zi("HEAD")[0].appendChild(a)}};(function(){const a=_.Zc();if(_.F(a,18))Ii();else{const b=_.Wd(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Ii,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><deepl-input-controller><template shadowrootmode="open"><link rel="stylesheet" href="chrome-extension://cofdbpoegempjloogbagkncekinflcnj/build/content.css"><div dir="ltr" style="visibility: initial !important;"><div class="dl-input-translation-container svelte-95aucy"><div></div></div></div></template></deepl-input-controller><style>html, :root, .aifnmjmchg.light, :host([class=light]) {--aifnmjmchg-main-color: 0, 0, 0;}.aifnmjmchg.light  .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover,.aifnmjmchg.light  .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover *,.aifnmjmchg.light .opener-logo:hover svg circle,.aifnmjmchg.light  .opener-logo:hover,.aifnmjmchg.light .opener-logo:hover svg circle,.aifnmjmchg.light  .opener-logo:hover *,.aifnmjmchg.light .tab-menu .active,.aifnmjmchg.light .tab-menu .active *,.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\],.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\] *,.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\],.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\] *,.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover,.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover *,.aifnmjmchg.light .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\]:hover *,.aifnmjmchg.light .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\]:hover * *,.aifnmjmchg.light #aifnmjmchg-sidebar-opener:hover .ai-aifnmjmchgopener-close,.aifnmjmchg.light #aifnmjmchg-sidebar-opener:hover .ai-aifnmjmchgopener-close *,.aifnmjmchg.light .dark\:hover\:aifnmjmchg-text-white:hover,.aifnmjmchg.light .dark\:hover\:aifnmjmchg-text-white:hover * {color: #fff !important;}.aifnmjmchg.light  .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover svg path,.aifnmjmchg.light  .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover svg circle,.aifnmjmchg.light .opener-logo:hover svg circle,.aifnmjmchg.light  .opener-logo:hover svg path,.aifnmjmchg.light .opener-logo:hover svg circle,.aifnmjmchg.light  .opener-logo:hover svg circle,.aifnmjmchg.light .tab-menu .active svg path,.aifnmjmchg.light .tab-menu .active svg circle,.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\] svg path,.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\] svg circle,.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\] svg path,.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\] svg circle,.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover svg path,.aifnmjmchg.light .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover svg circle,.aifnmjmchg.light .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\]:hover * svg path,.aifnmjmchg.light .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\]:hover * svg circle,.aifnmjmchg.light #aifnmjmchg-sidebar-opener:hover .ai-aifnmjmchgopener-close svg path,.aifnmjmchg.light #aifnmjmchg-sidebar-opener:hover .ai-aifnmjmchgopener-close svg circle,.aifnmjmchg.light .dark\:hover\:aifnmjmchg-text-white:hover svg path,.aifnmjmchg.light .dark\:hover\:aifnmjmchg-text-white:hover svg circle {fill: #fff !important;}.aifnmjmchg.light .light\:aifnmjmchg-text-neutral-300.hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\]:hover {color: #fff !important;}.aifnmjmchg.light .aifnmjmchg-peer:checked~.peer-checked\:after\:aifnmjmchg-border-white:after{background-color:#fff!important;}.aifnmjmchg.dark, :host([class=dark]) {--aifnmjmchg-main-color: 255, 255, 255;}.aifnmjmchg.dark  .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover,.aifnmjmchg.dark  .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover *,.aifnmjmchg.dark .opener-logo:hover svg circle,.aifnmjmchg.dark  .opener-logo:hover,.aifnmjmchg.dark .opener-logo:hover svg circle,.aifnmjmchg.dark  .opener-logo:hover *,.aifnmjmchg.dark .tab-menu .active,.aifnmjmchg.dark .tab-menu .active *,.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\],.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\] *,.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\],.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\] *,.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover,.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover *,.aifnmjmchg.dark .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\]:hover *,.aifnmjmchg.dark .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\]:hover * *,.aifnmjmchg.dark #aifnmjmchg-sidebar-opener:hover .ai-aifnmjmchgopener-close,.aifnmjmchg.dark #aifnmjmchg-sidebar-opener:hover .ai-aifnmjmchgopener-close *,.aifnmjmchg.dark .dark\:hover\:aifnmjmchg-text-white:hover,.aifnmjmchg.dark .dark\:hover\:aifnmjmchg-text-white:hover * {color: #000 !important;}.aifnmjmchg.dark  .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover svg path,.aifnmjmchg.dark  .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover svg circle,.aifnmjmchg.dark .opener-logo:hover svg circle,.aifnmjmchg.dark  .opener-logo:hover svg path,.aifnmjmchg.dark .opener-logo:hover svg circle,.aifnmjmchg.dark  .opener-logo:hover svg circle,.aifnmjmchg.dark .tab-menu .active svg path,.aifnmjmchg.dark .tab-menu .active svg circle,.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\] svg path,.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\] svg circle,.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\] svg path,.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\] svg circle,.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover svg path,.aifnmjmchg.dark .aifnmjmchg-bg-\[var\(--aifnmjmchg-link-color\)\]:hover svg circle,.aifnmjmchg.dark .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\]:hover * svg path,.aifnmjmchg.dark .hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\]:hover * svg circle,.aifnmjmchg.dark #aifnmjmchg-sidebar-opener:hover .ai-aifnmjmchgopener-close svg path,.aifnmjmchg.dark #aifnmjmchg-sidebar-opener:hover .ai-aifnmjmchgopener-close svg circle,.aifnmjmchg.dark .dark\:hover\:aifnmjmchg-text-white:hover svg path,.aifnmjmchg.dark .dark\:hover\:aifnmjmchg-text-white:hover svg circle {fill: #000 !important;}.aifnmjmchg.dark .dark\:aifnmjmchg-text-neutral-300.hover\:aifnmjmchg-bg-\[var\(--aifnmjmchg-tab-menu-active-bg-color\)\]:hover {color: #000 !important;}.aifnmjmchg.dark .aifnmjmchg-from-\[\#28282b\] * {color: #fff !important;}.aifnmjmchg.light .aifnmjmchg-peer:checked~.peer-checked\:after\:aifnmjmchg-border-white:after{background-color:#fff!important;}.aifnmjmchg.dark .aifnmjmchg-peer:checked~.peer-checked\:after\:aifnmjmchg-border-white:after{background-color:#000!important;}</style><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./class_Restoran.ipynb - Colab_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical colab-left-pane-open" style="position: relative;">
      <!--?lit$105441083$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$105441083$--><a id="link" class="button" href="https://colab.research.google.com/drive/1CUMTCVRW9nOVHMuuwKrgU3artqtnwy6v#notebook-main"><!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </a>
    </template><!--?lit$105441083$-->Langsung ke konten utama</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$105441083$-->
    <!--?lit$105441083$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning" hidden=""><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$105441083$-->Notebook ini dibuka dengan output pribadi. Output tidak akan disimpan. Anda dapat menonaktifkan ini di <a href="https://colab.research.google.com/drive/1CUMTCVRW9nOVHMuuwKrgU3artqtnwy6v#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Setelan notebook</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Buka setelan notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Tutup" data-aria-label="Tutup" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tutup">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$105441083$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><div id="header-logo">
              <!--?lit$105441083$--> <!--?lit$105441083$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="Lihat di Google Drive">
        <!--?lit$105441083$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$--><svg viewBox="0 0 24 24"><!--?lit$105441083$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$105441083$--> <!--?lit$105441083$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook yang disimpan di Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Nama notebook" command="rename" aria-describedby="doc-name-tooltip" style="width: 188.25px;" data-has-listeners="true" fdprocessedid="vehawk"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Ganti nama notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">class_Restoran.ipynbS_</colab-input-sizer>
            <!--?lit$105441083$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Beri bintang" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Beri bintang">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Bintangi notebook di Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$105441083$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="Semua perubahan telah disimpan" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Semua perubahan telah disimpan">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="Semua perubahan telah disimpan"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Semua perubahan telah disimpan</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$105441083$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$105441083$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$105441083$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$105441083$-->Lihat</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$105441083$-->Sisipkan</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$105441083$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$105441083$-->Fitur</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$105441083$-->Bantuan</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$105441083$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$105441083$-->
      <!--?lit$105441083$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$105441083$--> <md-icon-button id="comments" command="open-comments-thread" data-aria-label="Buka panel komentar" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Buka panel komentar">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Buka panel komentar</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$105441083$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Buka setelan" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Buka setelan">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Buka setelan</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$105441083$--> <md-filled-tonal-button id="share-toolbar-button" command="share" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$105441083$--><button id="button" class="button">
      <!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->people</md-icon>
                <!--?lit$105441083$-->Bagikan
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Bagikan notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$105441083$--> <md-icon-button class="show-chat-button" id="show-chat-button" command="show-chat" data-aria-label="Tampilkan Gemini" aria-describedby="show-chat-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tampilkan Gemini">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Tampilkan Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Fa gb_Jd gb_2d gb_Wc" id="gb"><div class="gb_Cd gb_Zd gb_xd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Qe" style="display:block"><div class="gb_3c"></div><div class="gb_z gb_cd gb_Mf gb_0"><div class="gb_D gb_jb gb_Mf gb_0"><a class="gb_B gb_Za gb_0" aria-expanded="false" aria-label="Akun Google: Dhiyaulhaq  
(dhiyaulhaq010705@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=id&amp;continue=https://colab.research.google.com/&amp;ec=GBRAqQM" tabindex="0" role="button"><img class="gb_P gbii" src="./class_Restoran.ipynb - Colab_files/unnamed.jpg" srcset="https://lh3.googleusercontent.com/ogw/AF2bZyie0u5VfiUVEtjEJjJKqeLOHJzrWUVZl5D3Sc451-8TV_o=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/AF2bZyie0u5VfiUVEtjEJjJKqeLOHJzrWUVZl5D3Sc451-8TV_o=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""><div class="gb_Q gb_R" aria-hidden="true"><svg class="gb_Ka" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_La" cx="7" cy="7" r="7"></circle><path class="gb_Na" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.qd=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.qd(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("D`"+b))}};
}catch(e){_._DumpException(e)}
try{
var sd=document.querySelector(".gb_J .gb_B"),td=document.querySelector("#gb.gb_Sc");sd&&!td&&_.qd(_.cd,sd,"click");
}catch(e){_._DumpException(e)}
try{
_.Yg=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].fa()&&a.i[b].B())return a.i[b];return null};_.Zg=function(a,b){a.i[b.J()]=b};var $g=new class extends _.Q{constructor(){var a=_.Oc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.Yg(this)&&_.Yg(this).J()==a||this.i[a].R(!0))}Pa(a){this.j=a;for(const b in this.i)this.i[b].fa()&&this.i[b].Pa(a)}fc(a){return a in this.i?this.i[a]:null}};_.fd("dd",$g);
}catch(e){_._DumpException(e)}
try{
_.qi=function(a,b){return _.K(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var ri=document.querySelector(".gb_z .gb_B"),si=document.querySelector("#gb.gb_Sc");ri&&!si&&_.qd(_.cd,ri,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><div class="notebook-horizontal">
        <!--?lit$105441083$--><colab-left-pane role="complementary" aria-label="left pane" class="colab-left-pane-open"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$105441083$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Daftar isi" title="Daftar isi" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Daftar isi" aria-pressed="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$105441083$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$105441083$--><md-icon-button toggle="" command="find" data-aria-label="Cari dan ganti" title="Cari dan ganti" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cari dan ganti" aria-pressed="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$105441083$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$105441083$--><md-icon-button toggle="" command="show-variables" data-aria-label="Variabel" title="Variabel" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Variabel" aria-pressed="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$--><svg viewBox="0 0 24 24"><!--?lit$105441083$-->
      <path d="M4.51,9.44V6.08c0-1.34.37-1.85,1.6-2.17l.22-.06V3.13l-.27,0-.44,0a4.46,4.46,0,0,0-2.2.59,2.78,2.78,0,0,0-1,2.51V9.74c0,1.26-.26,1.61-1.49,2L0,12l.94.29c1.21.38,1.49.75,1.49,2v3.5a2.94,2.94,0,0,0,1,2.6,4.39,4.39,0,0,0,2.14.56l.46,0,.27,0v-.72l-.22-.06c-1.24-.32-1.6-.81-1.6-2.17V14.58c0-1.43-.3-2.13-1.25-2.57C4.2,11.57,4.51,10.87,4.51,9.44Z"></path>
      <path d="M23.06,11.71c-1.22-.36-1.49-.71-1.49-2l0-3.5a3,3,0,0,0-1-2.6,4.38,4.38,0,0,0-2.14-.56l-.46,0-.27,0v.72l.22.06c1.24.32,1.6.81,1.6,2.17V9.44c0,1.44.3,2.13,1.25,2.57-1,.44-1.25,1.14-1.25,2.57v3.36c0,1.34-.37,1.85-1.6,2.17l-.22.06v.72l.27,0,.44,0a4.47,4.47,0,0,0,2.2-.59,2.82,2.82,0,0,0,1-2.51V14.28c0-1.26.26-1.61,1.49-2L24,12Z"></path>
      <path d="M15.16,8.22a.88.88,0,0,1,.46.16,1.25,1.25,0,0,0,.69.2h0A1,1,0,0,0,17,8.23a1.06,1.06,0,0,0,.24-.8,1.1,1.1,0,0,0-1.15-1h0c-1,0-1.73.64-3,2.57l-.12-.51c-.28-1.36-.56-2-1.39-2h0A8,8,0,0,0,9,7.08l-.47.16.16.91L9.41,8a3.22,3.22,0,0,1,.73-.14c.34,0,.43,0,.71,1.2l.56,2.47L9.76,13.82a3.6,3.6,0,0,1-.8.88.9.9,0,0,1-.38-.13,1.83,1.83,0,0,0-.88-.28,1,1,0,0,0-1,1.06A1.15,1.15,0,0,0,8,16.53c.85,0,1.35-.35,2.24-1.55l1.49-2,.46,1.88c.23,1,.46,1.66,1.53,1.66s1.66-.75,2.81-2.53l.17-.26-.81-.48-.16.2-.25.34-.19.25c-.45.57-.62.73-.76.73s-.28-.4-.34-.63l-.67-2.83a4.2,4.2,0,0,1-.15-.79C13.84,9.78,14.74,8.22,15.16,8.22Z"></path></svg></md-icon>
    </md-icon-button> <!--?lit$105441083$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$105441083$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Rahasia" title="Rahasia" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Rahasia" aria-pressed="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$105441083$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$105441083$--><md-icon-button toggle="" command="show-files" data-aria-label="File" title="File" value="" selected=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button standard selected" aria-label="File" aria-pressed="true">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="icon icon--selected"><slot name="selected"><slot></slot></slot></span>
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->folder</md-icon>
    </md-icon-button> <!--?lit$105441083$-->
      </div></div>
        <div class="left-pane-bottom"><!----><div class="left-pane-button">
        <!--?lit$105441083$--><md-icon-button command="snippets" data-aria-label="Cuplikan kode" title="Cuplikan kode" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Cuplikan kode">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->code</md-icon>
    </md-icon-button> <!--?lit$105441083$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$105441083$--><md-icon-button command="show-terminal" data-aria-label="Terminal" title="Terminal" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Terminal">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->terminal</md-icon>
    </md-icon-button> <!--?lit$105441083$-->
      </div></div>
      </div><colab-resizer class="ew-resize">
          <div class="resizer-contents">
            <div class="colab-left-pane-header layout horizontal noshrink">
              <h3 class="left-pane-content-title">File</h3>
              <!--?lit$105441083$--><md-icon-button class="colab-left-pane-move" data-aria-label="Pindahkan panel kiri ke tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Pindahkan panel kiri ke tab">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>tab</md-icon>
    </md-icon-button> <!--?lit$105441083$--><md-icon-button class="colab-left-pane-close" data-aria-label="Tutup panel kiri" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tutup panel kiri">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
            </div>
            <div class="left-pane-container"><colab-file-browser class="layout vertical"><colab-file-tree><!----> <!--?lit$105441083$--><colab-agent-promo-banner><template shadowrootmode="open"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <div><!--?lit$105441083$-->Analisis file Anda dengan kode yang ditulis oleh Gemini</div>
      <md-text-button value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$105441083$--><button id="button" class="button">
      <!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </button>
    </template>
        <!--?lit$105441083$-->Upload
      </md-text-button></template>
            </colab-agent-promo-banner>
        <div class="file-tree-buttons">
          <label for="file-tree-upload-input">
            <md-icon-button class="colab-icon file-tree-upload-button" title="Upload ke penyimpanan sesi" data-aria-label="Upload ke penyimpanan sesi" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Upload ke penyimpanan sesi">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
              <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>upload_file</md-icon>
            </md-icon-button>
          </label>
          <input id="file-tree-upload-input" type="file" multiple="" data-has-listeners="true">
          <md-icon-button class="file-tree-refresh" title="Muat ulang" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard ">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>refresh</md-icon>
          </md-icon-button>
          <md-icon-button toggle="" class="mount-drive-button" title="Pasang Drive" data-aria-label="Pasang Drive" aria-label-selected="Lepaskan Drive" style="display: flex;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Pasang Drive" aria-pressed="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$--><svg viewBox="0 0 24 24"><!--?lit$105441083$-->
    <path d="M20,6H12L10,4H4A2,2,0,0,0,2,6V18a2,2,0,0,0,2,2H20a2,2,0,0,0,2-2V8A2,2,0,0,0,20,6ZM13.57,9.32,13,8.4l.34-.6h3.11l3.69,6.5H16.38M12.11,17l-.67,1.2h-1L9,15.42,12.72,9l2,3.46h0M19.3,18.2H12.09l.67-1.2,1.15-2h6.64l.34.6Z"></path></svg></md-icon>
            <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$--><svg viewBox="0 0 24 24"><!--?lit$105441083$-->
    <path d="M12.72,9l2,3.46h0l-.26.47,2,2h4.1l.34.6L19.45,18l1.69,1.69A2,2,0,0,0,22,18V8a2,2,0,0,0-2-2H12L10,4H5.5l6.4,6.4Zm.66-1.17h3.11l3.69,6.5H16.38l-2.81-5L13,8.4Z"></path>
    <path d="M22.19,22.19,1.81,1.81.4,3.22,2.25,5.07A2,2,0,0,0,2,6V18a2,2,0,0,0,2,2H17.17l3.61,3.61Zm-11.73-4L9,15.42l1.3-2.26,2.35,2.36.17.17L12.11,17l-.67,1.2Zm1.63,0,.67-1.2.51-.9,2.1,2.1Z"></path></svg></md-icon>
          </md-icon-button>
          <md-icon-button toggle="" id="hidden-files-toggle" data-aria-label="Tampilkan file tersembunyi" aria-label-selected="Jangan tampilkan file tersembunyi" title="Tampilkan file tersembunyi" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tampilkan file tersembunyi" aria-pressed="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>visibility_off</md-icon>
            <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>visibility</md-icon>
          </md-icon-button>
        </div>
        <div class="parent-link"><div class="file-title-row">
          <!--?lit$105441083$-->
                <div class="file-icon colab-icon" style="margin-left: 0px;"></div>
              
          <md-icon class="file-icon colab-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->folder_open</md-icon>
          <span class="file-tree-name" title="Naik satu tingkat">
            <!--?lit$105441083$-->..
          </span>
          <input class="file-tree-name-input" value=".." data-has-listeners="true">
          <md-icon-button class="file-item-menu" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Tindakan lainnya untuk file: .." value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tindakan lainnya untuk file: .." aria-haspopup="menu" aria-expanded="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon></md-icon-button>
        </div></div>
        <div class="files-root"><colab-file-view filename="content" draggable="true"><!----><!--?lit$105441083$--><!--?--><!--?lit$105441083$-->
        <div class="child-files"><colab-file-view filename="sample_data" class="collapsed" draggable="true"><!----><!--?lit$105441083$-->
        <div class="file-title-row">
          <!--?lit$105441083$--> <md-icon class="file-icon colab-icon directory-icon" style="margin-left: 0px;" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
          <md-icon class="file-icon colab-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->folder</md-icon>
          <span class="file-tree-name" title="sample_data">
            <!--?lit$105441083$-->sample_data
          </span>
          <input class="file-tree-name-input" value="sample_data" data-has-listeners="true">
          <md-icon-button class="file-item-menu" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Tindakan lainnya untuk folder: sample_data" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tindakan lainnya untuk folder: sample_data" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon></md-icon-button>
        </div>
      <!--?lit$105441083$-->
        <div class="child-files"></div>
        <div class="overflow-ellipsis" title="Direktori terlalu besar untuk menampilkan semua file." style="margin-left: 0px;">
          …
        </div>
      <!--?--></colab-file-view></div>
        <div class="overflow-ellipsis" title="Direktori terlalu besar untuk menampilkan semua file." style="margin-left: -20px;">
          …
        </div>
      <!--?--></colab-file-view></div>
        <div class="files-drag-to-upload layout horizontal">
          <md-icon class="layout noshrink" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>upload_file</md-icon>
          <div> <!--?lit$105441083$-->Tarik file untuk menguploadnya ke penyimpanan sesi. </div>
        </div>
        <div class="files-uploading"></div>
        <div class="colab-usage-bar-container"><colab-usage-bar aria-describedby="file-browser-disk-display-kernel-tooltip" id="file-browser-disk-display-kernel" class="file-browser-disk-display usage-bar-with-suffix" tabindex="0" style="display: flex;"><template shadowrootmode="open"><!---->
        <div class="header">
          <div><!--?lit$105441083$-->Disk </div>
          <div class="suffix"><!--?lit$105441083$-->71.10 GB tersedia</div>
        </div>
        <!--?lit$105441083$-->
      <div class="progress-container">
        <md-linear-progress class="  " value="0.33988729555404223"><template shadowrootmode="open"><!---->
      <div role="progressbar" aria-valuemin="0" class="progress   " aria-valuemax="1" aria-valuenow="0.33988729555404223"><!--?lit$105441083$-->
      <div class="dots" hidden=""></div>
      <div class="inactive-track" style="transform: scaleX(1);"></div>
      <div class="bar primary-bar" style="transform: scaleX(0.339887);">
        <div class="bar-inner"></div>
      </div>
      <div class="bar secondary-bar">
        <div class="bar-inner"></div>
      </div>
    </div>
    </template></md-linear-progress>
      </div>
    
      </template></colab-usage-bar><colab-tooltip-trigger aria-hidden="true" id="file-browser-disk-display-kernel-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Disk: 36.61 GB/107.72 GB</div><!----><!--?--></template></colab-tooltip-trigger></div></colab-file-tree></colab-file-browser></div>
          </div>
        <div class="resizer-thumb"></div></colab-resizer></colab-left-pane>
        <div class="layout vertical grow">
          <colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$105441083$--> <colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$105441083$--><button id="button" class="button">
      <!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </button>
    </template>
        <!--?lit$105441083$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$105441083$--><span class="screenreader-only"><!--?lit$105441083$-->Tampilkan palet perintah <!--?lit$105441083$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$105441083$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Tampilkan palet perintah" shortcut="Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Tampilkan palet perintah (Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$105441083$-->Perintah
          </colab-toolbar-button>
          <span class="colab-separator"></span>
    <!--?lit$105441083$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$105441083$--><button id="button" class="button">
      <!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </button>
    </template>
        <!--?lit$105441083$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$105441083$--><span class="screenreader-only"><!--?lit$105441083$-->Sisipkan sel kode di bawah <!--?lit$105441083$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$105441083$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Sisipkan sel kode di bawah" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Sisipkan sel kode di bawah (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$105441083$-->Kode
          </colab-toolbar-button>
          <!--?lit$105441083$-->
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$105441083$--><button id="button" class="button">
      <!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </button>
    </template>
        <!--?lit$105441083$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$105441083$--><span class="screenreader-only"><!--?lit$105441083$-->Tambahkan sel teks <!--?lit$105441083$--></span>
      </md-text-button>
      <!--?lit$105441083$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Tambahkan sel teks" shortcut=""><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Tambahkan sel teks</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$105441083$-->Teks
          </colab-toolbar-button>
        
    <!--?lit$105441083$-->
    <!--?lit$105441083$-->
    <!--?lit$105441083$-->
    <!--?lit$105441083$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="Semua perubahan telah disimpan" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Semua perubahan telah disimpan">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="Semua perubahan telah disimpan"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Semua perubahan telah disimpan</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$105441083$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$105441083$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$105441083$--><!--?lit$105441083$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$105441083$--> <!--?lit$105441083$--><md-icon-button id="connect-icon" class="icon-okay" data-aria-label="Fokus pada sel yang terakhir dijalankan" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Fokus pada sel yang terakhir dijalankan">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->done</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger for="connect-icon" id="connect-icon-tooltip" aria-hidden="true" message="Fokus pada sel yang terakhir dijalankan"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Fokus pada sel yang terakhir dijalankan</div><!----><!--?--></template>
          </colab-tooltip-trigger>
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Terhubung ke
backend Google Compute Engine Python 3
RAM: 1.10 GB/12.67 GB
Disk: 36.61 GB/107.72 GB"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$105441083$--><button id="button" class="button">
      <!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </button>
    </template>
        <!--?lit$105441083$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$105441083$--><span class="screenreader-only"><!--?lit$105441083$-->Terhubung ke
backend Google Compute Engine Python 3
RAM: 1.10 GB/12.67 GB
Disk: 36.61 GB/107.72 GB <!--?lit$105441083$--></span>
      </md-text-button>
      <!--?lit$105441083$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Terhubung ke
backend Google Compute Engine Python 3
RAM: 1.10 GB/12.67 GB
Disk: 36.61 GB/107.72 GB" shortcut=""><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Terhubung ke</div><!----><!----><div><!--?lit$105441083$-->backend Google Compute Engine Python 3</div><!----><!----><div><!--?lit$105441083$-->RAM: 1.10 GB/12.67 GB</div><!----><!----><div><!--?lit$105441083$-->Disk: 36.61 GB/107.72 GB</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$105441083$--> <div id="connect-button-resource-display">
        <!--?lit$105441083$--><colab-usage-sparkline class="ram" label="RAM"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$105441083$-->RAM</div>
      <!--?lit$105441083$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
        <!--?lit$105441083$--><colab-usage-sparkline class="disks" label="Disk"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$105441083$-->Disk</div>
      <!--?lit$105441083$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
      </div>
      </colab-toolbar-button>
      <!--?lit$105441083$--> <md-icon-button id="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Opsi sambungan tambahan" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Opsi sambungan tambahan" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Opsi sambungan tambahan"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Opsi sambungan tambahan</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$105441083$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$105441083$-->
    <span class="collapsed-options">
      <!--?lit$105441083$--><span class="colab-separator"></span>
      <!--?lit$105441083$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Bagikan notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Bagikan notebook">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Bagikan notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Buka setelan" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Buka setelan">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Buka setelan</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$105441083$--> <md-icon-button class="show-chat-button" id="show-chat-button-toolbar" command="show-chat" data-aria-label="Tampilkan Gemini" aria-describedby="show-chat-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tampilkan Gemini">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button-toolbar" id="show-chat-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Tampilkan Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$105441083$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Alihkan visibilitas header" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Alihkan visibilitas header" aria-pressed="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Alihkan visibilitas header</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$105441083$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$105441083$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-DHOn6Cb2778-" class="selected-tab" tabindex="0" md-tab="" active=""><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$105441083$--><div class="indicator"></div>
      </div>
      <!--?lit$105441083$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-DHOn6Cb2778-"><!--?lit$105441083$--><!--?lit$105441083$-->Notebook<!--?--></span>
            <!--?lit$105441083$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$105441083$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Tindakan tab lainnya" data-aria-label="Tindakan tab lainnya" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tindakan tab lainnya" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" tabindex="-1" role="main" id="notebook-main" class="notebook-container" aria-label="Notebook">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$105441083$-->
              <div class="notebook-content ">
                <!--?lit$105441083$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Tambahkan sel kode
Ctrl+M B" title="Tambahkan sel kode
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$105441083$--><button id="button" class="button" aria-label="Tambahkan sel kode
Ctrl+M B">
      <!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$105441083$-->Kode
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Tambahkan sel teks" title="Tambahkan sel teks" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$105441083$--><button id="button" class="button" aria-label="Tambahkan sel teks">
      <!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$105441083$-->Teks
        </md-outlined-button>
        <!--?lit$105441083$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code icon-scrolling focused code-has-output" id="cell-mKGBJ5aE778h" tabindex="-1" role="region" aria-label="Sel 0: Sel kode: " style=""><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$105441083$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Naikkan sel
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Naikkan sel
Ctrl+M K" aria-disabled="true">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->arrow_upward</md-icon>
        <!--?lit$105441083$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Naikkan sel
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Naikkan sel</div><!----><!----><div><!--?lit$105441083$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Turunkan sel
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Turunkan sel
Ctrl+M J" aria-disabled="true">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->arrow_downward</md-icon>
        <!--?lit$105441083$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Turunkan sel
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Turunkan sel</div><!----><!----><div><!--?lit$105441083$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$105441083$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-mKGBJ5aE778h" anchor="ai-menu-anchor-mKGBJ5aE778h" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$105441083$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$105441083$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$105441083$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$105441083$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$105441083$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$105441083$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$105441083$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$105441083$-->Buat kode</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$105441083$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$105441083$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$105441083$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$105441083$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$105441083$-->Jelaskan kode</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-mKGBJ5aE778h-tooltip" data-aria-label="Fitur AI yang tersedia" id="ai-menu-anchor-mKGBJ5aE778h" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Fitur AI yang tersedia" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-mKGBJ5aE778h" id="ai-menu-anchor-mKGBJ5aE778h-tooltip" message="Fitur AI yang tersedia"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Fitur AI yang tersedia</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-copy-link-to-cell-tooltip" data-aria-label="Salin link ke sel" command="copy-link-to-cell" id="button-copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Salin link ke sel">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->link</md-icon>
        <!--?lit$105441083$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-copy-link-to-cell" id="button-copy-link-to-cell-tooltip" message="Salin link ke sel"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Salin link ke sel</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-add-comment-tooltip" data-aria-label="Tambahkan komentar
Ctrl+Alt+M" command="add-comment" id="button-add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tambahkan komentar
Ctrl+Alt+M">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->comment</md-icon>
        <!--?lit$105441083$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-add-comment" id="button-add-comment-tooltip" message="Tambahkan komentar
Ctrl+Alt+M"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Tambahkan komentar</div><!----><!----><div><!--?lit$105441083$-->Ctrl+Alt+M</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-editor-preferences-tooltip" data-aria-label="Buka setelan editor" command="editor-preferences" id="button-editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Buka setelan editor">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->settings</md-icon>
        <!--?lit$105441083$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-editor-preferences" id="button-editor-preferences-tooltip" message="Buka setelan editor"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Buka setelan editor</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->edit</md-icon>
        <!--?lit$105441083$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-mirror-cell-in-tab-tooltip" data-aria-label="Sel duplikat di tab" command="mirror-cell-in-tab" id="button-mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Sel duplikat di tab">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$--><svg viewBox="0 0 24 24"><!--?lit$105441083$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
        <!--?lit$105441083$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-mirror-cell-in-tab" id="button-mirror-cell-in-tab-tooltip" message="Sel duplikat di tab"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Sel duplikat di tab</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Hapus sel
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Hapus sel
Ctrl+M D">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->delete</md-icon>
        <!--?lit$105441083$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Hapus sel
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Hapus sel</div><!----><!----><div><!--?lit$105441083$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$105441083$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="Tindakan sel lainnya" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tindakan sel lainnya" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="Tindakan sel lainnya"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Tindakan sel lainnya</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution focused hovered">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Jalankan sel" aria-disabled="false">
        <!--?lit$105441083$--><span class="execution-count"><!--?lit$105441083$-->[5]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$105441083$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$105441083$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$105441083$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Jalankan sel (Ctrl+Enter)
sel telah dieksekusi sejak perubahan terakhir

dijalankan oleh Dhiyaulhaq
22.37 (0 menit yang lalu)
dijalankan dalam 0.023 d"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Jalankan sel (Ctrl+Enter)</div><!----><!----><div><!--?lit$105441083$-->sel telah dieksekusi sejak perubahan terakhir</div><!----><!----><br><!----><!----><div><!--?lit$105441083$-->dijalankan oleh Dhiyaulhaq</div><!----><!----><div><!--?lit$105441083$-->22.37 (0 menit yang lalu)</div><!----><!----><div><!--?lit$105441083$-->dijalankan dalam 0.023 d</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$105441083$--><div id="status" class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$--><svg viewBox="0 0 24 24"><!--?lit$105441083$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$105441083$-->0 d</div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="1" data-mode-id="notebook-python" style="height: 352px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/3" style="width: 626px; height: 352px;"><div data-mprt="3" class="overflow-guard" style="width: 626px; height: 352px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 352px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 352px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 352px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 620px; height: 352px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 352px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 668px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="cdr wordHighlightText" style="left:131px;width:31px;height:19px;"></div></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="cdr wordHighlightText" style="left:62px;width:31px;height:19px;"></div></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="cdr wordHighlightText" style="left:62px;width:31px;height:19px;"></div></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="cdr wordHighlightText" style="left:62px;width:31px;height:19px;"></div></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"><div class="cdr wordHighlightText" style="left:169px;width:31px;height:19px;"></div></div><div style="position:absolute;top:133px;width:100%;height:19px;"><div class="cdr wordHighlightText" style="left:200px;width:31px;height:19px;"></div><div class="cdr wordHighlightText" style="left:377px;width:31px;height:19px;"></div></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"><div class="current-line" style="width:668px; height:19px;"></div><div class="cdr wordHighlightText" style="left:192px;width:31px;height:19px;"></div></div><div style="position:absolute;top:190px;width:100%;height:19px;"><div class="cdr wordHighlightText" style="left:62px;width:31px;height:19px;"></div></div><div style="position:absolute;top:209px;width:100%;height:19px;"><div class="cdr wordHighlightText" style="left:493px;width:31px;height:19px;"></div></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 352px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 668px; height: 352px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk9">class</span><span class="mtk1">&nbsp;Restoran</span><span class="mtk12">:</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">__init__</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk4">self</span><span class="mtk1">,&nbsp;</span><span class="mtk4">nama</span><span class="mtk1">,&nbsp;</span><span class="mtk4">jenis_makanan</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk12">:</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">self</span><span class="mtk1">.nama&nbsp;=&nbsp;nama</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">self</span><span class="mtk1">.jenis_makanan&nbsp;=&nbsp;jenis_makanan</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">self</span><span class="mtk1">.pelanggan&nbsp;=&nbsp;</span><span class="mtk6">0</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">info_restoran</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk4">self</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk12">:</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk9">f</span><span class="mtk5">"Restoran&nbsp;</span><span class="mtk12 bracket-highlighting-1">{</span><span class="mtk4">self</span><span class="mtk1">.nama</span><span class="mtk12 bracket-highlighting-1">}</span><span class="mtk5">&nbsp;menyajikan&nbsp;</span><span class="mtk12 bracket-highlighting-1">{</span><span class="mtk4">self</span><span class="mtk1">.jenis_makanan</span><span class="mtk12 bracket-highlighting-1">}</span><span class="mtk5">."</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk9">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">tambah_pelanggan</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk4">self</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk12">:</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">self</span><span class="mtk1">.pelanggan&nbsp;+=&nbsp;</span><span class="mtk6">1</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk9">f</span><span class="mtk5">"Pelanggan&nbsp;bertambah!&nbsp;Total&nbsp;pelanggan&nbsp;hari&nbsp;ini:&nbsp;</span><span class="mtk12 bracket-highlighting-1">{</span><span class="mtk4">self</span><span class="mtk1">.pelanggan</span><span class="mtk12 bracket-highlighting-1">}</span><span class="mtk5">"</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Membuat&nbsp;objek</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk1">restoran1&nbsp;=&nbsp;Restoran</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">"Sederhana"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"makanan&nbsp;Padang"</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">restoran1.info_restoran</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk1">restoran1.tambah_pelanggan</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk1">restoran1.tambah_pelanggan</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-0">)</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 689px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 171px; left: 215px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 1px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="visible scrollbar horizontal" style="position: absolute; width: 606px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 562px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="21" height="528" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 352px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 352px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 352px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 626px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 171px; left: 6px; width: 76992px; height: 1px;" data-has-listeners="true"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 626px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 352px;"><div class="minimap-shadow-hidden" style="height: 352px;"></div><canvas width="0" height="528" style="position: absolute; left: 0px; width: 0px; height: 352px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="528" style="position: absolute; left: 0px; width: 0px; height: 352px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1280px; top: 419.333px; left: 586.667px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical disabled" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal disabled" style="top: 8px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip" style="width: 0px; height: 0px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 500px; max-height: 250px; width: 0px; height: 0px;"><div class="hover-row markdown-hover"><div class="hover-contents code-hover-contents"><div class="rendered-markdown"><div data-code="id#14"><span style="font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px;"><div class="monaco-tokenized-source"><span class="mtk12">(</span><span class="mtk1">parameter</span><span class="mtk12">)</span><span class="mtk1"> </span><span class="mtk17">self</span><span class="mtk12">:</span><span class="mtk1"> Self</span><span class="mtk9">@Pesawat</span></div></span></div></div></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 0px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 10px; height: 0px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 0px;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Output sel 0" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Tindakan output sel kode" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tindakan output sel kode" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$--><svg viewBox="0 0 24 24"><!--?lit$105441083$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Tindakan output sel kode"><template shadowrootmode="open"><!----><!--?lit$105441083$--><!----><div><!--?lit$105441083$-->Tindakan output sel kode</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>Restoran Sederhana menyajikan makanan Padang.
Pelanggan bertambah! Total pelanggan hari ini: 1
Pelanggan bertambah! Total pelanggan hari ini: 2
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Tambahkan sel kode
Ctrl+M B" title="Tambahkan sel kode
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$105441083$--><button id="button" class="button" aria-label="Tambahkan sel kode
Ctrl+M B">
      <!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$105441083$-->Kode
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Tambahkan sel teks" title="Tambahkan sel teks" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$105441083$--><button id="button" class="button" aria-label="Tambahkan sel teks">
      <!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$105441083$-->Teks
        </md-outlined-button>
        <!--?lit$105441083$-->
      </div><hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Komentar" style="display: none;"></section></div>
          <!--?lit$105441083$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$105441083$-->Produk berbayar Colab
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$105441083$-->Batalkan kontrak di sini
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style=""></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$105441083$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$105441083$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Tindakan tab lainnya" data-aria-label="Tindakan tab lainnya" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tindakan tab lainnya" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize"><div class="resizer-thumb"></div>
        <!--?lit$105441083$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$105441083$--><colab-tab-pane class="layout vertical grow" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" aria-labelledby="tab-title-irOhmoh378kX" draggable="true" tabindex="0" class="selected-tab" md-tab="" active=""><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$105441083$--><div class="indicator"></div>
      </div>
      <!--?lit$105441083$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-irOhmoh378kX"><!--?lit$105441083$--><!--?lit$105441083$-->Catatan rilis<!--?--></span>
            <!--?lit$105441083$--><md-icon-button class="tab-close" data-aria-label="Tutup" title="Tutup" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tutup">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon></md-icon-button>
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$105441083$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Tindakan tab lainnya" data-aria-label="Tindakan tab lainnya" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tindakan tab lainnya" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow selected-tab relnotes-tab"><colab-shaded-scroller shade-bottom="" class="layout vertical grow" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 4px 4px -7px inset, rgba(0, 0, 0, 0.15) 0px -4px 4px -2px inset;">
        <div><span><p>Please follow our <a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab" target="_blank" rel="nofollow" aria-label="blog Link akan terbuka di tab baru">blog</a> to see more
information about new features, tips and tricks, and featured notebooks such as
<a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab%2Fnoteworthy-notebooks-3-analyzing-a-bank-failure-with-colab-d23b372de313" target="_blank" rel="nofollow" aria-label="Analyzing a Bank Failure with Colab Link akan terbuka di tab baru">Analyzing a Bank Failure with Colab</a>.</p>
<h3>2025-01-13</h3>
<ul>
<li>Released version 1.2.0 of the (<a href="https://github.com/googlecolab/open_in_colab" target="_blank" rel="nofollow" aria-label="Open in Colab Chrome Extension Link akan terbuka di tab baru">Open in Colab Chrome Extension</a>).</li>
<li>Released minimizable comments with indicators next to cell.</li>
<li>TPU v5e-1 Runtimes are now available for selection (<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1869458629230993619" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>).</li>
<li>GPU prices were decreased (<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1869458629230993619" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>).</li>
</ul>
<p>Python package upgrades</p>
<ul>
<li>accelerate 1.1.1 -&gt; 1.2.1</li>
<li>aiohttp 3.10.10 -&gt; 3.11.11</li>
<li>altair 4.2.2 -&gt; 5.5.0</li>
<li>bigframes 1.25.0 -&gt; 1.29.0</li>
<li>cmake 3.30.5 -&gt; 3.31.2</li>
<li>cvxpy 1.5.3 -&gt; 3.6.0</li>
<li>earthengine-api 1.2.0 -&gt; 1.4.3</li>
<li>folium 0.18.0 -&gt; 0.19.3</li>
<li>holidays 0.60 -&gt; 0.63</li>
<li>huggingface-hub 0.26.2 -&gt; 0.27.0</li>
<li>jsonpickle 3.4.2 -&gt; 4.0.1</li>
<li>kagglehub 0.3.3 -&gt; 0.3.6</li>
<li>keras 3.4.1 -&gt; 3.5.0</li>
<li>matplotlib 3.8.0 -&gt; 3.10.0</li>
<li>openai 1.54.3 -&gt; 1.57.4</li>
<li>pymc 5.18.0 -&gt; 5.19.1</li>
<li>safetensors 0.4.5 -&gt; 0.5.0</li>
<li>scikit-image 0.24.0 -&gt; 0.25.0</li>
<li>scikit-learn 1.5.2 -&gt; 1.6.0</li>
<li>sentence-transformers 3.2.1 -&gt; 3.3.1</li>
<li>tensorflow 2.17.0 -&gt; 2.17.1</li>
<li>torch 2.5.0 -&gt; 2.5.1</li>
<li>torchaudio 2.5.0 -&gt; 2.5.1</li>
<li>torchvision 0.20.0 -&gt; 0.20.1</li>
<li>transformers 4.46.2 -&gt; 4.47.1</li>
<li>wandb 0.18.6 -&gt; 0.19.1</li>
<li>xarray 2024.10.0 -&gt; 2024.11.0</li>
</ul>
<p>Python package inclusions</p>
<ul>
<li>google-genai 0.3.0</li>
</ul>
<h3>2024-11-11</h3>
<ul>
<li>Users can now import Gemini API keys from AI Studio into their user secrets,
all in Colab
(<a href="https://www.google.com/url?q=https%3A%2F%2Fx.com%2FOfficialLoganK%2Fstatus%2F1854584985849618812" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>).</li>
<li>Increased limit to 1000 characters for requests to Gemini in Chat and
Generate windows.</li>
<li>Improved saving notebook to GitHub flow.</li>
<li>Updated Gemini spark icon to be colorful.</li>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fdocs.astral.sh%2Fuv%2F" target="_blank" rel="nofollow" aria-label="uv Link akan terbuka di tab baru"><code>uv</code></a> is pre-installed on the PATH for faster
package installs.</li>
<li>Fixed bugs<ul>
<li>Dropdown text for GitHub repository not visible
<a href="https://github.com/googlecolab/colabtools/issues/4901" target="_blank" rel="nofollow" aria-label="#4901 Link akan terbuka di tab baru">#4901</a>.</li>
<li>Pre-installed California housing dataset README not correct
<a href="https://github.com/googlecolab/colabtools/issues/4862" target="_blank" rel="nofollow" aria-label="#4862 Link akan terbuka di tab baru">#4862</a>.</li>
<li>Backend execution error for scheduled notebook
<a href="https://github.com/googlecolab/colabtools/issues/4850" target="_blank" rel="nofollow" aria-label="#4850 Link akan terbuka di tab baru">#4850</a>.</li>
<li>Drive File Stream issues
<a href="https://github.com/googlecolab/colabtools/issues/3441" target="_blank" rel="nofollow" aria-label="#3441 Link akan terbuka di tab baru">#3441</a>.</li>
<li>Linking to the signup page does not preserve the authuser parameter.</li>
<li>Error messages in Gemini chat are not polished.</li>
<li>Clicking in Gemini chat feedback causes jitters the UI.</li>
<li>Hovering over a table of contents entry would show the menu icons for
all entries.</li>
<li>Surveys display over open dialogs.</li>
<li>Playground mode banner not shown on mobile.</li>
</ul>
</li>
</ul>
<p>Python package upgrades</p>
<ul>
<li>accelerate 0.34.2 -&gt; 1.1.1</li>
<li>arviz 0.19.0 -&gt; 0.20.0</li>
<li>bigframes 1.18.0 -&gt; 1.25.0</li>
<li>bigquery-magics 0.2.0 -&gt; 0.4.0</li>
<li>bokeh 3.4.3 -&gt; 3.6.1</li>
<li>blosc 2.0.0 -&gt; 2.7.1</li>
<li>cloudpickle 2.2.1 -&gt; 3.1.0</li>
<li>cudf-cu12 24.4.1 -&gt; 24.10.1</li>
<li>dask 2024.8.0 -&gt; 24.10.0</li>
<li>debugpy 1.6.6 -&gt; 1.8.0</li>
<li>earthengine-api 1.0.0 -&gt; 1.2.0</li>
<li>folium 0.17.0 -&gt; 0.18.0</li>
<li>gscfs 2024.6.1 -&gt; 2024.10.0</li>
<li>geemap 0.34.3 -&gt; 0.35.1</li>
<li>holidays 0.57 -&gt; 0.60</li>
<li>huggingface-hub 0.24.7 -&gt; 0.26.2</li>
<li>kagglehub 0.3.0 -&gt; 0.3.3</li>
<li>lightgbm 4.4.0 -&gt; 4.5.0</li>
<li>lxml 4.9.4 -&gt; 5.3.0</li>
<li>matplotlib 3.7.1 -&gt; 3.8.0</li>
<li>mizani 0.11.4 -&gt; 0.13.0</li>
<li>networkx 3.3 -&gt; 3.4.2</li>
<li>nltk 3.8.1 -&gt; 3.9.1</li>
<li>pandas 2.1.4 -&gt; 2.2.2</li>
<li>pillow 10.4.0 -&gt; 11.0.0</li>
<li>plotnine 0.13.6 -&gt; 0.14.1</li>
<li>polars 1.6.0 -&gt; 1.9.0</li>
<li>protobuf 3.20.3 -&gt; 4.25.5</li>
<li>pyarrow 14.0.2 -&gt; 17.0.0</li>
<li>pydrive2 1.20.0 -&gt; 1.21.1</li>
<li>pymc 5.16.2 -&gt; 5.18.0</li>
<li>torch 2.4.1 -&gt; 2.5.0</li>
<li>torchaudio 2.4.1 -&gt; 2.5.0</li>
<li>torchvision 0.19.1 -&gt; 0.20.0</li>
<li>transformers 4.44.2 -&gt; 4.46.2</li>
<li>xarray 2024.9.0 -&gt; 2024.10.0</li>
</ul>
<p>Python package inclusions</p>
<ul>
<li>diffusers 0.31.0</li>
<li>gitpython 3.1.43</li>
<li>langchain 0.3.7</li>
<li>openai 1.54.3</li>
<li>pygit2 1.16.0</li>
<li>pyspark 3.5.3</li>
<li>sentence-transformers 3.2.1</li>
<li>timm 1.0.11</li>
<li>wandb 0.18.6</li>
</ul>
<p>Library and driver upgrades</p>
<ul>
<li>drivefs upgraded from 89.0.2 to 98.0.0</li>
</ul>
<h3>2024-09-23</h3>
<ul>
<li>Improved code snippet search</li>
<li>Updated Marketplace image and public local runtime container</li>
<li>Improved the look-and-feel of interactive form dropdowns and checkboxes</li>
<li>Fixed bugs<ul>
<li>activating the skip link caused the notebook to scroll out of view</li>
<li>toggling a checkbox too much caused the page to crash</li>
<li>lightning fast drags could cause orphaned tabs</li>
<li>custom widgets snippet would show for local runtimes</li>
</ul>
</li>
</ul>
<p>Python package upgrades</p>
<ul>
<li>accelerate 0.32.1 -&gt; 0.34.2</li>
<li>arviz 0.18.0 -&gt; 0.19</li>
<li>autograd 1.6.2 -&gt; 1.7.0</li>
<li>bigframes 1.14.0 -&gt; 1.18.0</li>
<li>dask 2024.7.1 -&gt; 2024.8.0</li>
<li>distributed 2024.7.1 -&gt; 2024.8.0</li>
<li>duckdb 0.10.3 -&gt; 1.1.0</li>
<li>earthengine-api 0.1.416 -&gt; 1.0.0</li>
<li>flax 0.8.4 -&gt; 0.8.5</li>
<li>gdown 5.1.0 -&gt; 5.2.0</li>
<li>geemap 0.33.1 -&gt; 0.34.3</li>
<li>geopandas 0.14.4 -&gt; 1.0.1</li>
<li>google-cloud-aiplatform 1.59.0 -&gt; 1.67.1</li>
<li>google-cloud-bigquery-storage 2.25.0 -&gt; 2.26.0</li>
<li>holidays 0.54 -&gt; 0.57</li>
<li>huggingface-hub 0.23.5 -&gt; 0.24.7</li>
<li>ibis-framework 8.0.0 -&gt; 9.2.0</li>
<li>jax 0.4.26 -&gt; 0.4.33</li>
<li>jaxlib 0.4.26 -&gt; 0.4.33</li>
<li>kagglehub 0.2.9 -&gt; 0.3.0</li>
<li>lightgbm 4.4.0 -&gt; 4.5.0</li>
<li>matplotlib-venn 0.11.10 -&gt; 1.1.1</li>
<li>mizani 0.9.3 -&gt; 0.11.4</li>
<li>Pillow 9.4.0 -&gt; 10.4.0</li>
<li>plotly 5.15.0 -&gt; 5.24.1</li>
<li>plotnine 0.12.4 -&gt; 0.13.6</li>
<li>polars 0.20.2 -&gt; 1.6.0</li>
<li>progressbar2 4.2.0 -&gt; 4.5.0</li>
<li>PyDrive2 1.6.3 -&gt; 1.20.0</li>
<li>pymc 5.10.4 -&gt; 5.16.2</li>
<li>pytensor 2.18.6 -&gt; 2.25.4</li>
<li>scikit-image 0.23.2 -&gt; 0.24.0</li>
<li>scikit-learn 1.3.2 -&gt; 1.5.2</li>
<li>torch 2.3.1 -&gt; 2.4.1</li>
<li>torchaudio 2.3.1 -&gt; 2.4.1</li>
<li>torchvision 0.18.1 -&gt; 0.19.1</li>
<li>transformers 4.42.4 -&gt; 4.44.2</li>
<li>urllib3 2.0.7 -&gt; 2.2.3</li>
<li>xarray 2024.6.0 -&gt; 2024.9.0</li>
</ul>
<p>Python package inclusions</p>
<ul>
<li>bigquery-magics 0.2.0</li>
</ul>
<h3>2024-08-20</h3>
<ul>
<li><p>TPU memory usage and utilization can now be checked with <code>!tpu-info</code></p>
</li>
<li><p>Gemini Chat responses are now grounded in relevant sources</p>
</li>
<li><p>Added a new "Create Gemini API key" link in the user secrets panel</p>
</li>
<li><p>Added a new "Gemini: Creating a prompt" snippet and touched up the existing
"Gemini: Connecting to Gemini" snippet</p>
</li>
<li><p>Added the ability to specify custom placeholder text for various interactive
form params (see
<a href="https://colab.research.google.com/notebooks/forms.ipynb" target="_blank" rel="nofollow" aria-label="examples Link akan terbuka di tab baru">examples</a>)</p>
</li>
<li><p>Keyboard navigation a11y improvements to comments UI</p>
</li>
<li><p>Various minor rendering improvements to interactive forms UI</p>
</li>
<li><p>A11y improvements for the run button and header</p>
</li>
<li><p>Updated tooltip styling</p>
</li>
<li><p>A11y improvements for the file browser’s disk usage bar</p>
</li>
<li><p>On mobile, tooltips now trigger on long press</p>
</li>
<li><p>On mobile, release notes updates will no longer display automatically</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>astropy 5.3.4 -&gt; 6.1.2</li>
<li>bigframes 1.11.1 -&gt; 1.14.0</li>
<li>bokeh 3.3.4 -&gt; 3.4.3</li>
<li>dask 2023.8.1 -&gt; 2024.7.1</li>
<li>earthengine-api 0.1.412 -&gt; 0.1.416</li>
<li>geopandas 0.13.2 -&gt; 0.14.4</li>
<li>kagglehub 0.2.8 -&gt; 0.2.9</li>
<li>keras 2.15.0 -&gt; 3.4.1</li>
<li>lightgbm 4.1.0 -&gt; 4.4.0</li>
<li>malloy 2023.1067 -&gt; 2024.1067</li>
<li>numba 0.58.1 -&gt; 0.60.0</li>
<li>numpy 1.25.2 -&gt; 1.26.4</li>
<li>opencv-python 4.8.0.76 -&gt; 4.10.0.84</li>
<li>pandas 2.0.3 -&gt; 2.1.4</li>
<li>pandas-gbq 0.19.2 -&gt; 0.23.1</li>
<li>panel 1.3.8 -&gt; 1.4.5</li>
<li>requests 2.31.0 -&gt; 2.32.3</li>
<li>scikit-learn 1.2.2. -&gt; 1.3.2</li>
<li>scipy 1.11.4 -&gt; 1.13.1</li>
<li>tensorboard 2.15.2 -&gt; 2.17.0</li>
<li>tensorflow 2.15.0 -&gt; 2.17.0</li>
<li>tf-keras 2.15.1 -&gt; 2.17.0</li>
<li>xarray 2023.7.0 -&gt; 2024.6.0</li>
<li>xgboost 2.0.3 -&gt; 2.1.1</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>einops 0.8.0</li>
</ul>
</li>
</ul>
<h3>2024-07-22</h3>
<ul>
<li><p>You can now embed Google sheets directly into Colab to streamline interactions with data with InteractiveSheet.</p>
<p>Example:</p>
<pre><code><span><span class="mtk1">from&nbsp;google.colab&nbsp;import&nbsp;sheets</span></span><br><span><span class="mtk1">sh&nbsp;=&nbsp;sheets.InteractiveSheet()</span></span><br><span><span class="mtk1">df&nbsp;=&nbsp;sh.as_df()</span></span></code></pre></li>
<li><p>Fixed multiple rendering bugs in cell editors with wide text content (i.e. text is no longer hidden or clipped)</p>
</li>
<li><p>Fixed multiple accessibility issues in Colab's comments feature (e.g. proper keyboard focus management, added accessibility landmarks, etc)</p>
</li>
<li><p>Fixed bug where AI code generation would fail for extremely long broken code snippets</p>
</li>
<li><p>Fixed multiple scrollbar bugs in the user secrets panel</p>
</li>
<li><p>Added the ability for workspace admin to purchase Colab Pro and Pro+ Subscriptions for users</p>
</li>
<li><p>Fixed bug where user secrets couldn’t be moved to a tab</p>
</li>
<li><p>Fixed several focus management accessibility issues in tabs, the table of contents, the left toolbar, and the run button</p>
</li>
<li><p>Fixed bug where overflowing cells may be omitted when pasting from Google Sheets</p>
</li>
<li><p>Fixed bug where the generate code button did not activate on touch</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>bigframes 1.9.0 -&gt; 1.11.1</li>
<li>cvxpy 1.3.4 -&gt; 1.5.2</li>
<li>earthengine-api 0.1.408 -&gt; 0.1.412</li>
<li>google-api-core 2.11.1 -&gt; 2.19.1</li>
<li>google-api-python-client 2.84.0 -&gt; 2.137.0</li>
<li>google-cloud-aiplatform 1.56.0 -&gt; 1.59.0</li>
<li>google-cloud-bigquery 3.21.0 -&gt; 3.25.0</li>
<li>google-cloud-core 2.3.3 -&gt; 2.4.1</li>
<li>google-cloud-datastore 2.15.2 -&gt; 2.19.0</li>
<li>google-cloud-firestore 2.11.1 -&gt; 2.16.1</li>
<li>google-cloud-functions 1.13.3 -&gt; 1.16.4</li>
<li>google-generativeai 0.5.4 -&gt; 0.7.2</li>
<li>kagglehub 0.2.5 -&gt; 0.2.8</li>
<li>pip 23.1.2 -&gt; 24.1.2</li>
<li>setuptools 67.7.2 -&gt; 71.0.4</li>
<li>sympy 1.12.1 -&gt; 1.13.1</li>
<li>torch 2.3.0 -&gt; 2.3.1</li>
<li>transformers 4.41.2 -&gt; 4.42.4</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>accelerate 0.32.1</li>
</ul>
</li>
</ul>
<h3>2024-06-18</h3>
<ul>
<li><p>Inline AI completions are now available to users on the free-of-charge tier</p>
</li>
<li><p>Reduced latency for LSP and terminal connections</p>
</li>
<li><p>Improved quality of inline completions</p>
</li>
<li><p>Visual improvements to switch controls across Colab</p>
</li>
<li><p>Various bug fixes, performance and a11y improvements to the user secrets
panel</p>
</li>
<li><p>Improved tooltip UX behavior</p>
</li>
<li><p>Improved behavior when copying data from Google Sheets and pasting in Colab</p>
</li>
<li><p>Scroll to cell fixes for single tabbed view and jump to cell command</p>
</li>
<li><p>Improved tab header behavior</p>
</li>
<li><p>A11y improvements for notebook-focused cells</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>torch 2.2.1 -&gt; 2.3.0</li>
<li>torchaudio 2.2.1 -&gt; 2.3.0</li>
<li>torchvision 0.17.1 -&gt; 0.18.0</li>
<li>torchtext 0.17.1 -&gt; 0.18.0</li>
<li>google-cloud-aiplatform 1.51.0 -&gt; 1.56.0</li>
<li>bigframes 1.5.0 -&gt; 1.8.0</li>
<li>regex 2023.12.25 -&gt; 2024.5.15</li>
</ul>
</li>
</ul>
<h3>2024-05-13</h3>
<ul>
<li><p>Code actions are now supported to automatically improve and refactor code. Code actions can be triggered by the keyboard shortcut "Ctrl/⌘ + ."</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>bigframes 1.0.0 -&gt; 1.5.0</li>
<li>google-cloud-aiplatform 1.47.0 -&gt; 1.51.0</li>
<li>jax[tpu] 0.4.23 -&gt; 0.4.26</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>cudf 24.4.1</li>
</ul>
</li>
</ul>
<h3>2024-04-15</h3>
<ul>
<li><p>TPU v2 runtime is now available</p>
</li>
<li><p>L4 runtime is now available for paid users</p>
</li>
<li><p>New distributed fine-tuning Gemma tutorial on TPUs
(<a href="https://github.com/googlecolab/colabtools/blob/main/notebooks/Gemma_Distributed_Fine_tuning_on_TPU.ipynb" target="_blank" rel="nofollow" aria-label="GitHub Link akan terbuka di tab baru">GitHub</a>)</p>
</li>
<li><p>Symbol rename is now supported with keyboard shortcut F2</p>
</li>
<li><p>Fixed bug causing inability to re-upload deleted files</p>
</li>
<li><p>Fixed breaking bug in colabtools %upload_files_async</p>
</li>
<li><p>Added syntax highlighting to %%writefile cells</p>
</li>
<li><p>Cuda dependencies that come with Torch are cached for faster 
downloads for packages that require Torch and its dependencies (<a href="https://github.com/googlecolab/colabtools/issues/4491" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>bigframes 0.24.0 -&gt; 1.0.0</li>
<li>duckdb 0.9.2 -&gt; 0.10.1</li>
<li>google-cloud-aiplatform 1.43.0 -&gt; 1.47.0</li>
<li>jax 0.4.23 -&gt; 0.4.26</li>
</ul>
</li>
</ul>
<h3>2024-03-13</h3>
<ul>
<li><p>Fixed bug that sometimes caused UserSecrets to move / disappear</p>
</li>
<li><p>Improved messaging for mounting drive in an unsupported environment
(<a href="https://github.com/googlecolab/colabtools/issues/4375" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>torch 2.1.0 -&gt; 2.2.1</li>
<li>torchaudio 2.1.0 -&gt; 2.2.1</li>
<li>torchvision 0.16.0 -&gt; 0.17.1</li>
<li>torchtext 0.16.0 -&gt; 0.17.1</li>
<li>PyMC 5.7.2 -&gt; 5.10.4</li>
<li>BigFrames 0.21.0 -&gt; 0.24.0</li>
<li>google-cloud-aiplatform 1.42.1 -&gt; 1.43.0</li>
<li>tornado 6.3.2 -&gt; 6.3.3</li>
</ul>
</li>
</ul>
<h3>2024-02-21</h3>
<ul>
<li><p>Try out Gemma on
<a href="https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemma/docs/lora_tuning.ipynb" target="_blank" rel="nofollow" aria-label="Colab Link akan terbuka di tab baru">Colab</a>!</p>
</li>
<li><p>Allow unicode in form text inputs</p>
</li>
<li><p>Display documentation and link to source when displaying functions</p>
</li>
<li><p>Display image-like ndarrays as images</p>
</li>
<li><p>Improved UX around quick charts and execution error suggestions</p>
</li>
<li><p>Released Marketplace image for the month of February
(<a href="https://github.com/googlecolab/colabtools/issues/4254" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>bigframes 0.19.2 -&gt; 0.21.0</li>
<li>regex 2023.6.3 -&gt; 2023.12.25</li>
<li>spacy 3.6.1 -&gt; 3.7.4</li>
<li>beautifulsoup4 4.11.2 -&gt; 4.12.3</li>
<li>tensorflow-probability 0.22.0 -&gt; 0.23.0</li>
<li>google-cloud-language 2.9.1 -&gt; 2.13.1</li>
<li>google-cloud-aiplatform 1.39.0 -&gt; 1.42.1</li>
<li>transformers 4.35.2 -&gt; 4..37.2</li>
<li>pyarrow 10.0.1 -&gt; 14.0.2</li>
</ul>
</li>
</ul>
<h3>2024-01-29</h3>
<ul>
<li><p>New
<a href="https://www.google.com/url?q=https%3A%2F%2Fwww.kaggle.com%2Fdiscussions%2Fproduct-feedback%2F470030" target="_blank" rel="nofollow" aria-label="Kaggle Notebooks &lt;&gt; Colab updates Link akan terbuka di tab baru">Kaggle Notebooks &lt;&gt; Colab updates</a>!
Now you can:</p>
<ul>
<li>Import directly from Colab without having to download/re-upload</li>
<li>Upload via link, by pasting Google Drive or Colab URLs</li>
<li>Export &amp; run Kaggle Notebooks on Colab with 1 click</li>
</ul>
</li>
<li><p>Try these notebooks that talk to Gemini:</p>
<ul>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fgithub%2Fgooglecolab%2Fcolabtools%2Fblob%2Fmain%2Fnotebooks%2FGemini_and_Stable_Diffusion.ipynb" target="_blank" rel="nofollow" aria-label="Gemini and Stable Diffusion Link akan terbuka di tab baru">Gemini and Stable Diffusion</a></li>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fgithub%2Fgooglecolab%2Fcolabtools%2Fblob%2Fmain%2Fnotebooks%2FLearning_with_Gemini_and_ChatGPT.ipynb" target="_blank" rel="nofollow" aria-label="Learning with Gemini and ChatGPT Link akan terbuka di tab baru">Learning with Gemini and ChatGPT</a></li>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fgithub%2Fgooglecolab%2Fcolabtools%2Fblob%2Fmain%2Fnotebooks%2FTalk_to_Gemini_with_Google%2527s_Speech_to_Text_API.ipynb" target="_blank" rel="nofollow" aria-label="Talk to Gemini with Google&#39;s Speech to Text API Link akan terbuka di tab baru">Talk to Gemini with Google's Speech to Text API</a></li>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fgithub%2Fgooglecolab%2Fcolabtools%2Fblob%2Fmain%2Fnotebooks%2FSell_lemonade_with_Gemini_and_Sheets.ipynb" target="_blank" rel="nofollow" aria-label="Sell lemonade with Gemini and Sheets Link akan terbuka di tab baru">Sell lemonade with Gemini and Sheets</a></li>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fgithub%2Fgooglecolab%2Fcolabtools%2Fblob%2Fmain%2Fnotebooks%2FGenerate_images_with_Gemini_and_Vertex.ipynb" target="_blank" rel="nofollow" aria-label="Generate images with Gemini and Vertex Link akan terbuka di tab baru">Generate images with Gemini and Vertex</a></li>
</ul>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>google-cloud-aiplatform 1.38.1 -&gt; 1.39.0</li>
<li>bigframes 0.18.0 -&gt; 0.19.2</li>
<li>polars 0.17.3 -&gt; 0.20.2</li>
<li>gdown 4.6.6 -&gt; 4.7.3
(<a href="https://github.com/googlecolab/colabtools/issues/4298" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>tensorflow-hub 0.15.0 -&gt; 0.16.0</li>
<li>flax 0.7.5 -&gt; 0.8.0</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>sentencepiece 0.1.99</li>
</ul>
</li>
</ul>
<h3>2024-01-08</h3>
<ul>
<li><p>Avoid nested scrollbars for large outputs by using
<code>google.colab.output.no_vertical_scroll()</code>
<a href="https://colab.research.google.com/gist/blois/635d82605b163fc8fbb8ae1128c7f388/no_vertical_scroll.ipynb" target="_blank" rel="nofollow" aria-label="Example notebook Link akan terbuka di tab baru">Example notebook</a></p>
</li>
<li><p>Fix <a href="https://github.com/googlecolab/colabtools/issues/4272" target="_blank" rel="nofollow" aria-label="bug Link akan terbuka di tab baru">bug</a> where
downloading models from Hugging Face could freeze</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>huggingface-hub 0.19.4 -&gt; 0.20.2</li>
<li>bigframes 0.17.0 -&gt; 0.18.0</li>
</ul>
</li>
</ul>
<h3>2023-12-18</h3>
<ul>
<li><p>Expanded access to AI coding has arrived in Colab across 175 locales for all
tiers of Colab users</p>
</li>
<li><p>Improvements to display of ML-based inline completions (for eligible
Pro/Pro+ users)</p>
</li>
<li><p>Started a series of
<a href="https://github.com/googlecolab/colabtools/tree/main/notebooks" target="_blank" rel="nofollow" aria-label="notebooks Link akan terbuka di tab baru">notebooks</a>
highlighting Gemini API capabilities</p>
</li>
<li><p>Enable ⌘/Ctrl+L to select the full line in an editor</p>
</li>
<li><p>Fixed <a href="https://github.com/googlecolab/colabtools/issues/4174" target="_blank" rel="nofollow" aria-label="bug Link akan terbuka di tab baru">bug</a> where we
weren't correctly formatting output from multiple execution results</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>CUDA 11.8 to CUDA 12.2</li>
<li>tensorflow 2.14.0 -&gt; 2.15.0</li>
<li>tensorboard 2.14.0 -&gt; 2.15.0</li>
<li>keras 2.14.0 -&gt; 2.15.0</li>
<li>Nvidia drivers 525.105.17 -&gt; 535.104.05</li>
<li>tensorflow-gcs-config 2.14.0 -&gt; 2.15.0</li>
<li>bigframes 0.13.0 -&gt; 0.17.0</li>
<li>geemap 0.28.2 -&gt; 0.29.6</li>
<li>pyarrow 9.0.0 -&gt; 10.0.1</li>
<li>google-generativeai 0.2.2 -&gt; 0.3.1</li>
<li>jax 0.4.20 —&gt; 0.4.23</li>
<li>jaxlib 0.4.20 —&gt; 0.4.23</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>kagglehub 0.1.4</li>
<li>google-cloud-aiplatform 1.38.1</li>
</ul>
</li>
</ul>
<h3>2023-11-27</h3>
<ul>
<li><p>Removed warning when calling <code>await</code> to make it render as code</p>
</li>
<li><p>Added "Run selection" to the cell context menu</p>
</li>
<li><p>Added highlighting for the <code>%%python</code> cell magic</p>
</li>
<li><p>Launched AI coding features for Pro/Pro+ users in more locales</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>bigframes 0.12.0 -&gt; 0.13.0</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>transformers 4.35.2</li>
<li>google-generativeai 0.2.2</li>
</ul>
</li>
</ul>
<h3>2023-11-08</h3>
<ul>
<li><p>Launched Secrets, for safe storage of private keys on Colab
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1719798406195867814" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>)</p>
</li>
<li><p>Fixed issue where TensorBoard would not load
(<a href="https://github.com/googlecolab/colabtools/issues/3990" target="_blank" rel="nofollow" aria-label="#3990 Link akan terbuka di tab baru">#3990</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>lightgbm 4.0.0 -&gt; 4.1.0</li>
<li>bigframes 0.10.0 -&gt; 0.12.0</li>
<li>bokeh 3.2.2 -&gt; 3.3.0</li>
<li>duckdb 0.8.1 -&gt; 0.9.1</li>
<li>numba 0.56.4 -&gt; 0.58.1</li>
<li>tweepy 4.13.0 -&gt; 4.14.0</li>
<li>jax 0.4.16 -&gt; 0.4.20</li>
<li>jaxlib 0.4.16 -&gt; 0.4.20</li>
</ul>
</li>
</ul>
<h3>2023-10-23</h3>
<ul>
<li><p>Updated the <strong>Open notebook</strong> dialog for better usability and support for
smaller screen sizes</p>
</li>
<li><p>Added smart paste support for data from Google Sheets for R notebooks</p>
</li>
<li><p>Enabled showing release notes in a tab</p>
</li>
<li><p>Launched AI coding features for Pro/Pro+ users in Australia 🇦🇺 Canada 🇨🇦
India 🇮🇳 and Japan 🇯🇵
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1714322243659108376" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>)</p>
</li>
<li><p>Python package upgrades</p>
<ul>
<li>earthengine-api 0.1.357 -&gt; 0.1.375</li>
<li>flax 0.7.2 -&gt; 0.7.4</li>
<li>geemap 0.27.4 -&gt; 0.28.2</li>
<li>jax 0.4.14 -&gt; 0.4.16</li>
<li>jaxlib 0.4.14 -&gt; 0.4.16</li>
<li>keras 2.13.1 -&gt; 2.14.0</li>
<li>tensorboard 2.13.0 -&gt; 2.14.1</li>
<li>tensorflow 2.13.0 -&gt; 2.14.0</li>
<li>tensorflow-gcs-config 2.13.0 -&gt; 2.14.0</li>
<li>tensorflow-hub 0.14.0 -&gt; 0.15.0</li>
<li>tensorflow-probability 0.20.1 -&gt; 0.22.0</li>
<li>torch 2.0.1 -&gt; 2.1.0</li>
<li>torchaudio 2.0.2 -&gt; 2.1.0</li>
<li>torchtext 0.15.2 -&gt; 0.16.0</li>
<li>torchvision 0.15.2 -&gt; 0.16.0</li>
<li>xgboost 1.7.6 -&gt; 2.0.0</li>
</ul>
</li>
<li><p>Python package inclusions</p>
<ul>
<li>bigframes 0.10.0</li>
<li>malloy 2023.1056</li>
</ul>
</li>
</ul>
<h3>2023-09-22</h3>
<ul>
<li>Added the ability to scope an AI generated suggestion to a specific Pandas
dataframe
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1699880260056322462" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>)</li>
<li>Added Colab link previews to Docs
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1701684666972205243" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>)</li>
<li>Added smart paste support for data from Google Sheets</li>
<li>Increased font size of dropdowns in interactive forms</li>
<li>Improved rendering of the notebook when printing</li>
<li>Python package upgrades<ul>
<li>tensorflow 2.12.0 -&gt; 2.13.0</li>
<li>tensorboard 2.12.3 -&gt; 2.13.0</li>
<li>keras 2.12.0 -&gt; 2.13.1</li>
<li>tensorflow-gcs-config 2.12.0 -&gt; 2.13.</li>
<li>scipy 1.10.1-&gt; 1.11.2</li>
<li>cython 0.29.6 -&gt; 3.0.2</li>
</ul>
</li>
<li>Python package inclusions<ul>
<li>geemap 0.26.0</li>
</ul>
</li>
</ul>
<h3>2023-08-18</h3>
<ul>
<li>Added "Change runtime type" to the menu in the connection button</li>
<li>Improved auto-reconnection to an already running notebook
(<a href="https://github.com/googlecolab/colabtools/issues/3764" target="_blank" rel="nofollow" aria-label="#3764 Link akan terbuka di tab baru">#3764</a>)</li>
<li>Increased the specs of our highmem machines for Pro users</li>
<li>Fixed <code>add-apt-repository</code> command on Ubuntu 22.04 runtime
(<a href="https://github.com/googlecolab/colabtools/issues/3867" target="_blank" rel="nofollow" aria-label="#3867 Link akan terbuka di tab baru">#3867</a>)</li>
<li>Python package upgrades<ul>
<li>bokeh 2.4.3 -&gt; 3.2.2</li>
<li>cmake 3.25.2 -&gt; 3.27.2</li>
<li>cryptography 3.4.8 -&gt; 41.0.3</li>
<li>dask 2022.12.1 -&gt; 2023.8.0</li>
<li>distributed 2022.12.1 -&gt; 2023.8.0</li>
<li>earthengine-api 0.1.358 -&gt; 0.1.364</li>
<li>flax 0.7.0 -&gt; 0.7.2</li>
<li>ipython-sql 0.4.0 -&gt; 0.5.0</li>
<li>jax 0.4.13 -&gt; 0.4.14</li>
<li>jaxlib 0.4.13 -&gt; 0.4.14</li>
<li>lightgbm 3.3.5 -&gt; 4.0.0</li>
<li>mkl 2019.0 -&gt; 2023.2.0</li>
<li>notebook 6.4.8 -&gt; 6.5.5</li>
<li>numpy 1.22.4 -&gt; 1.23.5</li>
<li>opencv-python 4.7.0.72 -&gt; 4.8.0.76</li>
<li>pillow 8.4.0 -&gt; 9.4.0</li>
<li>plotly 5.13.1 -&gt; 5.15.0</li>
<li>prettytable 0.7.2 -&gt; 3.8.0</li>
<li>pytensor 2.10.1 -&gt; 2.14.2</li>
<li>spacy 3.5.4 -&gt; 3.6.1</li>
<li>statsmodels 0.13.5 -&gt; 0.14.0</li>
<li>xarray 2022.12.0 -&gt; 2023.7.0</li>
</ul>
</li>
<li>Python package inclusions<ul>
<li>PyDrive2 1.6.3</li>
</ul>
</li>
</ul>
<h3>2023-07-21</h3>
<ul>
<li><p>Launched auto-plotting for dataframes, available using the chart button that
shows up alongside datatables
(<a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab%2Fcolab-data-visualizations-made-easy-5e1918e5234e" target="_blank" rel="nofollow" aria-label="post Link akan terbuka di tab baru">post</a>)</p>
<img src="./class_Restoran.ipynb - Colab_files/chart_icon.png" alt="Chart button in Colab" width="40">
</li>
<li><p>Added a menu to the table of contents to support running a section or
collapsing/expanding sections
(<a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab%2Ftwo-new-ways-to-manage-cell-execution-fbad61b40882" target="_blank" rel="nofollow" aria-label="post Link akan terbuka di tab baru">post</a>)</p>
<img alt="Table of Contents running a section" src="./class_Restoran.ipynb - Colab_files/run_section.png" width="300">
</li>
<li><p>Added an option to automatically run the first cell or section, available
under Edit -&gt; Notebook settings
(<a href="https://www.google.com/url?q=https%3A%2F%2Fmedium.com%2Fgoogle-colab%2Ftwo-new-ways-to-manage-cell-execution-fbad61b40882" target="_blank" rel="nofollow" aria-label="post Link akan terbuka di tab baru">post</a>)</p>
<img alt="Run first cell option" src="./class_Restoran.ipynb - Colab_files/auto_run_first_cell.png" width="300">
</li>
<li><p>Launched Pro/Pro+ to Algeria, Argentina, Chile, Ecuador, Egypt, Ghana,
Kenya, Malaysia, Nepal, Nigeria, Peru, Rwanda, Saudi Arabia, South Africa,
Sri Lanka, Tunisia, and Ukraine
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1674412460017700866" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>)</p>
</li>
<li><p>Added a command, "Toggle tab moves focus" for toggling tab trapping in the
editor (Tools -&gt; Command palette, "Toggle tab moves focus")</p>
</li>
<li><p>Fixed issue where <code>files.upload()</code> was sometimes returning an incorrect
filename (<a href="https://github.com/googlecolab/colabtools/issues/1550" target="_blank" rel="nofollow" aria-label="#1550 Link akan terbuka di tab baru">#1550</a>)</p>
</li>
<li><p>Fixed f-string syntax highlighting bug
(<a href="https://github.com/googlecolab/colabtools/issues/3802" target="_blank" rel="nofollow" aria-label="#3802 Link akan terbuka di tab baru">#3802</a>)</p>
</li>
<li><p>Disabled ambiguous characters highlighting for commonly used LaTeX
characters (<a href="https://github.com/googlecolab/colabtools/issues/3648" target="_blank" rel="nofollow" aria-label="#3648 Link akan terbuka di tab baru">#3648</a>)</p>
</li>
<li><p>Upgraded Ubuntu from 20.04 LTS to
<a href="https://www.google.com/url?q=https%3A%2F%2Fdiscourse.ubuntu.com%2Ft%2Fjammy-jellyfish-release-notes%2F24668" target="_blank" rel="nofollow" aria-label="22.04 LTS Link akan terbuka di tab baru">22.04 LTS</a></p>
</li>
<li><p>Updated the Colab Marketplace VM image</p>
</li>
<li><p>Python package upgrades:</p>
<ul>
<li>autograd 1.6.1 -&gt; 1.6.2</li>
<li>drivefs 76.0 -&gt; 77.0</li>
<li>flax 0.6.11 -&gt; 0.7.0</li>
<li>earthengine-api 0.1.357 -&gt; 0.1.358</li>
<li>GDAL 3.3.2-&gt;3.4.3</li>
<li>google-cloud-bigquery-storage 2.20.0 -&gt; 2.22.2</li>
<li>gspread-dataframe 3.0.8 -&gt; 3.3.1</li>
<li>holidays 0.27.1 -&gt; 0.29</li>
<li>jax 0.4.10 -&gt; jax 0.4.13</li>
<li>jaxlib 0.4.10 -&gt; jax 0.4.13</li>
<li>jupyterlab-widgets 3.0.7 -&gt; 3.0.8</li>
<li>nbformat 5.9.0 -&gt; 5.9.1</li>
<li>opencv-python-headless 4.7.0.72 -&gt; 4.8.0.74</li>
<li>pygame 2.4.0 -&gt; 2.5.0</li>
<li>spacy 3.5.3 -&gt; 3.5.4</li>
<li>SQLAlchemy 2.0.16 -&gt; 2.0.19</li>
<li>tabulate 0.8.10 -&gt; 0.9.0</li>
<li>tensorflow-hub 0.13.0 -&gt; 0.14.0</li>
</ul>
</li>
</ul>
<h3>2023-06-23</h3>
<ul>
<li>Launched AI coding features to subscribed users starting with Pro+ users in
the US (<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1661056135196217346" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>,
<a href="https://www.google.com/url?q=https%3A%2F%2Fblog.google%2Ftechnology%2Fdevelopers%2Fgoogle-colab-ai-coding-features%2F" target="_blank" rel="nofollow" aria-label="post Link akan terbuka di tab baru">post</a>)</li>
<li>Added the Kernel Selector in the Notebook Settings
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1671265645756039168" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>)</li>
<li>Fixed double space trimming issue in markdown
<a href="https://github.com/googlecolab/colabtools/issues/3766" target="_blank" rel="nofollow" aria-label="#3766 Link akan terbuka di tab baru">#3766</a></li>
<li>Fixed run button indicator not always centered
<a href="https://github.com/googlecolab/colabtools/issues/3609" target="_blank" rel="nofollow" aria-label="#3609 Link akan terbuka di tab baru">#3609</a></li>
<li>Fixed inconsistencies for automatic indentation on multi-line
<a href="https://github.com/googlecolab/colabtools/issues/3697" target="_blank" rel="nofollow" aria-label="#3697 Link akan terbuka di tab baru">#3697</a></li>
<li>Upgraded Python from 3.10.11 to 3.10.12</li>
<li>Python package updates:<ul>
<li>duckdb 0.7.1 -&gt; 0.8.1</li>
<li>earthengine-api 0.1.350 -&gt; 0.1.357</li>
<li>flax 0.6.9 -&gt; 0.6.11</li>
<li>google-cloud-bigquery 3.9.0 -&gt; 3.10.0</li>
<li>google-cloud-bigquery-storage 2.19.1 -&gt; 2.20.0</li>
<li>grpcio 1.54.0 -&gt; 1.56.0</li>
<li>holidays 0.25 -&gt; 0.27.1</li>
<li>nbformat 5.8.0 -&gt; 5.9.0</li>
<li>prophet 1.1.3 -&gt; 1.1.4</li>
<li>pydata-google-auth 1.7.0 -&gt; 1.8.0</li>
<li>spacy 3.5.2 -&gt; 3.5.3</li>
<li>tensorboard 2.12.2 -&gt; 2.12.3</li>
<li>xgboost 1.7.5 -&gt; 1.7.6</li>
</ul>
</li>
<li>Python package inclusions:<ul>
<li>gcsfs 2023.6.0</li>
<li>geopandas 0.13.2</li>
<li>google-cloud-bigquery-connection 1.12.0</li>
<li>google-cloud-functions 1.13.0</li>
<li>grpc-google-iam-v1 0.12.6</li>
<li>multidict 6.0.4</li>
<li>tensorboard-data-server 0.7.1</li>
</ul>
</li>
</ul>
<h3>2023-06-02</h3>
<ul>
<li>Released the new site <a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.google" target="_blank" rel="nofollow" aria-label="colab.google Link akan terbuka di tab baru">colab.google</a></li>
<li>Published Colab's Docker runtime image to
us-docker.pkg.dev/colab-images/public/runtime
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1663594080436375558" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>,
<a href="https://www.google.com/url?q=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2Flocal-runtimes.html" target="_blank" rel="nofollow" aria-label="instructions Link akan terbuka di tab baru">instructions</a>)</li>
<li>Launched support for Google children accounts
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1661811016664231937" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>)</li>
<li>Launched DagsHub integration
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FTheRealDagsHub%2Fstatus%2F1658098271850749956" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>,
<a href="https://www.google.com/url?q=https%3A%2F%2Fdagshub.com%2Fblog%2Fgoogle-colab-integration%2F" target="_blank" rel="nofollow" aria-label="post Link akan terbuka di tab baru">post</a>)</li>
<li>Upgraded to Monaco Editor Version 0.37.1</li>
<li>Fixed various Vim keybinding bugs</li>
<li>Fixed issue where the N and P letters sometimes couldn't be typed
(<a href="https://github.com/googlecolab/colabtools/issues/3664" target="_blank" rel="nofollow" aria-label="#3664 Link akan terbuka di tab baru">#3664</a>)</li>
<li>Fixed rendering support for compositional inputs
(<a href="https://github.com/googlecolab/colabtools/issues/3660" target="_blank" rel="nofollow" aria-label="#3660 Link akan terbuka di tab baru">#3660</a>,
<a href="https://github.com/googlecolab/colabtools/issues/3660" target="_blank" rel="nofollow" aria-label="#3679 Link akan terbuka di tab baru">#3679</a>)</li>
<li>Fixed lag in notebooks with lots of cells
(<a href="https://github.com/googlecolab/colabtools/issues/3676" target="_blank" rel="nofollow" aria-label="#3676 Link akan terbuka di tab baru">#3676</a>)</li>
<li>Improved support for R by adding a Runtime type notebook setting (Edit -&gt;
Notebook settings)</li>
<li>Improved documentation for connecting to a local runtime (Connect -&gt; Connect
to a local runtime)</li>
<li>Python package updates:<ul>
<li>holidays 0.23 -&gt; 0.25</li>
<li>jax 0.4.8 -&gt; 0.4.10</li>
<li>jaxlib 0.4.8 -&gt; 0.4.10</li>
<li>pip 23.0.1 -&gt; 23.1.2</li>
<li>tensorflow-probability 0.19.0 -&gt; 0.20.1</li>
<li>torch 2.0.0 -&gt; 2.0.1</li>
<li>torchaudio 2.0.1 -&gt; 2.0.2</li>
<li>torchdata 0.6.0 -&gt; 0.6.1</li>
<li>torchtext 0.15.1 -&gt; 0.15.2</li>
<li>torchvision 0.15.1 -&gt; 0.15.2</li>
<li>tornado 6.2 -&gt; 6.3.1</li>
</ul>
</li>
</ul>
<h3>2023-05-05</h3>
<ul>
<li>Released GPU type selection for paid users, allowing them to choose a
preferred NVidia GPU</li>
<li>Upgraded R from 4.2.3 to 4.3.0</li>
<li>Upgraded Python from 3.9.16 to 3.10.11</li>
<li>Python package updates:<ul>
<li>attrs 22.2.0 -&gt; attrs 23.1.0</li>
<li>earthengine-api 0.1.349 -&gt; earthengine-api 0.1.350</li>
<li>flax 0.6.8 -&gt; 0.6.9</li>
<li>grpcio 1.53.0 -&gt; 1.54.0</li>
<li>nbclient 0.7.3 -&gt; 0.7.4</li>
<li>tensorflow-datasets 4.8.3 -&gt; 4.9.2</li>
<li>termcolor 2.2.0 -&gt; 2.3.0</li>
<li>zict 2.2.0 -&gt; 3.0.0</li>
</ul>
</li>
</ul>
<h3>2023-04-14</h3>
<ul>
<li>Python package updates:<ul>
<li>google-api-python-client 2.70.0 -&gt; 2.84.0</li>
<li>google-auth-oauthlib 0.4.6 -&gt; 1.0.0</li>
<li>google-cloud-bigquery 3.4.2 -&gt; 3.9.0</li>
<li>google-cloud-datastore 2.11.1 -&gt; 2.15.1</li>
<li>google-cloud-firestore 2.7.3 -&gt; 2.11.0</li>
<li>google-cloud-language 2.6.1 -&gt; 2.9.1</li>
<li>google-cloud-storage 2.7.0 -&gt; 2.8.0</li>
<li>google-cloud-translate 3.8.4 -&gt; 3.11.1</li>
<li>networkx 3.0 -&gt; 3.1</li>
<li>notebook 6.3.0 -&gt; 6.4.8</li>
<li>jax 0.4.7 -&gt; 0.4.8</li>
<li>pandas 1.4.4 -&gt; 1.5.3</li>
<li>spacy 3.5.1 -&gt; 3.5.2</li>
<li>SQLAlchemy 1.4.47 -&gt; 2.0.9</li>
<li>xgboost 1.7.4 -&gt; 1.7.5</li>
</ul>
</li>
</ul>
<h3>2023-03-31</h3>
<ul>
<li>Improve bash ! syntax highlighting
(<a href="https://github.com/googlecolab/colabtools/issues/3507" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Fix bug where VIM keybindings weren't working in the file editor</li>
<li>Upgraded R from 4.2.2 to 4.2.3</li>
<li>Python package updates:<ul>
<li>arviz 0.12.1 --&gt; 0.15.1</li>
<li>astropy 4.3.1 --&gt; 5.2.2</li>
<li>dopamine-rl 1.0.5 --&gt; 4.0.6</li>
<li>gensim 3.6.0 --&gt; 4.3.1</li>
<li>ipykernel 5.3.4 -&gt; 5.5.6</li>
<li>ipython 7.9.0 -&gt; 7.34.0</li>
<li>jax 0.4.4 -&gt; 0.4.7</li>
<li>jaxlib 0.4.4 -&gt; 0.4.7</li>
<li>jupyter_core 5.2.0 -&gt; 5.3.0</li>
<li>keras 2.11.0 -&gt; 2.12.0</li>
<li>lightgbm 2.2.3 -&gt; 3.3.5</li>
<li>matplotlib 3.5.3 -&gt; 3.7.1</li>
<li>nltk 3.7 -&gt; 3.8.1</li>
<li>opencv-python 4.6.0.66 -&gt; 4.7.0.72</li>
<li>plotly 5.5.0 -&gt; 5.13.1</li>
<li>pymc 4.1.4 -&gt; 5.1.2</li>
<li>seaborn 0.11.2 -&gt; 0.12.2</li>
<li>spacy 3.4.4 -&gt; 3.5.1</li>
<li>sympy 1.7.1 -&gt; 1.11.1</li>
<li>tensorboard 2.11.2 -&gt; 2.12.0</li>
<li>tensorflow 2.11.0 -&gt; 2.12.0</li>
<li>tensorflow-estimator 2.11.0 -&gt; 2.12.0</li>
<li>tensorflow-hub 0.12.0 -&gt; 0.13.0</li>
<li>torch 1.13.1 -&gt; 2.0.0</li>
<li>torchaudio 0.13.1 -&gt; 2.0.1</li>
<li>torchtext 0.14.1 -&gt; 0.15.1</li>
<li>torchvision 0.14.1 -&gt; 0.15.1</li>
</ul>
</li>
</ul>
<h3>2023-03-10</h3>
<ul>
<li>Added the
<a href="https://colab.research.google.com/notebooks/editor_shortcuts.ipynb" target="_blank" rel="nofollow" aria-label="Colab editor shortcuts Link akan terbuka di tab baru">Colab editor shortcuts</a>
example notebook</li>
<li>Fixed triggering of @-mention and email autocomplete for large comments
(<a href="https://github.com/googlecolab/colabtools/issues/3383" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Added View Resources to the Runtime menu</li>
<li>Made file viewer images fit the view by default, resizing to original size
on click</li>
<li>When in VIM mode, enable copy as well as allowing propagation to monaco-vim
to escape visual mode
(<a href="https://github.com/googlecolab/colabtools/issues/3414" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Upgraded CUDA 11.6.2 -&gt; 11.8.0 and cuDNN 8.4.0.27 -&gt; 8.7.0.84</li>
<li>Upgraded Nvidia drivers 525.78.01 -&gt; 530.30.02</li>
<li>Upgraded Python 3.8.10 -&gt; 3.9.16</li>
<li>Python package updates:<ul>
<li>beautifulsoup4 4.6.3 -&gt; 4.9.3</li>
<li>bokeh 2.3.3 -&gt; 2.4.3</li>
<li>debugpy 1.0.0 -&gt; 1.6.6</li>
<li>Flask 1.1.4 -&gt; 2.2.3</li>
<li>jax 0.3.25 -&gt; 0.4.4</li>
<li>jaxlib 0.3.25 -&gt; 0.4.4</li>
<li>Jinja2 2.11.3 -&gt; 3.1.2</li>
<li>matplotlib 3.2.2 -&gt; 3.5.3</li>
<li>nbconvert 5.6.1 -&gt; 6.5.4</li>
<li>pandas 1.3.5 -&gt; 1.4.4</li>
<li>pandas-datareader 0.9.0 -&gt; 0.10.0</li>
<li>pandas-profiling 1.4.1 -&gt; 3.2.0</li>
<li>Pillow 7.1.2 -&gt; 8.4.0</li>
<li>plotnine 0.8.0 -&gt; 0.10.1</li>
<li>scikit-image 0.18.3 -&gt; 0.19.3</li>
<li>scikit-learn 1.0.2 -&gt; 1.2.2</li>
<li>scipy 1.7.3 -&gt; 1.10.1</li>
<li>setuptools 57.4.0 -&gt; 63.4.3</li>
<li>sklearn-pandas 1.8.0 -&gt; 2.2.0</li>
<li>statsmodels 0.12.2 -&gt; 0.13.5</li>
<li>urllib3 1.24.3 -&gt; 1.26.14</li>
<li>Werkzeug 1.0.1 -&gt; 2.2.3</li>
<li>wrapt 1.14.1 -&gt; 1.15.0</li>
<li>xgboost 0.90 -&gt; 1.7.4</li>
<li>xlrd 1.2.0 -&gt; 2.0.1</li>
</ul>
</li>
</ul>
<h3>2023-02-17</h3>
<ul>
<li>Show graphs of RAM and disk usage in notebook toolbar</li>
<li>Copy cell links directly to the clipboard instead of showing a dialog when
clicking on the link icon in the cell toolbar</li>
<li>Updated the
<a href="https://www.google.com/url?q=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2Fmarketplace.html" target="_blank" rel="nofollow" aria-label="Colab Marketplace VM image Link akan terbuka di tab baru">Colab Marketplace VM image</a></li>
<li>Upgraded CUDA to 11.6.2 and cuDNN to 8.4.0.27</li>
<li>Python package updates:<ul>
<li>tensorflow 2.9.2 -&gt; 2.11.0</li>
<li>tensorboard 2.9.1 -&gt; 2.11.2</li>
<li>keras 2.9.0 -&gt; 2.11.0</li>
<li>tensorflow-estimator 2.9.0 -&gt; 2.11.0</li>
<li>tensorflow-probability 0.17.0 -&gt; 0.19.0</li>
<li>tensorflow-gcs-config 2.9.0 -&gt; 2.11.0</li>
<li>earthengine-api 0.1.339 -&gt; 0.1.341</li>
<li>flatbuffers 1.12 -&gt; 23.1.21</li>
<li>platformdirs 2.6.2 -&gt; 3.0.0</li>
<li>pydata-google-auth 1.6.0 -&gt; 1.7.0</li>
<li>python-utils 3.4.5 -&gt; 3.5.2</li>
<li>tenacity 8.1.0 -&gt; 8.2.1</li>
<li>tifffile 2023.1.23.1 -&gt; 2023.2.3</li>
<li>notebook 5.7.16 -&gt; 6.3.0</li>
<li>tornado 6.0.4 -&gt; 6.2</li>
<li>aiohttp 3.8.3 -&gt; 3.8.4</li>
<li>charset-normalizer 2.1.1 -&gt; 3.0.1</li>
<li>fastai 2.7.0 -&gt; 2.7.1</li>
<li>soundfile 0.11.0 -&gt; 0.12.1</li>
<li>typing-extensions 4.4.0 -&gt; 4.5.0</li>
<li>widgetsnbextension 3.6.1 -&gt; 3.6.2</li>
<li>pydantic 1.10.4 -&gt; 1.10.5</li>
<li>zipp 3.12.0 -&gt; 3.13.0</li>
<li>numpy 1.21.6 -&gt; 1.22.4</li>
<li>drivefs 66.0 -&gt; 69.0</li>
<li>gdal 3.0.4 -&gt; 3.3.2
<a href="https://github.com/googlecolab/colabtools/issues/3375" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a></li>
</ul>
</li>
<li>Added libudunits2-dev for smoother R package installs
<a href="https://github.com/googlecolab/colabtools/issues/2831" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a></li>
</ul>
<h3>2023-02-03</h3>
<ul>
<li>Improved tooltips for pandas series to show common statistics about the
series object</li>
<li>Made the forms dropdown behave like an autocomplete box when it allows input</li>
<li>Updated the nvidia driver from 460.32.03 to 510.47.03</li>
<li>Python package updates:<ul>
<li>absl-py 1.3.0 -&gt; 1.4.0</li>
<li>bleach 5.0.1 -&gt; 6.0.0</li>
<li>cachetools 5.2.1 -&gt; 5.3.0</li>
<li>cmdstanpy 1.0.8 -&gt; 1.1.0</li>
<li>dnspython 2.2.1 -&gt; 2.3.0</li>
<li>fsspec 2022.11.0 -&gt; 2023.1.0</li>
<li>google-cloud-bigquery-storage 2.17.0 -&gt; 2.18.1</li>
<li>holidays 0.18 -&gt; 0.19</li>
<li>jupyter-core 5.1.3 -&gt; 5.2.0</li>
<li>packaging 21.3 -&gt; 23.0</li>
<li>prometheus-client 0.15.0 -&gt; 0.16.0</li>
<li>pyct 0.4.8 -&gt; 0.5.0</li>
<li>pydata-google-auth 1.5.0 -&gt; 1.6.0</li>
<li>python-slugify 7.0.0 -&gt; 8.0.0</li>
<li>sqlalchemy 1.4.46 -&gt; 2.0.0</li>
<li>tensorflow-io-gcs-filesystem 0.29.0 -&gt; 0.30.0</li>
<li>tifffile 2022.10.10 -&gt; 2023.1.23.1</li>
<li>zipp 3.11.0 -&gt; 3.12.0</li>
<li>Pinned sqlalchemy to version 1.4.46</li>
</ul>
</li>
</ul>
<h3>2023-01-12</h3>
<ul>
<li>Added support for @-mention and email autocomplete in comments</li>
<li>Improved errors when GitHub notebooks can't be loaded</li>
<li>Increased color contrast for colors used for syntax highlighting in the code
editor</li>
<li>Added terminal access for custom GCE VM runtimes</li>
<li>Upgraded Ubuntu from 18.04 LTS to 20.04 LTS
(<a>GitHub issue</a>)</li>
<li>Python package updates:<ul>
<li>GDAL 2.2.2 -&gt; 2.2.3.</li>
<li>NumPy from 1.21.5 to 1.21.6.</li>
<li>attrs 22.1.0 -&gt; 22.2.0</li>
<li>chardet 3.0.4 -&gt; 4.0.0</li>
<li>cloudpickle 1.6.0 -&gt; 2.2.0</li>
<li>filelock 3.8.2 -&gt; 3.9.0</li>
<li>google-api-core 2.8.2 -&gt; 2.11.0</li>
<li>google-api-python-client 1.12.11 -&gt; 2.70.0</li>
<li>google-auth-httplib2 0.0.3 -&gt; 0.1.0</li>
<li>google-cloud-bigquery 3.3.5 -&gt; 3.4.1</li>
<li>google-cloud-datastore 2.9.0 -&gt; 2.11.0</li>
<li>google-cloud-firestore 2.7.2 -&gt; 2.7.3</li>
<li>google-cloud-storage 2.5.0 -&gt; 2.7.0</li>
<li>holidays 0.17.2 -&gt; holidays 0.18</li>
<li>importlib-metadata 5.2.0 -&gt; 6.0.0</li>
<li>networkx 2.8.8 -&gt; 3.0</li>
<li>opencv-python-headless 4.6.0.66 -&gt; 4.7.0.68</li>
<li>pip 21.1.3 -&gt; 22.04</li>
<li>pip-tools 6.2.0 -&gt; 6.6.2</li>
<li>prettytable 3.5.0 -&gt; 3.6.0</li>
<li>requests 2.23.0 -&gt; 2.25.1</li>
<li>termcolor 2.1.1 -&gt; 2.2.0</li>
<li>torch 1.13.0 -&gt; 1.13.1</li>
<li>torchaudio 0.13.0 -&gt; 0.13.1</li>
<li>torchtext 0.14.0-&gt; 0.14.1</li>
<li>torchvision 0.14.0 -&gt; 0.14.1</li>
</ul>
</li>
</ul>
<h3>2022-12-06</h3>
<ul>
<li>Made fallback runtime version available until mid-December
(<a href="https://github.com/googlecolab/colabtools/issues/3246" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Upgraded to Python 3.8
(<a href="https://github.com/googlecolab/colabtools/issues/3246" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Python package updates:<ul>
<li>jax from 0.3.23 to 0.3.25, jaxlib from 0.3.22 to 0.3.25</li>
<li>pyarrow from 6.0.1 to 9.0.0</li>
<li>torch from 1.12.1 to 1.13.0</li>
<li>torchaudio from 0.12.1 to 0.13.0</li>
<li>torchvision from 0.13.1 to 0.14.0</li>
<li>torchtext from 0.13.1 to 0.14.0</li>
<li>xlrd from 1.1.0 to 1.2.0</li>
<li>DriveFS from 62.0.1 to 66.0.3</li>
</ul>
</li>
<li>Made styling of markdown tables in outputs match markdown tables in text
cells</li>
<li>Improved formatting for empty interactive table rows</li>
<li>Fixed syntax highlighting for variables with names that contain Python
keywords
(<a href="https://github.com/googlecolab/colabtools/issues/3210" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
</ul>
<h3>2022-11-11</h3>
<ul>
<li>Added more dark editor themes for Monaco (when in dark mode, "Editor
colorization" appears as an option in the Editor tab of the Tools → Settings
dialog)</li>
<li>Fixed bug where collapsed forms were deleted on mobile
<a href="https://github.com/googlecolab/colabtools/issues/3153" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a></li>
<li>Python package updates:<ul>
<li>rpy2 from 3.4.0 to 3.5.5
(<a href="https://github.com/googlecolab/colabtools/issues/3180" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>notebook from 5.5.0 to 5.7.16</li>
<li>tornado from 5.1.1 to 6.0.4</li>
<li>tensorflow_probability from 0.16.0 to 0.17.0</li>
<li>pandas-gbq from 0.13.3 to 0.17.9</li>
<li>protobuf from 3.17.3 to 3.19.6</li>
<li>google-api-core[grpc] from 1.31.5 to 2.8.2</li>
<li>google-cloud-bigquery from 1.21.0 to 3.3.5</li>
<li>google-cloud-core from 1.0.1 to 2.3.2</li>
<li>google-cloud-datastore from 1.8.0 to 2.9.0</li>
<li>google-cloud-firestore from 1.7.0 to 2.7.2</li>
<li>google-cloud-language from 1.2.0 to 2.6.1</li>
<li>google-cloud-storage from 1.18.0 to 2.5.0</li>
<li>google-cloud-translate from 1.5.0 to 3.8.4</li>
</ul>
</li>
</ul>
<h3>2022-10-21</h3>
<ul>
<li>Launched a single-click way to get from BigQuery to Colab to further explore
query results
(<a href="https://www.google.com/url?q=https%3A%2F%2Fcloud.google.com%2Fbigquery%2Fdocs%2Fexplore-data-colab" target="_blank" rel="nofollow" aria-label="announcement Link akan terbuka di tab baru">announcement</a>)</li>
<li>Launched
<a href="https://colab.research.google.com/signup" target="_blank" rel="nofollow" aria-label="Pro, Pro+, and Pay As You Go Link akan terbuka di tab baru">Pro, Pro+, and Pay As You Go</a> to
19 additional countries: Austria, Belgium, Bulgaria, Croatia, Cyprus,
Czechia, Denmark, Estonia, Finland, Greece, Hungary, Latvia, Lithuania,
Norway, Portugal, Romania, Slovakia, Slovenia, and Sweden
(<a href="https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2FGoogleColab%2Fstatus%2F1579956393834344449" target="_blank" rel="nofollow" aria-label="tweet Link akan terbuka di tab baru">tweet</a>)</li>
<li>Updated jax from 0.3.17 to 0.3.23, jaxlib from 0.3.15 to 0.3.22, TensorFlow
from 2.8.2 to 2.9.2, CUDA from 11.1 to 11.2, and cuDNN from 8.0 to 8.1
(<a href="https://github.com/googlecolab/backend-info" target="_blank" rel="nofollow" aria-label="backend-info Link akan terbuka di tab baru">backend-info</a>)</li>
<li>Added a <code>readonly</code> option to
<a href="https://github.com/googlecolab/colabtools/blob/main/google/colab/drive.py#L99" target="_blank" rel="nofollow" aria-label="drive.mount Link akan terbuka di tab baru"><code>drive.mount</code></a></li>
<li>Fixed bug where Xarray was not working
(<a href="https://github.com/googlecolab/colabtools/issues/3134" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Modified Markdown parsing to ignore block quote symbol within MathJax
(<a href="https://github.com/googlecolab/colabtools/issues/3118" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
</ul>
<h3>2022-09-30</h3>
<ul>
<li>Launched <a href="https://colab.research.google.com/signup" target="_blank" rel="nofollow" aria-label="Pay As You Go Link akan terbuka di tab baru">Pay As You Go</a>, allowing
premium GPU access without requiring a subscription</li>
<li>Added vim and tcllib to our runtime image</li>
<li>Fixed bug where open files were closed on kernel disconnect
(<a href="https://github.com/googlecolab/colabtools/issues/1716" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Fixed bug where the play button/execution indicator was not clickable when
scrolled into the cell output
(<a href="https://github.com/googlecolab/colabtools/issues/3068" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Updated the styling for form titles so that they avoid obscuring the code
editor</li>
<li>Created a GitHub repo,
<a href="https://github.com/googlecolab/backend-info" target="_blank" rel="nofollow" aria-label="backend-info Link akan terbuka di tab baru">backend-info</a>, with the latest
apt-list.txt and pip-freeze.txt files for the Colab runtime
(<a href="https://github.com/googlecolab/colabtools/issues/1445" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Added
<a href="https://github.com/googlecolab/colabtools/blob/main/google/colab/files.py#L33" target="_blank" rel="nofollow" aria-label="files.upload_file(filename) Link akan terbuka di tab baru"><code>files.upload_file(filename)</code></a>
to upload a file from the browser to the runtime with a specified filename</li>
</ul>
<h3>2022-09-16</h3>
<ul>
<li>Upgraded pymc from 3.11.0 to 4.1.4, jax from 0.3.14 to 0.3.17, jaxlib from
0.3.14 to 0.3.15, fsspec from 2022.8.1 to 2022.8.2</li>
<li>Modified our save flow to avoid persisting Drive filenames as titles in
notebook JSON</li>
<li>Updated our <a href="https://colab.research.google.com/pro/terms" target="_blank" rel="nofollow" aria-label="Terms of Service Link akan terbuka di tab baru">Terms of Service</a></li>
<li>Modified the <code>Jump to Cell</code> command to locate the cursor at the end of the
command palette input (<code>Jump to cell</code> in Tools → Command palette in a
notebook with section headings)</li>
<li>Updated the styling of the Drive notebook comment UI</li>
<li>Added support for terminating your runtime from code: <code>python from
google.colab import runtime runtime.unassign()</code></li>
<li>Added regex filter support to the Recent notebooks dialog</li>
<li>Inline google.colab.files.upload JS to fix <code>files.upload()</code> not working
(<a href="https://github.com/googlecolab/colabtools/issues/51" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
</ul>
<h3>2022-08-26</h3>
<ul>
<li>Upgraded PyYAML from 3.13 to 6.0
(<a href="https://github.com/googlecolab/colabtools/issues/2942" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>),
drivefs from 61.0.3 to 62.0.1</li>
<li>Upgraded TensorFlow from 2.8.2 to 2.9.1 and ipywidgets from 7.7.1 to 8.0.1
but rolled both back due to a number of user reports
(<a href="https://github.com/googlecolab/colabtools/issues/3008" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>,
<a href="https://github.com/googlecolab/colabtools/issues/3020#issuecomment-1223330253" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Stop persisting inferred titles in notebook JSON
(<a href="https://github.com/googlecolab/colabtools/issues/764" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Fix bug in background execution which affected some Pro+ users
(<a href="https://github.com/googlecolab/colabtools/issues/2991" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Fix bug where <code>Download as .py</code> incorrectly handled text cells ending in a
double quote</li>
<li>Fix bug for Pro and Pro+ users where we weren't honoring the preference
(Tools → Settings) to use a temporary scratch notebook as the default
landing page</li>
<li>Provide undo/redo for scratch cells</li>
<li>When writing ipynb files, serialize empty multiline strings as <code>[]</code> for
better consistency with JupyterLab</li>
</ul>
<h3>2022-08-11</h3>
<ul>
<li>Upgraded ipython from 5.5.0 to 7.9.0, fbprophet 0.7 to prophet 1.1,
tensorflow-datasets from 4.0.1 to 4.6.0, drivefs from 60.0.2 to 61.0.3,
pytorch from 1.12.0 to 1.12.1, numba from 0.51 to 0.56, and lxml from 4.2.0
to 4.9.1</li>
<li>Loosened our <code>requests</code> version requirement
(<a href="https://github.com/deepset-ai/haystack/pull/2921#issuecomment-1199714337" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Removed support for TensorFlow 1</li>
<li>Added Help → Report Drive abuse for Drive notebooks</li>
<li>Fixed indentation for Python lines ending in <code>[</code></li>
<li>Modified styling of tables in Markdown to left-align them rather than
centering them</li>
<li>Fixed special character replacement when copying interactive tables as
Markdown</li>
<li>Fixed ansi 8-bit color parsing
(<a href="https://github.com/googlecolab/colabtools/issues/2963" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Configured logging to preempt transitive imports and other loading from
implicitly configuring the root logger</li>
<li>Modified forms to use a value of <code>None</code> instead of causing a parse error
when clearing raw and numeric-typed form fields</li>
</ul>
<h3>2022-07-22</h3>
<ul>
<li>Update scipy from 1.4.1 to 1.7.3, drivefs from 59.0.3 to 60.0.2, pytorch
from 1.11 to 1.12, jax &amp; jaxlib from 0.3.8 to 0.3.14, opencv-python from
4.1.2.30 to 4.6.0.66, spaCy from 3.3.1 to 3.4.0, and dlib from 19.18.0 to
19.24.0</li>
<li>Fix <code>Open in tab</code> doc link which was rendering incorrectly
(<a href="https://github.com/googlecolab/colabtools/issues/2690" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>)</li>
<li>Add a preference for the default tab orientation to the Site section of the
settings menu under Tools → Settings</li>
<li>Show a warning for <code>USE_AUTH_EPHEM</code> usage when running authenticate_user on
a TPU runtime
(<a href="https://github.com/googlecolab/colabtools/blob/main/google/colab/auth.py#L243" target="_blank" rel="nofollow" aria-label="code Link akan terbuka di tab baru">code</a>)</li>
</ul>
<h3>2022-07-01</h3>
<ul>
<li>Add a preference for code font to the settings menu under Tools → Settings</li>
<li>Update drivefs from 58.0.3 to 59.0.3 and spacy from 2.2.4 to 3.3.1</li>
<li>Allow
<a href="https://www.google.com/url?q=https%3A%2F%2Fipython.org%2Fipython-doc%2F3%2Fnotebook%2Fnbformat.html%23display-data" target="_blank" rel="nofollow" aria-label="display_data Link akan terbuka di tab baru">display_data</a>
and
<a href="https://www.google.com/url?q=https%3A%2F%2Fipython.org%2Fipython-doc%2F3%2Fnotebook%2Fnbformat.html%23execute-result" target="_blank" rel="nofollow" aria-label="execute_result Link akan terbuka di tab baru">execute_result</a>
text outputs to wrap, matching behavior of JupyterLab (does not affect
stream outputs/print statements).</li>
<li>Improve LSP handling of some magics, esp. %%writefile
(<a href="https://github.com/googlecolab/colabtools/issues/2859" target="_blank" rel="nofollow" aria-label="GitHub issue Link akan terbuka di tab baru">GitHub issue</a>).</li>
<li>Add a
<a href="https://www.google.com/url?q=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2Ffaq.html%23drive-mount-code-cell" target="_blank" rel="nofollow" aria-label="FAQ entry Link akan terbuka di tab baru">FAQ entry</a>
about the mount Drive button behavior and include link buttons for each FAQ
entry.</li>
<li>Fix bug where the notebook was sometimes hidden behind other tabs on load
when in single pane view.</li>
<li>Fix issue with inconsistent scrolling when an editor is in multi-select
mode.</li>
<li>Fix bug where clicking on a link in a form would navigate away from the
notebook</li>
<li>Show a confirmation dialog before performing Replace all from the Find and
replace pane.</li>
</ul>
<h3>2022-06-10</h3>
<ul>
<li>Update drivefs from 57.0.5 to 58.0.3 and tensorflow from 2.8.0 to 2.8.2</li>
<li>Support more than 100 repos in the GitHub repo selector shown in the open
dialog and the clone to GitHub dialog</li>
<li>Show full notebook names on hover in the open dialog</li>
<li>Improve the color contrast for links, buttons, and the
<code>ipywidgets.Accordion</code> widget in dark mode</li>
</ul>
<h3>2022-05-20</h3>
<ul>
<li>Support URL params for linking to some common pref settings:
<a href="https://colab.research.google.com/?force_theme=dark" target="_blank" rel="nofollow" aria-label="force_theme=dark Link akan terbuka di tab baru">force_theme=dark</a>,
<a href="https://colab.research.google.com/?force_corgi_mode=1" target="_blank" rel="nofollow" aria-label="force_corgi_mode=1 Link akan terbuka di tab baru">force_corgi_mode=1</a>,
<a href="https://colab.research.google.com/?force_font_size=14" target="_blank" rel="nofollow" aria-label="force_font_size=14 Link akan terbuka di tab baru">force_font_size=14</a>.
Params forced by URL are not persisted unless saved using Tools → Settings.</li>
<li>Add a class <code>markdown-google-sans</code> to allow
<span class="markdown-google-sans">Markdown to render in Google Sans</span></li>
<li>Update monaco-vim from 0.1.19 to 0.3.4</li>
<li>Update drivefs from 55.0.3 to 57.0.5, jax from 0.3.4 to 0.3.8, and jaxlib
from 0.3.2 to 0.3.7</li>
</ul>
<h3>2022-04-29</h3>
<ul>
<li>Added 🦀 mode (under Miscellaneous in Tools → Settings)</li>
<li>Added "Disconnect and delete runtime" option to the menu next to the Connect
button</li>
<li>Improved rendering of filter options in an interactive table</li>
<li>Added git-lfs to the base image</li>
<li>Updated torch from 1.10.0 to 1.11.0, jupyter-core from 4.9.2 to 4.10.0, and
cmake from 3.12.0 to 3.22.3</li>
<li>Added more details to our
<a href="https://www.google.com/url?q=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2Ffaq.html" target="_blank" rel="nofollow" aria-label="FAQ Link akan terbuka di tab baru">FAQ</a> about unsupported
uses (using proxies, downloading torrents, etc.)</li>
<li>Fixed <a href="https://github.com/googlecolab/colabtools/issues/2779" target="_blank" rel="nofollow" aria-label="issue Link akan terbuka di tab baru">issue</a> with
apt-get dependencies</li>
</ul>
<h3>2022-04-15</h3>
<ul>
<li>Add an option in the file browser to show hidden files.</li>
<li>Upgrade gdown from 4.2.0 to 4.4.0, google-api-core[grpc] from 1.26.0 to
1.31.5, and pytz from 2018.4 to 2022.1</li>
</ul>
<h3>2022-03-25</h3>
<ul>
<li>Launched
<a href="https://colab.research.google.com/signup?utm_source=relnotes&amp;utm_medium=link&amp;utm_campaign=additional_countries" target="_blank" rel="nofollow" aria-label="Pro/Pro+ Link akan terbuka di tab baru">Pro/Pro+</a>
to 12 additional countries: Australia, Bangladesh, Colombia, Hong Kong,
Indonesia, Mexico, New Zealand, Pakistan, Philippines, Singapore, Taiwan,
and Vietnam</li>
<li>Added
<a href="https://github.com/googlecolab/colabtools/blob/main/google/colab/auth.py#L253" target="_blank" rel="nofollow" aria-label="google.colab.auth.authenticate_service_account() Link akan terbuka di tab baru"><code>google.colab.auth.authenticate_service_account()</code></a>
to support using
<a href="https://www.google.com/url?q=https%3A%2F%2Fcloud.google.com%2Fiam%2Fdocs%2Fcreating-managing-service-account-keys%23iam-service-account-keys-create-console" target="_blank" rel="nofollow" aria-label="Service Account keys Link akan terbuka di tab baru">Service Account keys</a></li>
<li>Update jax from 0.3.1 to 0.3.4 &amp; jaxlib from 0.3.0 to 0.3.2</li>
<li>Fixed an issue with Twitter previews of notebooks shared as GitHub Gists</li>
</ul>
<h3>2022-03-10</h3>
<ul>
<li>Launched
<a href="https://colab.research.google.com/signup?utm_source=relnotes&amp;utm_medium=link&amp;utm_campaign=additional_countries" target="_blank" rel="nofollow" aria-label="Pro/Pro+ Link akan terbuka di tab baru">Pro/Pro+</a>
to 10 new countries: Ireland, Israel, Italy, Morocco, the Netherlands,
Poland, Spain, Switzerland, Turkey, and the United Arab Emirates</li>
<li>Launched support for
<a href="https://github.com/googlecolab/colabtools/wiki/Scheduled-notebooks" target="_blank" rel="nofollow" aria-label="scheduling notebooks for Pro+ users Link akan terbuka di tab baru">scheduling notebooks for Pro+ users</a></li>
<li>Fixed bug in interactive datatables where filtering by number did not work</li>
<li>Finished removing the python2 kernelspec</li>
</ul>
<h3>2022-02-25</h3>
<ul>
<li>Made various accessibility improvements to the header</li>
<li>Fix bug with
<a href="https://www.google.com/url?q=https%3A%2F%2Fcolab.sandbox.google.com%2Fnotebooks%2Fforms.ipynb%23scrollTo%3Dh9aZYKhly2h_" target="_blank" rel="nofollow" aria-label="forms run:auto Link akan terbuka di tab baru">forms run:auto</a>
where a form field change would trigger multiple runs</li>
<li>Minor updates to the
<a href="https://colab.research.google.com/notebooks/bigquery.ipynb" target="_blank" rel="nofollow" aria-label="bigquery example notebook Link akan terbuka di tab baru">bigquery example notebook</a>
and snippet</li>
<li>Include background execution setting in the sessions dialog for Pro+ users</li>
<li>Update tensorflow-probability from 0.15 to 0.16</li>
<li>Update jax from 0.2.25 to 0.3.1 &amp; jaxlib from 0.1.71 to 0.3.0</li>
</ul>
<h3>2022-02-11</h3>
<ul>
<li>Improve keyboard navigation for the open dialog</li>
<li>Fix issue where nvidia-smi stopped reporting resource utilization for some
users who were modifying the version of nvidia used</li>
<li>Update tensorflow from 2.7 to 2.8, keras from 2.7 to 2.8, numpy from 1.19.5
to 1.21.5, tables from 3.4.4 to 3.7.0</li>
</ul>
<h3>2022-02-04</h3>
<ul>
<li>Improve UX for opening content alongside your notebook, such as files opened
from the file browser. This includes a multi-pane view and drag-drop support</li>
<li>Better Twitter previews when sharing example Colab notebooks and notebooks
opened from GitHub Gists</li>
<li>Update pandas from 1.1.5 to 1.3.5</li>
<li>Update openpyxl from 2.5.9 to 3.0.0 and pyarrow from 3.0.0 to 6.0.0</li>
<li>Link to the release notes from the Help menu</li>
</ul>
<h3>2022-01-28</h3>
<ul>
<li>Add a copy button to
<a href="https://colab.research.google.com/notebooks/data_table.ipynb" target="_blank" rel="nofollow" aria-label="data tables Link akan terbuka di tab baru">data tables</a></li>
<li>Python LSP support for better completions and code diagnostics. This can be
configured in the Editor Settings (Tools → Settings)</li>
<li>Update
<a href="https://colab.research.google.com/notebooks/io.ipynb#scrollTo=sOm9PFrT8mGG" target="_blank" rel="nofollow" aria-label="gspread examples Link akan terbuka di tab baru">gspread examples</a>
in our documentation</li>
<li>Update gdown from 3.6 to 4.2</li>
</ul>
<h3>2022-01-21</h3>
<ul>
<li>New documentation for the
<a href="https://colab.research.google.com/notebooks/google.colab.ipynb" target="_blank" rel="nofollow" aria-label="google.colab package Link akan terbuka di tab baru"><code>google.colab</code> package</a></li>
<li>Show GPU RAM in the resource usage tab</li>
<li>Improved security for mounting Google Drive which disallows mounting Drive
from accounts other than the one currently executing the notebook</li>
</ul>
<h3>2022-01-14</h3>
<ul>
<li>Add a preference (Tools → Settings) to use a temporary scratch notebook as
the default landing page</li>
<li>Fix bug where <code>/</code> and <code>:</code> weren't working in VIM mode</li>
<li>Update gspread from 3.0 to 3.4</li>
<li>Update the
<a href="https://www.google.com/url?q=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2Fmarketplace.html" target="_blank" rel="nofollow" aria-label="Colab Marketplace VM image Link akan terbuka di tab baru">Colab Marketplace VM image</a></li>
</ul>
</span></div></colab-shaded-scroller></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$105441083$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$105441083$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Tindakan tab lainnya" data-aria-label="Tindakan tab lainnya" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tindakan tab lainnya" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./class_Restoran.ipynb - Colab_files/outputframe.html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./class_Restoran.ipynb - Colab_files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-status-bar role="region" aria-label="Status bar runtime" style="min-height: inherit;"><template shadowrootmode="open"><!----><!--?lit$105441083$--> <!--?lit$105441083$--> <div class="cell-status">
        <button><!--?lit$105441083$--><md-icon class="success" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$--><svg viewBox="0 0 24 24"><!--?lit$105441083$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>&nbsp; <!--?lit$105441083$-->0 d</button>
        <button><!--?lit$105441083$-->selesai pada 22.37</button>
      </div>
      <md-icon-button class="visible-on-closed" title="Terhubung" disabled="" value="" data-aria-label="Terhubung"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Terhubung" disabled="">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" class="visible-on-closed" status="icon-okay" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$105441083$-->fiber_manual_record</md-icon>
      </md-icon-button>
      <!--?lit$105441083$-->
      <md-icon-button title="Tutup" data-aria-label="Tutup" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Tutup">
        <!--?lit$105441083$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$105441083$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$105441083$--><span class="icon"><slot></slot></span>
        <!--?lit$105441083$-->
        <!--?lit$105441083$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button></template></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$105441083$--><div command="locate-in-drive" class=" goog-menuitem " role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Temukan di Drive<!--?lit$105441083$--></div></div><div command="open-in-playground" class=" goog-menuitem " role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Buka dalam mode playground<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class=" goog-menuitem " role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Notebook baru di Drive<!--?lit$105441083$--></div></div><div command="open" class=" goog-menuitem " role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Buka notebook<!--?lit$105441083$--></div></div><div command="import-notebook" class=" goog-menuitem " role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Upload notebook<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class=" goog-menuitem " role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Ganti nama<!--?lit$105441083$--></div></div><div command="move-notebook" class=" goog-menuitem " role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Pindahkan<!--?lit$105441083$--></div></div><div command="trash" class=" goog-menuitem " role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Pindahkan ke sampah<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class=" goog-menuitem " role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Simpan salinan di Drive<!--?lit$105441083$--></div></div><div command="copy-to-gist" class=" goog-menuitem " role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Simpan salinan sebagai Gist GitHub<!--?lit$105441083$--></div></div><div command="copy-to-github" class=" goog-menuitem " role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Simpan salinan di GitHub<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class=" goog-menuitem " role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Simpan<!--?lit$105441083$--></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Simpan dan pasang pin pada revisi<!--?lit$105441083$--></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Histori revisi<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":k" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$105441083$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Cetak<!--?lit$105441083$--></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$105441083$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Download .ipynb<!--?lit$105441083$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Download .py<!--?lit$105441083$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$105441083$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Urungkan<!--?lit$105441083$--></div></div><div command="redo" class=" goog-menuitem " role="menuitem" id=":r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Ulangi<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Pilih semua sel<!--?lit$105441083$--></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Potong sel atau pilihan<!--?lit$105441083$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Salin sel atau pilihan<!--?lit$105441083$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Tempel<!--?lit$105441083$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Hapus sel yang dipilih<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Cari dan ganti<!--?lit$105441083$--></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Cari berikutnya<!--?lit$105441083$--></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Cari sebelumnya<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":12" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Setelan notebook<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Hapus semua output<!--?lit$105441083$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$105441083$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$105441083$-->Daftar isi<!--?lit$105441083$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Info notebook<!--?lit$105441083$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Histori kode yang dieksekusi<!--?lit$105441083$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$105441083$-->Komentar
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1e" style="user-select: none;"></div><div command="collapse-sections" class=" goog-menuitem " role="menuitem" id=":1f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Ciutkan bagian<!--?lit$105441083$--></div></div><div command="expand-sections" class=" goog-menuitem " role="menuitem" id=":1g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Luaskan bagian<!--?lit$105441083$--></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Simpan tata letak bagian yang diciutkan<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1i" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Tampilkan/sembunyikan kode<!--?lit$105441083$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Tampilkan/sembunyikan output<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1l" style="user-select: none;"></div><div command="focus-next-tab" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Fokuskan tab berikutnya<!--?lit$105441083$--></div></div><div command="focus-previous-tab" class=" goog-menuitem " role="menuitem" id=":1n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Fokuskan tab sebelumnya<!--?lit$105441083$--></div></div><div command="move-tab-to-next" class=" goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Pindahkan tab ke panel berikutnya<!--?lit$105441083$--></div></div><div command="move-tab-to-prev" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Pindahkan tab ke panel sebelumnya<!--?lit$105441083$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$105441083$--><div command="hide-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Sembunyikan komentar<!--?lit$105441083$--></div></div><div command="show-minimized-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Minimalkan komentar<!--?lit$105441083$--></div></div><div command="show-expanded-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Luaskan komentar<!--?lit$105441083$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$105441083$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Sel kode<!--?lit$105441083$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Sel teks<!--?lit$105441083$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Sel header bagian<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1u" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Sel kode coretan<!--?lit$105441083$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Cuplikan kode<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1x" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Tambahkan kolom formulir<!--?lit$105441083$--></div></div></div><div class="goog-menu colab-styled-scroller" id="runtime-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 565px; visibility: visible; left: 268.604px; top: 62px; display: none;"><!--?lit$105441083$--><div command="runall" class="goog-menuitem" role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Jalankan semua<!--?lit$105441083$--><span class="goog-menuitem-accel">Ctrl+F9</span></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":21" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Jalankan sebelumnya<!--?lit$105441083$--><span class="goog-menuitem-accel">Ctrl+F8</span></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Jalankan sel yang difokuskan<!--?lit$105441083$--><span class="goog-menuitem-accel">Ctrl+Enter</span></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Jalankan pilihan<!--?lit$105441083$--><span class="goog-menuitem-accel">Ctrl+Shift+Enter</span></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Jalankan sel dan yang di bawahnya<!--?lit$105441083$--><span class="goog-menuitem-accel">Ctrl+F10</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":25" style="user-select: none;"></div><div command="interrupt" class="goog-menuitem" role="menuitem" id=":26" aria-disabled="false" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Interupsi eksekusi<!--?lit$105441083$--><span class="goog-menuitem-accel">Ctrl+M I</span></div></div><div command="restart" class="goog-menuitem" role="menuitem" id=":27" aria-disabled="false" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Mulai ulang sesi<!--?lit$105441083$--><span class="goog-menuitem-accel">Ctrl+M .</span></div></div><div command="restart-and-run-all" class="goog-menuitem" role="menuitem" id=":28" aria-disabled="false" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Mulai ulang sesi dan jalankan semua<!--?lit$105441083$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Putuskan koneksi dan hapus runtime<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2a" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Ubah jenis runtime<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Kelola sesi<!--?lit$105441083$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Lihat resource<!--?lit$105441083$--></div></div><div command="view-runtime-logs" class="goog-menuitem" role="menuitem" id=":2f" aria-disabled="false" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Lihat log waktu proses<!--?lit$105441083$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$105441083$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Palet perintah<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2i" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Setelan<!--?lit$105441083$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Pintasan keyboard<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2l" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Perbedaan notebook<!--?lit$105441083$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$105441083$-->(dibuka di tab baru)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$105441083$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Pertanyaan umum (FAQ)<!--?lit$105441083$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Lihat catatan rilis<!--?lit$105441083$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Telusuri cuplikan kode<!--?lit$105441083$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2r" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Laporkan bug<!--?lit$105441083$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":2t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Laporkan penyalahgunaan Drive<!--?lit$105441083$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Kirim masukan<!--?lit$105441083$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Lihat persyaratan layanan<!--?lit$105441083$--></div></div><div command="view-in-english" class=" goog-menuitem " role="menuitem" id=":2w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$105441083$-->Lihat dalam bahasa Inggris<!--?lit$105441083$--></div></div></div><dialog class="doc-comments-area" aria-label="Komentar"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$105441083$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$105441083$--><button id="button" class="button">
      <!--?lit$105441083$-->
      <span class="touch"></span>
      <!--?lit$105441083$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$105441083$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$105441083$-->Tambahkan komentar
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy40f07c85454be4011a6cad5aec86c1b736d5a5110.3351400813" name="apiproxy40f07c85454be4011a6cad5aec86c1b736d5a5110.3351400813" src="./class_Restoran.ipynb - Colab_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-x4c9fq56wuun" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./class_Restoran.ipynb - Colab_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;" data-has-listeners="true"></textarea></div><iframe style="display: none;" src="./class_Restoran.ipynb - Colab_files/saved_resource.html"></iframe></div><iframe id="apiproxyb4ca6ba0ad853deb9ac9cda83eee963bb2f374840.3507115922" name="apiproxyb4ca6ba0ad853deb9ac9cda83eee963bb2f374840.3507115922" src="./class_Restoran.ipynb - Colab_files/proxy(1).html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><span id="PING_IFRAME_FORM_DETECTION" style="display: none;"></span><iframe src="./class_Restoran.ipynb - Colab_files/bscframe.html" style="display: none;"></iframe><span id="PING_CONTENT_DLS_POPUP" style="display: none;"></span><div style="background-color: transparent; border: none; bottom: 15px; display: block; margin: 0px; opacity: 1; padding: 0px; position: fixed; right: 15px; z-index: 2147483647;"><template shadowrootmode="closed"><style>/*!
 * 
 *     MCAFEE RESTRICTED CONFIDENTIAL
 *     Copyright (c) 2025 McAfee, LLC
 *
 *     The source code contained or described herein and all documents related
 *     to the source code ("Material") are owned by McAfee or its
 *     suppliers or licensors. Title to the Material remains with McAfee
 *     or its suppliers and licensors. The Material contains trade
 *     secrets and proprietary and confidential information of McAfee or its
 *     suppliers and licensors. The Material is protected by worldwide copyright
 *     and trade secret laws and treaty provisions. No part of the Material may
 *     be used, copied, reproduced, modified, published, uploaded, posted,
 *     transmitted, distributed, or disclosed in any way without McAfee's prior
 *     express written permission.
 *
 *     No license under any patent, copyright, trade secret or other intellectual
 *     property right is granted to or conferred upon you by disclosure or
 *     delivery of the Materials, either expressly, by implication, inducement,
 *     estoppel or otherwise. Any license under such intellectual property rights
 *     must be expressed and approved by McAfee in writing.
 *
 */
@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-Thin.ttf") format("truetype");font-weight:100;font-style:normal}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-ThinItalic.ttf") format("truetype");font-weight:100;font-style:italic}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-ExtraLight.ttf") format("truetype");font-weight:200;font-style:normal}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-ExtraLightItalic.ttf") format("truetype");font-weight:200;font-style:italic}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-Light.ttf") format("truetype");font-weight:300;font-style:normal}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-LightItalic.ttf") format("truetype");font-weight:300;font-style:italic}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-Regular.ttf") format("truetype");font-weight:400;font-style:normal}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-Italic.ttf") format("truetype");font-weight:400;font-style:italic}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-Medium.ttf") format("truetype");font-weight:500;font-style:normal}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-MediumItalic.ttf") format("truetype");font-weight:500;font-style:italic}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-SemiBold.ttf") format("truetype");font-weight:600;font-style:normal}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-SemiBoldItalic.ttf") format("truetype");font-weight:600;font-style:italic}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-Bold.ttf") format("truetype");font-weight:700;font-style:normal}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-BoldItalic.ttf") format("truetype");font-weight:700;font-style:italic}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-ExtraBold.ttf") format("truetype");font-weight:800;font-style:normal}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-ExtraBoldItalic.ttf") format("truetype");font-weight:800;font-style:italic}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-Black.ttf") format("truetype");font-weight:900;font-style:normal}@font-face{font-family:"McAfeePoppins";src:url("../../../fonts/Poppins-BlackItalic.ttf") format("truetype");font-weight:900;font-style:italic}*{border:0;box-sizing:border-box;font:inherit;font-family:"McAfeePoppins",Helvetica,Arial;font-size:100%;margin:0;padding:0;vertical-align:baseline;outline:none}article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section{display:block}html,body{background-color:#f5f6fa;font-family:"McAfeePoppins",Helvetica,Arial;line-height:1;height:100%;width:100%}ol,ul{list-style:none}blockquote,q{quotes:none}blockquote:after,blockquote:before,q:after,q:before{content:"";content:none}table{border-collapse:collapse;border-spacing:0}b{font-weight:bold}img{display:block}.dls__container{align-items:center;display:flex;margin:0 auto;margin-top:50px;position:relative}.dls__popup__expanded{align-items:center;overflow:hidden;border-radius:100px;cursor:pointer;display:flex;left:0;padding:15px;position:absolute;height:95px;width:383px;background-color:#fff;transition:all .3s ease-in-out}.dls__popup__expanded .dls__icon{height:65px;width:73px}.content{margin-left:12px}.content .content__images{display:flex;align-items:center;width:250px}.content .content__images .seperator__line{margin-left:5px;margin-right:10px}.content .content__images #dls_close_icon{cursor:pointer;margin-left:auto;margin-right:0px}.content p{font-family:"McAfeePoppins",Helvetica,Arial;font-weight:"400";font-size:14px;line-height:20px;margin-top:8px;color:#4258ff;width:250px;cursor:pointer}.shield{overflow:hidden;box-shadow:0px 2px 4px 0px rgba(33,41,52,.12),0px -1px 2px 0px rgba(0,0,0,.08);align-items:center;border-radius:100px;bottom:0;display:flex;height:95px;justify-content:center;position:absolute;right:0;width:383px;transition:all .3s ease-in-out}.shield__circle{display:flex;justify-content:center;align-items:center;width:55px;height:55px;background-color:#c01818;transition:all .6s ease-in-out .2s;z-index:1;opacity:0}

/*# sourceMappingURL=../sourceMap/chrome/css/download_scan_popup.css.map*/</style><div class="dls__container">
  <div class="shield" style="background: transparent; opacity: 0.1; display: none;">
    <div class="shield__circle" style="opacity: 0;">
      <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/mcafee_logo_white.svg?secret=gpvksa" x-mcsrc="" id="dls_ballon_icon" x-mcsrcparsed="true">
    </div>
    <div class="dls__popup__expanded" style="opacity: 1;">
      <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/download_scan_icon.svg?secret=gpvksa" x-mcsrc="" class="dls__icon" x-mcsrcparsed="true">
      <div class="content">
        <div class="content__images">
          <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/mcafee_logo_red.svg?secret=gpvksa" x-mcsrc="" id="dls_mcafee_logo" x-mcsrcparsed="true">
          <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/seperator_line.svg?secret=gpvksa" x-mcsrc="" class="seperator__line" x-mcsrcparsed="true">
          <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/webadvisor.svg?secret=gpvksa" x-mcsrc="" x-mcsrcparsed="true">
          <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/close-outline.svg?secret=gpvksa" x-mcsrc="" id="dls_close_icon" x-mcsrcparsed="true">
        </div>
        <p id="download_scan_popup_expanded_descriptions">Your download's being scanned. We'll let you know if there's an issue.</p>
      </div>
    </div>
  </div>
</div><style>/*!
 * 
 *     MCAFEE RESTRICTED CONFIDENTIAL
 *     Copyright (c) 2025 McAfee, LLC
 *
 *     The source code contained or described herein and all documents related
 *     to the source code ("Material") are owned by McAfee or its
 *     suppliers or licensors. Title to the Material remains with McAfee
 *     or its suppliers and licensors. The Material contains trade
 *     secrets and proprietary and confidential information of McAfee or its
 *     suppliers and licensors. The Material is protected by worldwide copyright
 *     and trade secret laws and treaty provisions. No part of the Material may
 *     be used, copied, reproduced, modified, published, uploaded, posted,
 *     transmitted, distributed, or disclosed in any way without McAfee's prior
 *     express written permission.
 *
 *     No license under any patent, copyright, trade secret or other intellectual
 *     property right is granted to or conferred upon you by disclosure or
 *     delivery of the Materials, either expressly, by implication, inducement,
 *     estoppel or otherwise. Any license under such intellectual property rights
 *     must be expressed and approved by McAfee in writing.
 *
 */
.mc-interactive-balloon{position:absolute;right:-50px;bottom:8px;box-shadow:rgba(0,0,0,.12) 0px 0px 10px;height:40px;width:40px;background:#1671ee;border-radius:20px;display:flex;justify-content:center;align-items:center}

/*# sourceMappingURL=../sourceMap/chrome/css/interactive_balloon.css.map*/</style></template></div></body><div id="aifnmjmchg" class="aifnmjmchg dark" data-v-app=""><!----><!----><div id="aifnmjmchg-container" class="close-sidebar"><div id="aifnmjmchg-sidebar"><div id="ai-aifnmjmchgsidebar" class="aifnmjmchg-flex aifnmjmchg-w-full aifnmjmchg-h-full aifnmjmchg-overflow-hidden"><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-w-[calc(100%_-_60px)]" id="aifnmjmchg-sidebar-chat"><div class="aifnmjmchg-header aifnmjmchg-flex-shrink"><nav class="aifnmjmchg-w-full aifnmjmchg-bg-[transparent]"><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-w-full aifnmjmchg-p-0"><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-between aifnmjmchg-w-full"><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-between"><span name="logo" class="aifnmjmchg-w-8 aifnmjmchg-h-8 "><svg class=" aifnmjmchg-w-8 aifnmjmchg-h-8  aifnmjmchg-logo-dark aifnmjmchg-logo aifnmjmchg-p-0.5 " xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830.12 868.33">    <path fill="currentColor" d="M424.14,825.57c-114.47,0-207.59-93.13-207.59-207.59V261.32c0-114.46,93.12-207.59,207.59-207.59s207.59,93.13,207.59,207.59V618C631.73,732.44,538.6,825.57,424.14,825.57Zm0-713.31c-82.19,0-149.06,66.87-149.06,149.06V618C275.08,700.17,342,767,424.14,767S573.2,700.17,573.2,618V261.32C573.2,179.13,506.33,112.26,424.14,112.26Z"></path>    <path fill="currentColor" d="M578.23,736.49a206.33,206.33,0,0,1-103.45-27.9L165.91,530.27a207.59,207.59,0,0,1-76-283.58c57.24-99.13,184.45-133.21,283.58-76L682.37,349c99.13,57.23,133.22,184.45,76,283.58A206.21,206.21,0,0,1,632.3,729.33,208.85,208.85,0,0,1,578.23,736.49ZM270,201.45A149.18,149.18,0,0,0,140.61,276C99.52,347.13,124,438.48,195.17,479.58L504,657.9c71.18,41.1,162.53,16.63,203.62-54.56h0A149.06,149.06,0,0,0,653.1,399.72L344.23,221.39A148.22,148.22,0,0,0,270,201.45Z"></path>    <path fill="currentColor" d="M270,736.49A208.9,208.9,0,0,1,216,729.33,207.59,207.59,0,0,1,165.91,349L474.78,170.7c99.12-57.23,226.34-23.14,283.57,76h0c57.24,99.13,23.15,226.34-76,283.58L373.5,708.59A206.37,206.37,0,0,1,270,736.49Zm308.28-535A148.15,148.15,0,0,0,504,221.39L195.17,399.72A149.06,149.06,0,0,0,344.23,657.9L653.1,479.58c71.18-41.1,95.66-132.44,54.56-203.62L733,261.32,707.66,276A149.15,149.15,0,0,0,578.32,201.45Z"></path></svg></span><div class="aifnmjmchg-self-center aifnmjmchg-text-base aifnmjmchg-text-black aifnmjmchg-ml-2 dark:aifnmjmchg-text-gray-200 aifnmjmchg-whitespace-nowrap">Obrolan</div></div><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-max-h-[50px]"><button class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-space-x-2 aifnmjmchg-bg-transparent hover:aifnmjmchg-bg-[var(--aifnmjmchg-link-color)] aifnmjmchg-transition-all aifnmjmchg-rounded-full aifnmjmchg-p-1 aifnmjmchg-px-2"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hide="true" class="aifnmjmchg-w-4 aifnmjmchg-h-4 dark:aifnmjmchg-text-gray-200"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15"></path></svg><span class="aifnmjmchg-text-sm dark:aifnmjmchg-text-gray-200">_Percakapan Baru</span></button><button type="button" class="aifnmjmchg-ml-2 svg-logo"><span><svg class="aifnmjmchg-h-6 aifnmjmchg-w-6 aifnmjmchg-history_icon" width="1em" height="1em" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M20 12C20 16.4183 16.4183 20 12 20C7.58172 20 4 16.4183 4 12C4 7.58172 7.58172 4 12 4C16.4183 4 20 7.58172 20 12ZM22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12ZM13 8.99939C12.9997 8.4471 12.5517 7.99966 11.9994 8C11.4471 8.00034 10.9997 8.44833 11 9.00061L11.0024 13.0006C11.0026 13.3347 11.1697 13.6466 11.4477 13.832L14.4471 15.832C14.9066 16.1384 15.5275 16.0143 15.8339 15.5548C16.1403 15.0953 16.0161 14.4744 15.5566 14.168L13.0021 12.4647L13 8.99939Z" fill="currentColor"></path></svg></span></button></div></div></div></nav></div><div id="aifnmjmchg-upgrade-plan-modal" class="aifnmjmchg-hide"><div tabindex="-1" aria-hide="true" class="aifnmjmchg-fixed !aifnmjmchg-z-[999999] aifnmjmchg-modal aifnmjmchg-m-0 aifnmjmchg-bg-[rgba(0,0,0,.5)] aifnmjmchg-top-0 aifnmjmchg-left-0 aifnmjmchg-bottom-0 aifnmjmchg-right-0 aifnmjmchg-w-full aifnmjmchg-p-4 aifnmjmchg-overflow-x-hidden aifnmjmchg-overflow-y-auto lg:aifnmjmchg-inset-0 h-[calc(100%)] aifnmjmchg-max-h-full aifnmjmchg-justify-center aifnmjmchg-flex aifnmjmchg-w-full aifnmjmchg-items-center" data-modal-hide=""><div class="aifnmjmchg-relative aifnmjmchg-w-full lg:aifnmjmchg-max-w-screen-xl aifnmjmchg-max-h-full"><div class="aifnmjmchg-relative aifnmjmchg-bg-white aifnmjmchg-rounded-lg aifnmjmchg-shadow dark:aifnmjmchg-bg-neutral-800"><div class="aifnmjmchg-px-6 aifnmjmchg-py-4 aifnmjmchg-border-b aifnmjmchg-rounded-t dark:aifnmjmchg-border-neutral-600"><h3 class="aifnmjmchg-text-base aifnmjmchg-font-semibold aifnmjmchg-text-neutral-900 lg:aifnmjmchg-text-lg dark:aifnmjmchg-text-white aifnmjmchg-text-center">Search</h3><button type="button" class="aifnmjmchg-absolute aifnmjmchg-top-3 aifnmjmchg-right-2.5 aifnmjmchg-text-neutral-400 aifnmjmchg-bg-transparent hover:aifnmjmchg-bg-neutral-200 hover:aifnmjmchg-text-neutral-900 aifnmjmchg-rounded-lg aifnmjmchg-text-sm aifnmjmchg-w-8 aifnmjmchg-h-8 aifnmjmchg-ml-auto aifnmjmchg-inline-flex aifnmjmchg-justify-center aifnmjmchg-items-center dark:hover:aifnmjmchg-bg-neutral-600 dark:hover:aifnmjmchg-text-white" data-modal-hide=""><svg class="aifnmjmchg-w-3 aifnmjmchg-h-3" aria-hide="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"></path></svg><span class="aifnmjmchg-sr-only">Close modal</span></button></div><div class="aifnmjmchg-px-4 aifnmjmchg-py-12 aifnmjmchg-w-full aifnmjmchg-text-center aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center aifnmjmchg-gap-8"><p class="aifnmjmchg-px-4 aifnmjmchg-text-sm aifnmjmchg-text-neutral-600 dark:aifnmjmchg-text-neutral-400">Data dari ChatGPT bukanlah data real-time. Fitur WebAccess menggabungkan kecerdasan ChatGPT dengan informasi web real-time, memungkinkan GPT untuk menangani pertanyaan yang terkait dengan informasi real-time secara lebih efektif. Tingkatkan untuk mendapatkan fitur ini, dan tidak perlu lagi khawatir tentang informasi yang usang!</p><button class="aifnmjmchg-pricing aifnmjmchg-cursor-pointer aifnmjmchg-w-full aifnmjmchg-font-semibold aifnmjmchg-text-white aifnmjmchg-text-sm aifnmjmchg-py-2 aifnmjmchg-rounded-md aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-gap-2 aifnmjmchg-justify-center aifnmjmchg-bg-[var(--aifnmjmchg-link-color)] hover:aifnmjmchg-opacity-90 aifnmjmchg-transition-all">Tingkatkan Sekarang</button></div><!----></div></div></div></div><button data-aifnmjmchg-dropdown-toggle="aifnmjmchg-upgrade-plan-modal" id="aifnmjmchg-toggle-upgrade-button" class="aifnmjmchg-hidden"></button><div id="ai-aifnmjmchgsidebar-content" class="false"><div class="aifnmjmchg-h-screen aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-h-full"><div id="ai-aifnmjmchgmessage-container" class="aifnmjmchg-flex aifnmjmchg-relative aifnmjmchg-flex-grow aifnmjmchg-w-full aifnmjmchg-overflow-x-hidden"><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-h-full aifnmjmchg-space-y-3"><div id="aifnmjmchg-example"><div class="aifnmjmchg-p-2"><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-between aifnmjmchg-p-3 aifnmjmchg-space-x-3 aifnmjmchg-border aifnmjmchg-rounded-xl aifnmjmchg-bg-neutral-100 dark:aifnmjmchg-bg-neutral-900 dark:aifnmjmchg-text-neutral-200 aifnmjmchg-cursor-pointer"><div><p class="aifnmjmchg-font-bold">🤓 Jelaskan sesuatu yang rumit</p><p class="aifnmjmchg-opacity-60 aifnmjmchg-text-[11px] example_content">Jelaskan Kecerdasan Buatan sehingga saya dapat menjelaskannya kepada anak saya yang berusia enam tahun.</p></div><button><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="aifnmjmchg-w-5 aifnmjmchg-h-5 aifnmjmchg-cursor-pointer" fill="none"><path d="M20 12L14 6M20 12L14 18M20 12L9.5 12M4 12L6.5 12" stroke="#14746F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></div></div><div class="aifnmjmchg-p-2"><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-between aifnmjmchg-p-3 aifnmjmchg-space-x-3 aifnmjmchg-border aifnmjmchg-rounded-xl aifnmjmchg-bg-neutral-100 dark:aifnmjmchg-bg-neutral-900 dark:aifnmjmchg-text-neutral-200 aifnmjmchg-cursor-pointer"><div><p class="aifnmjmchg-font-bold">🧠 Dapatkan saran dan buat ide baru</p><p class="aifnmjmchg-opacity-60 aifnmjmchg-text-[11px] example_content">Harap berikan saya 10 ide perjalanan terbaik di seluruh dunia</p></div><button><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="aifnmjmchg-w-5 aifnmjmchg-h-5 aifnmjmchg-cursor-pointer" fill="none"><path d="M20 12L14 6M20 12L14 18M20 12L9.5 12M4 12L6.5 12" stroke="#14746F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></div></div><div class="aifnmjmchg-p-2"><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-between aifnmjmchg-p-3 aifnmjmchg-space-x-3 aifnmjmchg-border aifnmjmchg-rounded-xl aifnmjmchg-bg-neutral-100 dark:aifnmjmchg-bg-neutral-900 dark:aifnmjmchg-text-neutral-200 aifnmjmchg-cursor-pointer"><div><p class="aifnmjmchg-font-bold">💭 Terjemahkan, ringkas, perbaiki tata bahasa dan lainnya...</p><p class="aifnmjmchg-opacity-60 aifnmjmchg-text-[11px] example_content">Menerjemahkan "I love you", ke bahasa Perancis</p></div><button><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="aifnmjmchg-w-5 aifnmjmchg-h-5 aifnmjmchg-cursor-pointer" fill="none"><path d="M20 12L14 6M20 12L14 18M20 12L9.5 12M4 12L6.5 12" stroke="#14746F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></div></div></div><!----><div data-v-99f45794="" class="aifnmjmchg-h-full" id="aifnmjmchg-message"><div data-v-99f45794="" aria-details="chat-key-0" class="aifnmjmchg-bg-neutral-100 dark:aifnmjmchg-bg-neutral-900 dark:aifnmjmchg-text-gray-200 aifnmjmchg-mt-[2px] aifnmjmchg-mb-[2px]"><div data-v-99f45794="" class="aifnmjmchg-flex aifnmjmchg-p-2 aifnmjmchg-text-[10px] dark:aifnmjmchg-text-gray-200 aifnmjmchg-flex-col aifnmjmchg-items-start aifnmjmchg-justify-start aifnmjmchg-gap-2"><div data-v-99f45794="" class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-space-x-2"><span data-v-99f45794=""><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-GPT-4o Mini" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"> <rect width="16" height="16" rx="8" fill="#0BD6FF"></rect> <path d="M13.1348 6.91143C13.4071 6.0943 13.3133 5.19918 12.878 4.45593C12.2232 3.31593 10.907 2.72943 9.62146 3.00543C9.04958 2.36118 8.22796 1.99481 7.36658 2.00006C6.05258 1.99706 4.88671 2.84306 4.48246 4.09331C3.63833 4.26618 2.90971 4.79456 2.48333 5.54343C1.82371 6.68043 1.97408 8.11368 2.85533 9.08868C2.58308 9.9058 2.67683 10.8009 3.11221 11.5442C3.76696 12.6842 5.08321 13.2707 6.36871 12.9947C6.94021 13.6389 7.76221 14.0053 8.62358 13.9997C9.93833 14.0031 11.1046 13.1563 11.5088 11.9049C12.353 11.7321 13.0816 11.2037 13.508 10.4548C14.1668 9.3178 14.0157 7.88643 13.1348 6.91143ZM8.62433 13.2156C8.09821 13.2163 7.58858 13.0322 7.18471 12.6951C7.20308 12.6853 7.23496 12.6677 7.25558 12.6549L9.64508 11.2749C9.76733 11.2056 9.84233 11.0754 9.84158 10.9348V7.56618L10.8515 8.1493C10.8623 8.15455 10.8695 8.16505 10.871 8.17705V10.9667C10.8695 12.2072 9.86483 13.2129 8.62433 13.2156ZM3.79283 11.1519C3.52921 10.6967 3.43433 10.1631 3.52471 9.64518C3.54233 9.65568 3.57346 9.6748 3.59558 9.68755L5.98508 11.0676C6.10621 11.1384 6.25621 11.1384 6.37771 11.0676L9.29483 9.38305V10.5493C9.29558 10.5613 9.28996 10.5729 9.28058 10.5804L6.86521 11.9751C5.78933 12.5946 4.41496 12.2263 3.79283 11.1519ZM3.16396 5.93605C3.42646 5.48006 3.84083 5.1313 4.33433 4.95018C4.33433 4.97081 4.33321 5.00718 4.33321 5.03268V7.79305C4.33246 7.9333 4.40746 8.06343 4.52933 8.1328L7.44646 9.81693L6.43658 10.4001C6.42646 10.4068 6.41371 10.4079 6.40246 10.4031L3.98671 9.0073C2.91308 8.38555 2.54521 7.01155 3.16396 5.93605ZM11.4612 7.86693L8.54408 6.18243L9.55396 5.59968C9.56408 5.59293 9.57683 5.59181 9.58808 5.59668L12.0038 6.9913C13.0793 7.61268 13.448 8.98855 12.8266 10.0641C12.5637 10.5193 12.1497 10.8681 11.6566 11.0496V8.20668C11.6577 8.06643 11.5827 7.93668 11.4612 7.86693ZM12.4662 6.35418C12.4486 6.34331 12.4175 6.32455 12.3953 6.3118L10.0058 4.93181C9.88471 4.86093 9.73471 4.86093 9.61321 4.93181L6.69608 6.6163V5.45005C6.69533 5.43805 6.70096 5.42643 6.71033 5.41893L9.12571 4.02543C10.2016 3.40481 11.5771 3.77418 12.1973 4.85043C12.4595 5.30493 12.5551 5.83706 12.4662 6.35418ZM6.14708 8.4328L5.13683 7.84968C5.12596 7.84443 5.11883 7.83393 5.11733 7.82193V5.03231C5.11808 3.79031 6.12571 2.78381 7.36771 2.78456C7.89308 2.78456 8.40158 2.96906 8.80546 3.30506C8.78708 3.31481 8.75558 3.33243 8.73458 3.34518L6.34508 4.72518C6.22283 4.79456 6.14783 4.92431 6.14858 5.06493L6.14708 8.4328ZM6.69571 7.25005L7.99508 6.49968L9.29446 7.24968V8.75005L7.99508 9.50005L6.69571 8.75005V7.25005Z" fill="white"></path> </svg></span><span data-v-99f45794="">GPT-4o Mini</span></div><!----></div><div data-v-99f45794="" class="dark:aifnmjmchg-bg-neutral-900 aifnmjmchg-px-6 aifnmjmchg-py-4 ai_result_container"><div data-v-99f45794="" class="aifnmjmchg-flex aifnmjmchg-flex-row aifnmjmchg-items-center"><div data-v-99f45794="" class="ai_result">Halo, bagaimana saya bisa membantu Anda hari ini?<br></div><!----></div><!----><div data-v-99f45794="" class="aifnmjmchg-mt-3 aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-float-right aifnmjmchg-cursor-pointer aifnmjmchg-gap-2 aifnmjmchg-divide-x-[0.5px] aifnmjmchg-divide-neutral-300 dark:aifnmjmchg-divide-neutral-700 aifnmjmchg-opacity-0"><div class="aifnmjmchg-bg-neutral-200 dark:aifnmjmchg-bg-neutral-950 aifnmjmchg-w-3 aifnmjmchg-h-3 aifnmjmchg-p-1 aifnmjmchg-rounded-md aifnmjmchg-justify-center aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-float-right aifnmjmchg-cursor-pointer"><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><svg class="svg-inline--fa fa-clipboard aifnmjmchg-w-3 aifnmjmchg-h-3" aria-hidden="true" focusable="false" data-prefix="far" data-icon="clipboard" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path class="" fill="currentColor" d="M280 64l40 0c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 512c-35.3 0-64-28.7-64-64L0 128C0 92.7 28.7 64 64 64l40 0 9.6 0C121 27.5 153.3 0 192 0s71 27.5 78.4 64l9.6 0zM64 112c-8.8 0-16 7.2-16 16l0 320c0 8.8 7.2 16 16 16l256 0c8.8 0 16-7.2 16-16l0-320c0-8.8-7.2-16-16-16l-16 0 0 24c0 13.3-10.7 24-24 24l-88 0-88 0c-13.3 0-24-10.7-24-24l0-24-16 0zm128-8a24 24 0 1 0 0-48 24 24 0 1 0 0 48z"></path></svg><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999] aifnmjmchg-top-0 aifnmjmchg-left-1/2 aifnmjmchg-transform aifnmjmchg--translate-x-1/2 aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-900 dark:aifnmjmchg-text-gray-200 aifnmjmchg-translate-y-[-120%] ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[200px] aifnmjmchg-w-full">Salin</div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li></div><!----><!----></div><div data-v-99f45794="" class="aifnmjmchg-clear-both"></div></div><!----><!----></div><div data-v-99f45794="" id="aifnmjmchg-stop-chat-ai_chat" class="aifnmjmchg-stop-chat aifnmjmchg-hide"><button data-v-99f45794="" class="aifnmjmchg-text-white hover:aifnmjmchg-opacity-90 aifnmjmchg-font-medium aifnmjmchg-text-md aifnmjmchg-px-5 aifnmjmchg-py-2 aifnmjmchg-rounded-md dark:hover:aifnmjmchg-bg-[var(--aifnmjmchg-tab-menu-active-bg-color)]"><div data-v-99f45794="" class="aifnmjmchg-flex aifnmjmchg-w-full aifnmjmchg-gap-2 aifnmjmchg-items-center aifnmjmchg-justify-center"><svg data-v-99f45794="" stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-xs" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><rect data-v-99f45794="" x="3" y="3" width="18" height="18" rx="2" ry="2"></rect></svg> Berhenti menghasilkan</div></button></div></div></div></div></div><div class="aifnmjmchg-px-3 aifnmjmchg-pt-3"><div class="aifnmjmchg-flex aifnmjmchg-relative aifnmjmchg-w-full aifnmjmchg-items-center aifnmjmchg-justify-start aifnmjmchg-my-3 aifnmjmchg-grid aifnmjmchg-grid-cols-5 lg:aifnmjmchg-grid-none lg:grid-cols-2"><div class="aifnmjmchg-flex aifnmjmchg-w-full aifnmjmchg-gap-3 aifnmjmchg-items-center aifnmjmchg-col-span-5 lg:aifnmjmchg-col-span-none"><div class="aifnmjmchg-flex aifnmjmchg-flex-wrap aifnmjmchg-gap-[6px] aifnmjmchg-max-w-full aifnmjmchg-place-self-end aifnmjmchg-self-center aifnmjmchg-min-w-[55px]"><div class="aifnmjmchg-text-xs aifnmjmchg-relative aifnmjmchg-min-w-[55px]" data-aifnmjmchg-dropdown-toggle="aifnmjmchg-model-dropdown" data-placement="top-start"><div class="aifnmjmchg-flex aifnmjmchg-justify-center aifnmjmchg-min-h-full aifnmjmchg-max-h-full aifnmjmchg-items-center aifnmjmchg-leading-4 aifnmjmchg-gap-[2px] lg:aifnmjmchg-flex aifnmjmchg-space-x-1 aifnmjmchg-text-sm aifnmjmchg-relative dark:aifnmjmchg-text-neutral-200 aifnmjmchg-border aifnmjmchg-rounded-xl aifnmjmchg-cursor-pointer aifnmjmchg-pl-[6px] aifnmjmchg-pr-[5px] aifnmjmchg-py-[7px]"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-justify-center aifnmjmchg-items-center aifnmjmchg-rounded-full aifnmjmchg-h-4 aifnmjmchg-w-4 aifnmjmchg-ml-[1px] aifnmjmchg-mr-[2px]"><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-center aifnmjmchg-rounded-full"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-GPT-4o Mini" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"> <rect width="16" height="16" rx="8" fill="#0BD6FF"></rect> <path d="M13.1348 6.91143C13.4071 6.0943 13.3133 5.19918 12.878 4.45593C12.2232 3.31593 10.907 2.72943 9.62146 3.00543C9.04958 2.36118 8.22796 1.99481 7.36658 2.00006C6.05258 1.99706 4.88671 2.84306 4.48246 4.09331C3.63833 4.26618 2.90971 4.79456 2.48333 5.54343C1.82371 6.68043 1.97408 8.11368 2.85533 9.08868C2.58308 9.9058 2.67683 10.8009 3.11221 11.5442C3.76696 12.6842 5.08321 13.2707 6.36871 12.9947C6.94021 13.6389 7.76221 14.0053 8.62358 13.9997C9.93833 14.0031 11.1046 13.1563 11.5088 11.9049C12.353 11.7321 13.0816 11.2037 13.508 10.4548C14.1668 9.3178 14.0157 7.88643 13.1348 6.91143ZM8.62433 13.2156C8.09821 13.2163 7.58858 13.0322 7.18471 12.6951C7.20308 12.6853 7.23496 12.6677 7.25558 12.6549L9.64508 11.2749C9.76733 11.2056 9.84233 11.0754 9.84158 10.9348V7.56618L10.8515 8.1493C10.8623 8.15455 10.8695 8.16505 10.871 8.17705V10.9667C10.8695 12.2072 9.86483 13.2129 8.62433 13.2156ZM3.79283 11.1519C3.52921 10.6967 3.43433 10.1631 3.52471 9.64518C3.54233 9.65568 3.57346 9.6748 3.59558 9.68755L5.98508 11.0676C6.10621 11.1384 6.25621 11.1384 6.37771 11.0676L9.29483 9.38305V10.5493C9.29558 10.5613 9.28996 10.5729 9.28058 10.5804L6.86521 11.9751C5.78933 12.5946 4.41496 12.2263 3.79283 11.1519ZM3.16396 5.93605C3.42646 5.48006 3.84083 5.1313 4.33433 4.95018C4.33433 4.97081 4.33321 5.00718 4.33321 5.03268V7.79305C4.33246 7.9333 4.40746 8.06343 4.52933 8.1328L7.44646 9.81693L6.43658 10.4001C6.42646 10.4068 6.41371 10.4079 6.40246 10.4031L3.98671 9.0073C2.91308 8.38555 2.54521 7.01155 3.16396 5.93605ZM11.4612 7.86693L8.54408 6.18243L9.55396 5.59968C9.56408 5.59293 9.57683 5.59181 9.58808 5.59668L12.0038 6.9913C13.0793 7.61268 13.448 8.98855 12.8266 10.0641C12.5637 10.5193 12.1497 10.8681 11.6566 11.0496V8.20668C11.6577 8.06643 11.5827 7.93668 11.4612 7.86693ZM12.4662 6.35418C12.4486 6.34331 12.4175 6.32455 12.3953 6.3118L10.0058 4.93181C9.88471 4.86093 9.73471 4.86093 9.61321 4.93181L6.69608 6.6163V5.45005C6.69533 5.43805 6.70096 5.42643 6.71033 5.41893L9.12571 4.02543C10.2016 3.40481 11.5771 3.77418 12.1973 4.85043C12.4595 5.30493 12.5551 5.83706 12.4662 6.35418ZM6.14708 8.4328L5.13683 7.84968C5.12596 7.84443 5.11883 7.83393 5.11733 7.82193V5.03231C5.11808 3.79031 6.12571 2.78381 7.36771 2.78456C7.89308 2.78456 8.40158 2.96906 8.80546 3.30506C8.78708 3.31481 8.75558 3.33243 8.73458 3.34518L6.34508 4.72518C6.22283 4.79456 6.14783 4.92431 6.14858 5.06493L6.14708 8.4328ZM6.69571 7.25005L7.99508 6.49968L9.29446 7.24968V8.75005L7.99508 9.50005L6.69571 8.75005V7.25005Z" fill="white"></path> </svg></span></div></div><span class="aifnmjmchg-inline-block aifnmjmchg-text-[13px] aifnmjmchg-text-ellipsis aifnmjmchg-whitespace-nowrap aifnmjmchg-overflow-hidden aifnmjmchg-max-w-full">GPT-4o Mini</span><div class="aifnmjmchg-flex aifnmjmchg-items-end pl-[2px] pr-[2px]"><svg aria-hide="true" fill="currentColor" focusable="false" height="12" role="img" viewBox="0 0 12 12" width="12" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div></div><ul class="aifnmjmchg-model-dropdown aifnmjmchg-z-20 aifnmjmchg-width-full aifnmjmchg-hide aifnmjmchg-w-max aifnmjmchg-min-w-[180px] aifnmjmchg-max-w-[250px] aifnmjmchg-bg-white aifnmjmchg-divide-y aifnmjmchg-divide-neutral-100 aifnmjmchg-rounded-lg aifnmjmchg-shadow dark:aifnmjmchg-bg-neutral-900 dark:aifnmjmchg-divide-neutral-700"><div class="aifnmjmchg-divide-y aifnmjmchg-divide-neutral-100 dark:aifnmjmchg-divide-neutral-700"><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><div class="aifnmjmchg-flex aifnmjmchg-px-4 aifnmjmchg-py-2.5 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700 hover:aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer" style="background: rgba(1, 167, 125, 0.3);"><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-gap-2 aifnmjmchg-text-[12px]"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-GPT-4o Mini" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"> <rect width="16" height="16" rx="8" fill="#0BD6FF"></rect> <path d="M13.1348 6.91143C13.4071 6.0943 13.3133 5.19918 12.878 4.45593C12.2232 3.31593 10.907 2.72943 9.62146 3.00543C9.04958 2.36118 8.22796 1.99481 7.36658 2.00006C6.05258 1.99706 4.88671 2.84306 4.48246 4.09331C3.63833 4.26618 2.90971 4.79456 2.48333 5.54343C1.82371 6.68043 1.97408 8.11368 2.85533 9.08868C2.58308 9.9058 2.67683 10.8009 3.11221 11.5442C3.76696 12.6842 5.08321 13.2707 6.36871 12.9947C6.94021 13.6389 7.76221 14.0053 8.62358 13.9997C9.93833 14.0031 11.1046 13.1563 11.5088 11.9049C12.353 11.7321 13.0816 11.2037 13.508 10.4548C14.1668 9.3178 14.0157 7.88643 13.1348 6.91143ZM8.62433 13.2156C8.09821 13.2163 7.58858 13.0322 7.18471 12.6951C7.20308 12.6853 7.23496 12.6677 7.25558 12.6549L9.64508 11.2749C9.76733 11.2056 9.84233 11.0754 9.84158 10.9348V7.56618L10.8515 8.1493C10.8623 8.15455 10.8695 8.16505 10.871 8.17705V10.9667C10.8695 12.2072 9.86483 13.2129 8.62433 13.2156ZM3.79283 11.1519C3.52921 10.6967 3.43433 10.1631 3.52471 9.64518C3.54233 9.65568 3.57346 9.6748 3.59558 9.68755L5.98508 11.0676C6.10621 11.1384 6.25621 11.1384 6.37771 11.0676L9.29483 9.38305V10.5493C9.29558 10.5613 9.28996 10.5729 9.28058 10.5804L6.86521 11.9751C5.78933 12.5946 4.41496 12.2263 3.79283 11.1519ZM3.16396 5.93605C3.42646 5.48006 3.84083 5.1313 4.33433 4.95018C4.33433 4.97081 4.33321 5.00718 4.33321 5.03268V7.79305C4.33246 7.9333 4.40746 8.06343 4.52933 8.1328L7.44646 9.81693L6.43658 10.4001C6.42646 10.4068 6.41371 10.4079 6.40246 10.4031L3.98671 9.0073C2.91308 8.38555 2.54521 7.01155 3.16396 5.93605ZM11.4612 7.86693L8.54408 6.18243L9.55396 5.59968C9.56408 5.59293 9.57683 5.59181 9.58808 5.59668L12.0038 6.9913C13.0793 7.61268 13.448 8.98855 12.8266 10.0641C12.5637 10.5193 12.1497 10.8681 11.6566 11.0496V8.20668C11.6577 8.06643 11.5827 7.93668 11.4612 7.86693ZM12.4662 6.35418C12.4486 6.34331 12.4175 6.32455 12.3953 6.3118L10.0058 4.93181C9.88471 4.86093 9.73471 4.86093 9.61321 4.93181L6.69608 6.6163V5.45005C6.69533 5.43805 6.70096 5.42643 6.71033 5.41893L9.12571 4.02543C10.2016 3.40481 11.5771 3.77418 12.1973 4.85043C12.4595 5.30493 12.5551 5.83706 12.4662 6.35418ZM6.14708 8.4328L5.13683 7.84968C5.12596 7.84443 5.11883 7.83393 5.11733 7.82193V5.03231C5.11808 3.79031 6.12571 2.78381 7.36771 2.78456C7.89308 2.78456 8.40158 2.96906 8.80546 3.30506C8.78708 3.31481 8.75558 3.33243 8.73458 3.34518L6.34508 4.72518C6.22283 4.79456 6.14783 4.92431 6.14858 5.06493L6.14708 8.4328ZM6.69571 7.25005L7.99508 6.49968L9.29446 7.24968V8.75005L7.99508 9.50005L6.69571 8.75005V7.25005Z" fill="white"></path> </svg></span> GPT-4o Mini</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999]  aifnmjmchg-popper aifnmjmchg-popper-y aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-900 ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[170px] aifnmjmchg-w-full"><div class="aifnmjmchg-text-xs"><div class="aifnmjmchg-text-xs aifnmjmchg-break-words aifnmjmchg-whitespace-pre-wrap aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Sangat cepat, cocok untuk sebagian besar tugas sehari-hari.</div><div class="aifnmjmchg-text-[10px] aifnmjmchg-opacity-60 aifnmjmchg-mt-1 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Biaya 1 Query Cepat.</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><div class="aifnmjmchg-flex aifnmjmchg-px-4 aifnmjmchg-py-2.5 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700 hover:aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer" style=""><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-gap-2 aifnmjmchg-text-[12px]"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-GPT-4o" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"> <rect width="16" height="16" rx="8" fill="#AB68E1"></rect> <path d="M13.1348 6.91143C13.4071 6.0943 13.3133 5.19918 12.878 4.45593C12.2232 3.31593 10.907 2.72943 9.62146 3.00543C9.04958 2.36118 8.22796 1.99481 7.36658 2.00006C6.05258 1.99706 4.88671 2.84306 4.48246 4.09331C3.63833 4.26618 2.90971 4.79456 2.48333 5.54343C1.82371 6.68043 1.97408 8.11368 2.85533 9.08868C2.58308 9.9058 2.67683 10.8009 3.11221 11.5442C3.76696 12.6842 5.08321 13.2707 6.36871 12.9947C6.94021 13.6389 7.76221 14.0053 8.62358 13.9997C9.93833 14.0031 11.1046 13.1563 11.5088 11.9049C12.353 11.7321 13.0816 11.2037 13.508 10.4548C14.1668 9.3178 14.0157 7.88643 13.1348 6.91143ZM8.62433 13.2156C8.09821 13.2163 7.58858 13.0322 7.18471 12.6951C7.20308 12.6853 7.23496 12.6677 7.25558 12.6549L9.64508 11.2749C9.76733 11.2056 9.84233 11.0754 9.84158 10.9348V7.56618L10.8515 8.1493C10.8623 8.15455 10.8695 8.16505 10.871 8.17705V10.9667C10.8695 12.2072 9.86483 13.2129 8.62433 13.2156ZM3.79283 11.1519C3.52921 10.6967 3.43433 10.1631 3.52471 9.64518C3.54233 9.65568 3.57346 9.6748 3.59558 9.68755L5.98508 11.0676C6.10621 11.1384 6.25621 11.1384 6.37771 11.0676L9.29483 9.38305V10.5493C9.29558 10.5613 9.28996 10.5729 9.28058 10.5804L6.86521 11.9751C5.78933 12.5946 4.41496 12.2263 3.79283 11.1519ZM3.16396 5.93605C3.42646 5.48006 3.84083 5.1313 4.33433 4.95018C4.33433 4.97081 4.33321 5.00718 4.33321 5.03268V7.79305C4.33246 7.9333 4.40746 8.06343 4.52933 8.1328L7.44646 9.81693L6.43658 10.4001C6.42646 10.4068 6.41371 10.4079 6.40246 10.4031L3.98671 9.0073C2.91308 8.38555 2.54521 7.01155 3.16396 5.93605ZM11.4612 7.86693L8.54408 6.18243L9.55396 5.59968C9.56408 5.59293 9.57683 5.59181 9.58808 5.59668L12.0038 6.9913C13.0793 7.61268 13.448 8.98855 12.8266 10.0641C12.5637 10.5193 12.1497 10.8681 11.6566 11.0496V8.20668C11.6577 8.06643 11.5827 7.93668 11.4612 7.86693ZM12.4662 6.35418C12.4486 6.34331 12.4175 6.32455 12.3953 6.3118L10.0058 4.93181C9.88471 4.86093 9.73471 4.86093 9.61321 4.93181L6.69608 6.6163V5.45005C6.69533 5.43805 6.70096 5.42643 6.71033 5.41893L9.12571 4.02543C10.2016 3.40481 11.5771 3.77418 12.1973 4.85043C12.4595 5.30493 12.5551 5.83706 12.4662 6.35418ZM6.14708 8.4328L5.13683 7.84968C5.12596 7.84443 5.11883 7.83393 5.11733 7.82193V5.03231C5.11808 3.79031 6.12571 2.78381 7.36771 2.78456C7.89308 2.78456 8.40158 2.96906 8.80546 3.30506C8.78708 3.31481 8.75558 3.33243 8.73458 3.34518L6.34508 4.72518C6.22283 4.79456 6.14783 4.92431 6.14858 5.06493L6.14708 8.4328ZM6.69571 7.25005L7.99508 6.49968L9.29446 7.24968V8.75005L7.99508 9.50005L6.69571 8.75005V7.25005Z" fill="white"></path> </svg></span> GPT-4o</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999]  aifnmjmchg-popper aifnmjmchg-popper-y aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-900 ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[170px] aifnmjmchg-w-full"><div class="aifnmjmchg-text-xs"><div class="aifnmjmchg-text-xs aifnmjmchg-break-words aifnmjmchg-whitespace-pre-wrap aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Model unggulan terbaru dan paling canggih dari OpenAI yang dapat berpikir melintasi audio, visual, dan teks secara real time.</div><div class="aifnmjmchg-text-[10px] aifnmjmchg-opacity-60 aifnmjmchg-mt-1 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Memerlukan 1 Kueri Lanjutan.</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><div class="aifnmjmchg-flex aifnmjmchg-px-4 aifnmjmchg-py-2.5 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700 hover:aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer" style=""><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-gap-2 aifnmjmchg-text-[12px]"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-o1 Mini" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"> <path d="M0 8C0 3.58172 3.58172 0 8 0C12.4183 0 16 3.58172 16 8C16 12.4183 12.4183 16 8 16C3.58172 16 0 12.4183 0 8Z" fill="#AFDE75"></path> <g filter="url(#o1mini_filter)"> <path d="M13.1348 6.91143C13.4071 6.0943 13.3133 5.19918 12.878 4.45593C12.2232 3.31593 10.907 2.72943 9.62146 3.00543C9.04958 2.36118 8.22796 1.99481 7.36658 2.00006C6.05258 1.99706 4.88671 2.84306 4.48246 4.09331C3.63833 4.26618 2.90971 4.79456 2.48333 5.54343C1.82371 6.68043 1.97408 8.11368 2.85533 9.08868C2.58308 9.9058 2.67683 10.8009 3.11221 11.5442C3.76696 12.6842 5.08321 13.2707 6.36871 12.9947C6.94021 13.6389 7.76221 14.0053 8.62358 13.9997C9.93833 14.0031 11.1046 13.1563 11.5088 11.9049C12.353 11.7321 13.0816 11.2037 13.508 10.4548C14.1668 9.3178 14.0157 7.88643 13.1348 6.91143ZM8.62433 13.2156C8.09821 13.2163 7.58858 13.0322 7.18471 12.6951C7.20308 12.6853 7.23496 12.6677 7.25558 12.6549L9.64508 11.2749C9.76733 11.2056 9.84233 11.0754 9.84158 10.9348V7.56618L10.8515 8.1493C10.8623 8.15455 10.8695 8.16505 10.871 8.17705V10.9667C10.8695 12.2072 9.86483 13.2129 8.62433 13.2156ZM3.79283 11.1519C3.52921 10.6967 3.43433 10.1631 3.52471 9.64518C3.54233 9.65568 3.57346 9.6748 3.59558 9.68755L5.98508 11.0676C6.10621 11.1384 6.25621 11.1384 6.37771 11.0676L9.29483 9.38305V10.5493C9.29558 10.5613 9.28996 10.5729 9.28058 10.5804L6.86521 11.9751C5.78933 12.5946 4.41496 12.2263 3.79283 11.1519ZM3.16396 5.93605C3.42646 5.48006 3.84083 5.1313 4.33433 4.95018C4.33433 4.97081 4.33321 5.00718 4.33321 5.03268V7.79305C4.33246 7.9333 4.40746 8.06343 4.52933 8.1328L7.44646 9.81693L6.43658 10.4001C6.42646 10.4068 6.41371 10.4079 6.40246 10.4031L3.98671 9.0073C2.91308 8.38555 2.54521 7.01155 3.16396 5.93605ZM11.4612 7.86693L8.54408 6.18243L9.55396 5.59968C9.56408 5.59293 9.57683 5.59181 9.58808 5.59668L12.0038 6.9913C13.0793 7.61268 13.448 8.98855 12.8266 10.0641C12.5637 10.5193 12.1497 10.8681 11.6566 11.0496V8.20668C11.6577 8.06643 11.5827 7.93668 11.4612 7.86693ZM12.4662 6.35418C12.4486 6.34331 12.4175 6.32455 12.3953 6.3118L10.0058 4.93181C9.88471 4.86093 9.73471 4.86093 9.61321 4.93181L6.69608 6.6163V5.45005C6.69533 5.43805 6.70096 5.42643 6.71033 5.41893L9.12571 4.02543C10.2016 3.40481 11.5771 3.77418 12.1973 4.85043C12.4595 5.30493 12.5551 5.83706 12.4662 6.35418ZM6.14708 8.4328L5.13683 7.84968C5.12596 7.84443 5.11883 7.83393 5.11733 7.82193V5.03231C5.11808 3.79031 6.12571 2.78381 7.36771 2.78456C7.89308 2.78456 8.40158 2.96906 8.80546 3.30506C8.78708 3.31481 8.75558 3.33243 8.73458 3.34518L6.34508 4.72518C6.22283 4.79456 6.14783 4.92431 6.14858 5.06493L6.14708 8.4328ZM6.69571 7.25005L7.99508 6.49968L9.29446 7.24968V8.75005L7.99508 9.50005L6.69571 8.75005V7.25005Z" fill="white"></path> </g> <defs> <filter id="o1mini_filter" x="0.0749512" y="0" width="15.8406" height="15.9998" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"> <feflood flood-opacity="0" result="BackgroundImageFix"></feflood> <fecolormatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"></fecolormatrix> <feoffset></feoffset> <fegaussianblur stdDeviation="1"></fegaussianblur> <fecomposite in2="hardAlpha" operator="out"></fecomposite> <fecolormatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.2 0"></fecolormatrix> <feblend mode="normal" in2="BackgroundImageFix" result="o1mini_dropshadow"></feblend> <feblend mode="normal" in="SourceGraphic" in2="o1mini_dropshadow" result="shape"></feblend> </filter> </defs> </svg></span> o1 Mini</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999]  aifnmjmchg-popper aifnmjmchg-popper-y aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-900 ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[170px] aifnmjmchg-w-full"><div class="aifnmjmchg-text-xs"><div class="aifnmjmchg-text-xs aifnmjmchg-break-words aifnmjmchg-whitespace-pre-wrap aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Model penalaran dasar OpenAI untuk penalaran STEM, khususnya matematika dan pemrograman. Terbaik untuk tugas-tugas yang membutuhkan logika kuat tanpa pengetahuan luas.</div><div class="aifnmjmchg-text-[10px] aifnmjmchg-opacity-60 aifnmjmchg-mt-1 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Biaya 5 Kueri Lanjutan</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><div class="aifnmjmchg-flex aifnmjmchg-px-4 aifnmjmchg-py-2.5 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700 hover:aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer" style=""><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-gap-2 aifnmjmchg-text-[12px]"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-o1 Preview" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"> <path d="M0 8C0 3.58172 3.58172 0 8 0C12.4183 0 16 3.58172 16 8C16 12.4183 12.4183 16 8 16C3.58172 16 0 12.4183 0 8Z" fill="url(#o1_linear)"></path> <g filter="url(#o1_filter)"> <path d="M13.1348 6.91143C13.4071 6.0943 13.3133 5.19918 12.878 4.45593C12.2232 3.31593 10.907 2.72943 9.62146 3.00543C9.04958 2.36118 8.22796 1.99481 7.36658 2.00006C6.05258 1.99706 4.88671 2.84306 4.48246 4.09331C3.63833 4.26618 2.90971 4.79456 2.48333 5.54343C1.82371 6.68043 1.97408 8.11368 2.85533 9.08868C2.58308 9.9058 2.67683 10.8009 3.11221 11.5442C3.76696 12.6842 5.08321 13.2707 6.36871 12.9947C6.94021 13.6389 7.76221 14.0053 8.62358 13.9997C9.93833 14.0031 11.1046 13.1563 11.5088 11.9049C12.353 11.7321 13.0816 11.2037 13.508 10.4548C14.1668 9.3178 14.0157 7.88643 13.1348 6.91143ZM8.62433 13.2156C8.09821 13.2163 7.58858 13.0322 7.18471 12.6951C7.20308 12.6853 7.23496 12.6677 7.25558 12.6549L9.64508 11.2749C9.76733 11.2056 9.84233 11.0754 9.84158 10.9348V7.56618L10.8515 8.1493C10.8623 8.15455 10.8695 8.16505 10.871 8.17705V10.9667C10.8695 12.2072 9.86483 13.2129 8.62433 13.2156ZM3.79283 11.1519C3.52921 10.6967 3.43433 10.1631 3.52471 9.64518C3.54233 9.65568 3.57346 9.6748 3.59558 9.68755L5.98508 11.0676C6.10621 11.1384 6.25621 11.1384 6.37771 11.0676L9.29483 9.38305V10.5493C9.29558 10.5613 9.28996 10.5729 9.28058 10.5804L6.86521 11.9751C5.78933 12.5946 4.41496 12.2263 3.79283 11.1519ZM3.16396 5.93605C3.42646 5.48006 3.84083 5.1313 4.33433 4.95018C4.33433 4.97081 4.33321 5.00718 4.33321 5.03268V7.79305C4.33246 7.9333 4.40746 8.06343 4.52933 8.1328L7.44646 9.81693L6.43658 10.4001C6.42646 10.4068 6.41371 10.4079 6.40246 10.4031L3.98671 9.0073C2.91308 8.38555 2.54521 7.01155 3.16396 5.93605ZM11.4612 7.86693L8.54408 6.18243L9.55396 5.59968C9.56408 5.59293 9.57683 5.59181 9.58808 5.59668L12.0038 6.9913C13.0793 7.61268 13.448 8.98855 12.8266 10.0641C12.5637 10.5193 12.1497 10.8681 11.6566 11.0496V8.20668C11.6577 8.06643 11.5827 7.93668 11.4612 7.86693ZM12.4662 6.35418C12.4486 6.34331 12.4175 6.32455 12.3953 6.3118L10.0058 4.93181C9.88471 4.86093 9.73471 4.86093 9.61321 4.93181L6.69608 6.6163V5.45005C6.69533 5.43805 6.70096 5.42643 6.71033 5.41893L9.12571 4.02543C10.2016 3.40481 11.5771 3.77418 12.1973 4.85043C12.4595 5.30493 12.5551 5.83706 12.4662 6.35418ZM6.14708 8.4328L5.13683 7.84968C5.12596 7.84443 5.11883 7.83393 5.11733 7.82193V5.03231C5.11808 3.79031 6.12571 2.78381 7.36771 2.78456C7.89308 2.78456 8.40158 2.96906 8.80546 3.30506C8.78708 3.31481 8.75558 3.33243 8.73458 3.34518L6.34508 4.72518C6.22283 4.79456 6.14783 4.92431 6.14858 5.06493L6.14708 8.4328ZM6.69571 7.25005L7.99508 6.49968L9.29446 7.24968V8.75005L7.99508 9.50005L6.69571 8.75005V7.25005Z" fill="white"></path> </g> <defs> <filter id="o1_filter" x="0.0749512" y="0" width="15.8406" height="15.9998" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"> <feflood flood-opacity="0" result="BackgroundImageFix"></feflood> <fecolormatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"></fecolormatrix> <feoffset></feoffset> <fegaussianblur stdDeviation="1"></fegaussianblur> <fecomposite in2="hardAlpha" operator="out"></fecomposite> <fecolormatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.3 0"></fecolormatrix> <feblend mode="normal" in2="BackgroundImageFix" result="o1_dropshadow"></feblend> <feblend mode="normal" in="SourceGraphic" in2="o1_dropshadow" result="shape"></feblend> </filter> <lineargradient id="o1_linear" x1="2" y1="2" x2="14" y2="14" gradientUnits="userSpaceOnUse"> <stop offset="0.2" stop-color="#F9D914"></stop> <stop offset="0.6" stop-color="#D8E0A2"></stop> <stop offset="1" stop-color="#56A9CB"></stop> </lineargradient> </defs> </svg></span> o1 Preview</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999]  aifnmjmchg-popper aifnmjmchg-popper-y aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-900 ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[170px] aifnmjmchg-w-full"><div class="aifnmjmchg-text-xs"><div class="aifnmjmchg-text-xs aifnmjmchg-break-words aifnmjmchg-whitespace-pre-wrap aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Model penalaran canggih OpenAI untuk tugas-tugas kompleks dalam sains, matematika, dan pemrograman. Membutuhkan waktu lebih lama untuk berpikir, menyampaikan tanggapan yang dipertimbangkan dengan baik terhadap masalah yang menantang.</div><div class="aifnmjmchg-text-[10px] aifnmjmchg-opacity-60 aifnmjmchg-mt-1 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Biaya 15 Kueri Lanjutan</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><div class="aifnmjmchg-flex aifnmjmchg-px-4 aifnmjmchg-py-2.5 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700 hover:aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer" style=""><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-gap-2 aifnmjmchg-text-[12px]"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-Claude 3 Haiku" width="16" height="16" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"><rect width="100%" height="100%" rx="8" fill="#F0E8D6"></rect><path d="M4.67668 9.70835L6.71408 8.5651L6.74817 8.46546L6.71408 8.41039H6.61444L6.27356 8.38941L5.10934 8.35795L4.09981 8.31599L3.12176 8.26355L2.87528 8.21111L2.64453 7.90694L2.66813 7.75486L2.87528 7.61588L3.17158 7.64211L3.82711 7.68668L4.81041 7.75486L5.52363 7.79681L6.58035 7.90694H6.74817L6.77177 7.83877L6.71408 7.79681L6.6695 7.75486L5.65212 7.06524L4.55082 6.33628L3.97395 5.91674L3.66192 5.70435L3.50459 5.50507L3.43642 5.06979L3.71961 4.75776L4.09981 4.78398L4.19683 4.8102L4.58229 5.1065L5.40564 5.74368L6.48071 6.53557L6.63804 6.66667L6.70097 6.6221L6.70884 6.59063L6.63804 6.47264L6.0533 5.41592L5.42924 4.34084L5.15129 3.89508L5.07787 3.62762C5.05165 3.51749 5.03329 3.42572 5.03329 3.31297L5.35582 2.87507L5.53412 2.81738L5.96415 2.87507L6.14508 3.0324L6.41253 3.64335L6.84519 4.60568L7.51645 5.91412L7.71311 6.3022L7.818 6.66143L7.85733 6.77156H7.92551V6.70863L7.98057 5.97181L8.08283 5.06717L8.18247 3.90295L8.21656 3.57518L8.37913 3.18186L8.70166 2.96947L8.95338 3.09008L9.16053 3.38639L9.13169 3.5778L9.00845 4.37755L8.76721 5.63093L8.60988 6.47001H8.70166L8.80654 6.36513L9.23133 5.80137L9.94455 4.90984L10.2592 4.55586L10.6263 4.16516L10.8623 3.97899H11.3081L11.6358 4.4667L11.489 4.97015L11.0301 5.55227L10.6499 6.04523L10.1045 6.77942L9.76362 7.36678L9.79509 7.41398L9.87637 7.40611L11.1088 7.1439L11.7748 7.02328L12.5693 6.88693L12.9285 7.05475L12.9679 7.22519L12.8263 7.57393L11.9767 7.7837L10.9803 7.98298L9.49616 8.33435L9.47781 8.34746L9.49878 8.37368L10.1674 8.43661L10.4532 8.45234H11.1533L12.4565 8.54936L12.7974 8.77487L13.002 9.05019L12.9679 9.25996L12.4434 9.52742L11.7355 9.3596L10.0835 8.96628L9.51714 8.82469H9.43848V8.87189L9.91046 9.33338L10.7758 10.1148L11.8587 11.1217L11.9138 11.3708L11.7748 11.5674L11.628 11.5465L10.6761 10.8306L10.309 10.5081L9.47781 9.80799H9.42274V9.88141L9.61416 10.162L10.6263 11.6828L10.6787 12.1496L10.6053 12.3016L10.3431 12.3934L10.0547 12.341L9.46207 11.5097L8.85112 10.5736L8.35816 9.73457L8.29785 9.76865L8.00679 12.9021L7.87044 13.0621L7.55578 13.1827L7.29357 12.9834L7.1546 12.6609L7.29357 12.0237L7.46139 11.1925L7.59774 10.5317L7.72098 9.71097L7.7944 9.43827L7.78915 9.41991L7.72885 9.42778L7.11002 10.2773L6.16868 11.5491L5.42399 12.3462L5.24569 12.417L4.93627 12.2571L4.96512 11.9712L5.13818 11.7169L6.16868 10.4058L6.79012 9.59297L7.19131 9.12361L7.18869 9.05544H7.16509L4.42758 10.8332L3.93986 10.8962L3.73009 10.6995L3.75632 10.377L3.85596 10.2721L4.67931 9.70572L4.67668 9.70835Z" fill="#D97757"></path></svg></span> Claude 3 Haiku</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999]  aifnmjmchg-popper aifnmjmchg-popper-y aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-900 ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[170px] aifnmjmchg-w-full"><div class="aifnmjmchg-text-xs"><div class="aifnmjmchg-text-xs aifnmjmchg-break-words aifnmjmchg-whitespace-pre-wrap aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Model paling kompak Anthropic, dirancang untuk responsivitas yang hampir seketika dan pengalaman AI yang mulus yang meniru interaksi manusia.</div><div class="aifnmjmchg-text-[10px] aifnmjmchg-opacity-60 aifnmjmchg-mt-1 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Biaya 1 Query Cepat.</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><div class="aifnmjmchg-flex aifnmjmchg-px-4 aifnmjmchg-py-2.5 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700 hover:aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer" style=""><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-gap-2 aifnmjmchg-text-[12px]"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-Claude 3 Sonnet" width="16" height="16" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"><rect width="100%" height="100%" rx="8" fill="#F0E8D6"></rect><path d="M4.67668 9.70835L6.71408 8.5651L6.74817 8.46546L6.71408 8.41039H6.61444L6.27356 8.38941L5.10934 8.35795L4.09981 8.31599L3.12176 8.26355L2.87528 8.21111L2.64453 7.90694L2.66813 7.75486L2.87528 7.61588L3.17158 7.64211L3.82711 7.68668L4.81041 7.75486L5.52363 7.79681L6.58035 7.90694H6.74817L6.77177 7.83877L6.71408 7.79681L6.6695 7.75486L5.65212 7.06524L4.55082 6.33628L3.97395 5.91674L3.66192 5.70435L3.50459 5.50507L3.43642 5.06979L3.71961 4.75776L4.09981 4.78398L4.19683 4.8102L4.58229 5.1065L5.40564 5.74368L6.48071 6.53557L6.63804 6.66667L6.70097 6.6221L6.70884 6.59063L6.63804 6.47264L6.0533 5.41592L5.42924 4.34084L5.15129 3.89508L5.07787 3.62762C5.05165 3.51749 5.03329 3.42572 5.03329 3.31297L5.35582 2.87507L5.53412 2.81738L5.96415 2.87507L6.14508 3.0324L6.41253 3.64335L6.84519 4.60568L7.51645 5.91412L7.71311 6.3022L7.818 6.66143L7.85733 6.77156H7.92551V6.70863L7.98057 5.97181L8.08283 5.06717L8.18247 3.90295L8.21656 3.57518L8.37913 3.18186L8.70166 2.96947L8.95338 3.09008L9.16053 3.38639L9.13169 3.5778L9.00845 4.37755L8.76721 5.63093L8.60988 6.47001H8.70166L8.80654 6.36513L9.23133 5.80137L9.94455 4.90984L10.2592 4.55586L10.6263 4.16516L10.8623 3.97899H11.3081L11.6358 4.4667L11.489 4.97015L11.0301 5.55227L10.6499 6.04523L10.1045 6.77942L9.76362 7.36678L9.79509 7.41398L9.87637 7.40611L11.1088 7.1439L11.7748 7.02328L12.5693 6.88693L12.9285 7.05475L12.9679 7.22519L12.8263 7.57393L11.9767 7.7837L10.9803 7.98298L9.49616 8.33435L9.47781 8.34746L9.49878 8.37368L10.1674 8.43661L10.4532 8.45234H11.1533L12.4565 8.54936L12.7974 8.77487L13.002 9.05019L12.9679 9.25996L12.4434 9.52742L11.7355 9.3596L10.0835 8.96628L9.51714 8.82469H9.43848V8.87189L9.91046 9.33338L10.7758 10.1148L11.8587 11.1217L11.9138 11.3708L11.7748 11.5674L11.628 11.5465L10.6761 10.8306L10.309 10.5081L9.47781 9.80799H9.42274V9.88141L9.61416 10.162L10.6263 11.6828L10.6787 12.1496L10.6053 12.3016L10.3431 12.3934L10.0547 12.341L9.46207 11.5097L8.85112 10.5736L8.35816 9.73457L8.29785 9.76865L8.00679 12.9021L7.87044 13.0621L7.55578 13.1827L7.29357 12.9834L7.1546 12.6609L7.29357 12.0237L7.46139 11.1925L7.59774 10.5317L7.72098 9.71097L7.7944 9.43827L7.78915 9.41991L7.72885 9.42778L7.11002 10.2773L6.16868 11.5491L5.42399 12.3462L5.24569 12.417L4.93627 12.2571L4.96512 11.9712L5.13818 11.7169L6.16868 10.4058L6.79012 9.59297L7.19131 9.12361L7.18869 9.05544H7.16509L4.42758 10.8332L3.93986 10.8962L3.73009 10.6995L3.75632 10.377L3.85596 10.2721L4.67931 9.70572L4.67668 9.70835Z" fill="black" fill-opacity="0.92"></path></svg></span> Claude 3 Sonnet</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999]  aifnmjmchg-popper aifnmjmchg-popper-y aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-900 ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[170px] aifnmjmchg-w-full"><div class="aifnmjmchg-text-xs"><div class="aifnmjmchg-text-xs aifnmjmchg-break-words aifnmjmchg-whitespace-pre-wrap aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Sangat cepat, cocok untuk sebagian besar tugas sehari-hari.</div><div class="aifnmjmchg-text-[10px] aifnmjmchg-opacity-60 aifnmjmchg-mt-1 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Memerlukan 1 Kueri Lanjutan.</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><div class="aifnmjmchg-flex aifnmjmchg-px-4 aifnmjmchg-py-2.5 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700 hover:aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer" style=""><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-gap-2 aifnmjmchg-text-[12px]"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-Claude 3 Opus" width="16" height="16" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"><rect width="100%" height="100%" rx="8" fill="#C36E51"></rect><path d="M4.67668 9.70835L6.71408 8.5651L6.74817 8.46546L6.71408 8.41039H6.61444L6.27356 8.38941L5.10934 8.35795L4.09981 8.31599L3.12176 8.26355L2.87528 8.21111L2.64453 7.90694L2.66813 7.75486L2.87528 7.61588L3.17158 7.64211L3.82711 7.68668L4.81041 7.75486L5.52363 7.79681L6.58035 7.90694H6.74817L6.77177 7.83877L6.71408 7.79681L6.6695 7.75486L5.65212 7.06524L4.55082 6.33628L3.97395 5.91674L3.66192 5.70435L3.50459 5.50507L3.43642 5.06979L3.71961 4.75776L4.09981 4.78398L4.19683 4.8102L4.58229 5.1065L5.40564 5.74368L6.48071 6.53557L6.63804 6.66667L6.70097 6.6221L6.70884 6.59063L6.63804 6.47264L6.0533 5.41592L5.42924 4.34084L5.15129 3.89508L5.07787 3.62762C5.05165 3.51749 5.03329 3.42572 5.03329 3.31297L5.35582 2.87507L5.53412 2.81738L5.96415 2.87507L6.14508 3.0324L6.41253 3.64335L6.84519 4.60568L7.51645 5.91412L7.71311 6.3022L7.818 6.66143L7.85733 6.77156H7.92551V6.70863L7.98057 5.97181L8.08283 5.06717L8.18247 3.90295L8.21656 3.57518L8.37913 3.18186L8.70166 2.96947L8.95338 3.09008L9.16053 3.38639L9.13169 3.5778L9.00845 4.37755L8.76721 5.63093L8.60988 6.47001H8.70166L8.80654 6.36513L9.23133 5.80137L9.94455 4.90984L10.2592 4.55586L10.6263 4.16516L10.8623 3.97899H11.3081L11.6358 4.4667L11.489 4.97015L11.0301 5.55227L10.6499 6.04523L10.1045 6.77942L9.76362 7.36678L9.79509 7.41398L9.87637 7.40611L11.1088 7.1439L11.7748 7.02328L12.5693 6.88693L12.9285 7.05475L12.9679 7.22519L12.8263 7.57393L11.9767 7.7837L10.9803 7.98298L9.49616 8.33435L9.47781 8.34746L9.49878 8.37368L10.1674 8.43661L10.4532 8.45234H11.1533L12.4565 8.54936L12.7974 8.77487L13.002 9.05019L12.9679 9.25996L12.4434 9.52742L11.7355 9.3596L10.0835 8.96628L9.51714 8.82469H9.43848V8.87189L9.91046 9.33338L10.7758 10.1148L11.8587 11.1217L11.9138 11.3708L11.7748 11.5674L11.628 11.5465L10.6761 10.8306L10.309 10.5081L9.47781 9.80799H9.42274V9.88141L9.61416 10.162L10.6263 11.6828L10.6787 12.1496L10.6053 12.3016L10.3431 12.3934L10.0547 12.341L9.46207 11.5097L8.85112 10.5736L8.35816 9.73457L8.29785 9.76865L8.00679 12.9021L7.87044 13.0621L7.55578 13.1827L7.29357 12.9834L7.1546 12.6609L7.29357 12.0237L7.46139 11.1925L7.59774 10.5317L7.72098 9.71097L7.7944 9.43827L7.78915 9.41991L7.72885 9.42778L7.11002 10.2773L6.16868 11.5491L5.42399 12.3462L5.24569 12.417L4.93627 12.2571L4.96512 11.9712L5.13818 11.7169L6.16868 10.4058L6.79012 9.59297L7.19131 9.12361L7.18869 9.05544H7.16509L4.42758 10.8332L3.93986 10.8962L3.73009 10.6995L3.75632 10.377L3.85596 10.2721L4.67931 9.70572L4.67668 9.70835Z" fill="black" fill-opacity="0.92"></path></svg></span> Claude 3 Opus</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999]  aifnmjmchg-popper aifnmjmchg-popper-y aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-900 ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[170px] aifnmjmchg-w-full"><div class="aifnmjmchg-text-xs"><div class="aifnmjmchg-text-xs aifnmjmchg-break-words aifnmjmchg-whitespace-pre-wrap aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Model paling kuat dari Anthropic, memberikan kinerja terkini pada tugas-tugas yang sangat kompleks dan menunjukkan kefasihan serta pemahaman seperti manusia.</div><div class="aifnmjmchg-text-[10px] aifnmjmchg-opacity-60 aifnmjmchg-mt-1 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Biaya 2 Pencarian Lanjutan.</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><div class="aifnmjmchg-flex aifnmjmchg-px-4 aifnmjmchg-py-2.5 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700 hover:aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer" style=""><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-gap-2 aifnmjmchg-text-[12px]"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-Gemini 1.5 Flash" width="16" height="16" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"><rect width="100%" height="100%" rx="8" fill="#F3F3FA"></rect><path d="M8 14C8 13.17 7.84002 12.39 7.52 11.66C7.21002 10.93 6.785 10.295 6.245 9.755C5.705 9.215 5.07 8.78998 4.34 8.48C3.61 8.15998 2.83 8 2 8C2.83 8 3.61 7.84498 4.34 7.535C5.07 7.21498 5.705 6.785 6.245 6.245C6.785 5.705 7.21002 5.07 7.52 4.34C7.84002 3.61 8 2.83 8 2C8 2.83 8.15502 3.61 8.465 4.34C8.78502 5.07 9.215 5.705 9.755 6.245C10.295 6.785 10.93 7.21498 11.66 7.535C12.39 7.84498 13.17 8 14 8C13.17 8 12.39 8.15998 11.66 8.48C10.93 8.78998 10.295 9.215 9.755 9.755C9.215 10.295 8.78502 10.93 8.465 11.66C8.15502 12.39 8 13.17 8 14Z" fill="url(#gemini_flash_linear)"></path><defs><radialgradient id="gemini_flash_linear" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(3.1909 6.87693) rotate(18.6832) scale(12.7725 102.316)"><stop offset="0.0671246" stop-color="#9168C0"></stop><stop offset="0.342551" stop-color="#5684D1"></stop><stop offset="0.672076" stop-color="#1BA1E3"></stop></radialgradient></defs></svg></span> Gemini 1.5 Flash</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999]  aifnmjmchg-popper aifnmjmchg-popper-y aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-900 ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[170px] aifnmjmchg-w-full"><div class="aifnmjmchg-text-xs"><div class="aifnmjmchg-text-xs aifnmjmchg-break-words aifnmjmchg-whitespace-pre-wrap aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Model paling seimbang milik Google, menggabungkan kemampuan dengan efisiensi secara sempurna.</div><div class="aifnmjmchg-text-[10px] aifnmjmchg-opacity-60 aifnmjmchg-mt-1 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Biaya 1 Query Cepat.</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><div class="aifnmjmchg-flex aifnmjmchg-px-4 aifnmjmchg-py-2.5 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700 hover:aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer" style=""><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-gap-2 aifnmjmchg-text-[12px]"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-Gemini 1.5 Pro" width="16" height="16" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"><rect width="100%" height="100%" rx="8" fill="#000002"></rect><path d="M8 14C8 13.17 7.84002 12.39 7.52 11.66C7.21002 10.93 6.785 10.295 6.245 9.755C5.705 9.215 5.07 8.78998 4.34 8.48C3.61 8.15998 2.83 8 2 8C2.83 8 3.61 7.84498 4.34 7.535C5.07 7.21498 5.705 6.785 6.245 6.245C6.785 5.705 7.21002 5.07 7.52 4.34C7.84002 3.61 8 2.83 8 2C8 2.83 8.15502 3.61 8.465 4.34C8.78502 5.07 9.215 5.705 9.755 6.245C10.295 6.785 10.93 7.21498 11.66 7.535C12.39 7.84498 13.17 8 14 8C13.17 8 12.39 8.15998 11.66 8.48C10.93 8.78998 10.295 9.215 9.755 9.755C9.215 10.295 8.78502 10.93 8.465 11.66C8.15502 12.39 8 13.17 8 14Z" fill="url(#gemini_flash_linear)"></path><defs><radialgradient id="gemini_flash_linear" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(3.1909 6.87693) rotate(18.6832) scale(12.7725 102.316)"><stop offset="0.0671246" stop-color="#9168C0"></stop><stop offset="0.342551" stop-color="#5684D1"></stop><stop offset="0.672076" stop-color="#1BA1E3"></stop></radialgradient></defs></svg></span> Gemini 1.5 Pro</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999]  aifnmjmchg-popper aifnmjmchg-popper-y aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-900 ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[170px] aifnmjmchg-w-full"><div class="aifnmjmchg-text-xs"><div class="aifnmjmchg-text-xs aifnmjmchg-break-words aifnmjmchg-whitespace-pre-wrap aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Model ringan Google, dioptimalkan untuk kecepatan dan efisiensi.</div><div class="aifnmjmchg-text-[10px] aifnmjmchg-opacity-60 aifnmjmchg-mt-1 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Memerlukan 1 Kueri Lanjutan.</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><div class="aifnmjmchg-flex aifnmjmchg-px-4 aifnmjmchg-py-2.5 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700 hover:aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer" style=""><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-gap-2 aifnmjmchg-text-[12px]"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-Llama 3.1 70B" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"> <rect width="16" height="16" rx="8" fill="white"></rect> <rect width="16" height="16" rx="8" fill="#F3F3FA"></rect> <path d="M2.85869 9.20519C2.85869 9.70602 2.96857 10.0905 3.11229 10.3231C3.30068 10.6278 3.58164 10.7571 3.8681 10.7571C4.23751 10.7571 4.5755 10.6654 5.22681 9.76459C5.74874 9.04257 6.36346 8.0291 6.77715 7.39372L7.47774 6.31729C7.9644 5.56972 8.52769 4.73871 9.17356 4.17541C9.70098 3.71562 10.2696 3.46021 10.842 3.46021C11.8031 3.46021 12.7185 4.01713 13.4191 5.06164C14.1858 6.20554 14.558 7.64644 14.558 9.13333C14.558 10.0173 14.3838 10.6668 14.0873 11.1799C13.8009 11.6762 13.2426 12.172 12.3034 12.172V10.7569C13.1076 10.7569 13.3082 10.018 13.3082 9.17234C13.3082 7.96729 13.0273 6.63 12.4083 5.67444C11.9691 4.99665 11.3999 4.58251 10.7736 4.58251C10.0963 4.58251 9.55122 5.09345 8.93864 6.00419C8.61296 6.48815 8.27865 7.07787 7.90325 7.74336L7.48999 8.47543C6.65997 9.94753 6.44966 10.2827 6.03459 10.8358C5.30713 11.8045 4.68587 12.1718 3.8681 12.1718C2.89792 12.1718 2.28446 11.7516 1.9045 11.1186C1.59436 10.6027 1.44202 9.92583 1.44202 9.15459L2.85869 9.20519Z" fill="#0081FB"></path> <path d="M2.55908 5.16128C3.20858 4.16011 4.1459 3.45996 5.22096 3.45996C5.84354 3.45996 6.4626 3.64423 7.1088 4.17198C7.81576 4.74885 8.56926 5.6993 9.50933 7.26508L9.84639 7.82684C10.6601 9.18242 11.123 9.87982 11.394 10.2087C11.7424 10.631 11.9865 10.7569 12.3035 10.7569C13.1076 10.7569 13.3082 10.018 13.3082 9.17237L14.558 9.13314C14.558 10.0171 14.3838 10.6666 14.0873 11.1798C13.8009 11.676 13.2426 12.1718 12.3035 12.1718C11.7196 12.1718 11.2024 12.045 10.6304 11.5054C10.1909 11.0912 9.67668 10.3555 9.28122 9.69418L8.10491 7.72927C7.51475 6.74315 6.97315 6.0079 6.66 5.67491C6.32289 5.31681 5.88958 4.88444 5.19811 4.88444C4.63849 4.88444 4.16321 5.27714 3.7655 5.87786L2.55908 5.16128Z" fill="url(#llama_flash_linear_color)"></path> <path d="M5.19808 4.88444C4.63846 4.88444 4.16318 5.27715 3.76547 5.87786C3.20305 6.72667 2.85896 7.991 2.85896 9.20517C2.85896 9.706 2.96884 10.0905 3.11257 10.3231L1.9045 11.1185C1.59436 10.6027 1.44202 9.92581 1.44202 9.15457C1.44202 7.75201 1.82698 6.29018 2.55905 5.16128C3.20855 4.16011 4.14587 3.45996 5.22093 3.45996L5.19808 4.88444Z" fill="url(#llama_flash_linear_color)"></path> <defs> <lineargradient id="llama_flash_linear_color" x1="4.28529" y1="7.5901" x2="13.3163" y2="8.04621" gradientUnits="userSpaceOnUse"> <stop stop-color="#0064E1"></stop> <stop offset="0.4" stop-color="#0064E1"></stop> <stop offset="0.83" stop-color="#0073EE"></stop> <stop offset="1" stop-color="#0082FB"></stop> </lineargradient> <lineargradient id="paint1_linear_38187_34499_:r11:" x1="3.33145" y1="9.79994" x2="3.33145" y2="6.47032" gradientUnits="userSpaceOnUse"> <stop stop-color="#0082FB"></stop> <stop offset="1" stop-color="#0064E0"></stop> </lineargradient> </defs> </svg></span> Llama 3.1 70B</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999]  aifnmjmchg-popper aifnmjmchg-popper-y aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-900 ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[170px] aifnmjmchg-w-full"><div class="aifnmjmchg-text-xs"><div class="aifnmjmchg-text-xs aifnmjmchg-break-words aifnmjmchg-whitespace-pre-wrap aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Model serbaguna Meta, unggul dalam ringkasan bentuk panjang, percakapan multibahasa, dan bantuan pemrograman.</div><div class="aifnmjmchg-text-[10px] aifnmjmchg-opacity-60 aifnmjmchg-mt-1 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Biaya 1 Query Cepat.</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><div class="aifnmjmchg-flex aifnmjmchg-px-4 aifnmjmchg-py-2.5 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700 hover:aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer" style=""><div class="aifnmjmchg-w-full"><div class="aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-ai-aifnmjmchgicon aifnmjmchg-flex aifnmjmchg-gap-2 aifnmjmchg-text-[12px]"><span><svg class="aifnmjmchg-w-[16px] aifnmjmchg-h-[16px] aifnmjmchg-Llama 3.1 405B" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"> <rect width="16" height="16" rx="8" fill="url(#llama_flash_linear_color_1)"></rect> <rect width="16" height="16" rx="8" fill="url(#llama_flash_linear_color_1)"></rect> <path fill-rule="evenodd" clip-rule="evenodd" d="M9.05626 4.53918C9.53096 4.12535 10.0427 3.89546 10.5579 3.89546C11.4229 3.89546 12.2468 4.39672 12.8774 5.33682C13.5675 6.36638 13.9025 7.66325 13.9025 9.00152C13.9025 9.79713 13.7457 10.3817 13.4788 10.8436C13.221 11.2902 12.7185 11.7364 11.8733 11.7364C11.3478 11.7364 10.8823 11.6222 10.3675 11.1365C9.97189 10.7637 9.50905 10.1016 9.15313 9.50633L8.09439 7.73782C8.0642 7.68737 8.03415 7.63765 8.00426 7.58868L7.91292 7.75048L7.54097 8.40938C6.79391 9.73434 6.60462 10.036 6.23104 10.5338C5.5763 11.4057 5.01714 11.7362 4.28111 11.7362C3.40791 11.7362 2.85577 11.3581 2.51379 10.7883C2.23465 10.3241 2.09753 9.7148 2.09753 9.02065C2.09753 7.75829 2.44402 6.44258 3.10291 5.42652C3.68749 4.52543 4.53112 3.89526 5.49872 3.89526C6.05906 3.89526 6.61624 4.06111 7.19785 4.53611C7.50448 4.78632 7.82084 5.11461 8.16103 5.54533C8.43741 5.17199 8.73552 4.8189 9.05626 4.53918ZM3.60085 10.0724C3.4715 9.863 3.3726 9.51696 3.3726 9.06619C3.3726 7.97339 3.68254 6.83544 4.18874 6.07147C4.54669 5.53081 4.97447 5.17735 5.47815 5.17735C6.1005 5.17735 6.4905 5.56651 6.79391 5.88881C6.94538 6.04988 7.15623 6.31551 7.40134 6.66455L6.89938 7.43579C6.52704 8.00766 5.97377 8.91983 5.50401 9.56967C4.9178 10.3805 4.6136 10.463 4.28111 10.463C4.02329 10.463 3.77041 10.3466 3.60085 10.0724ZM12.7776 9.03662C12.7776 9.79773 12.597 10.4628 11.8733 10.4628C11.5879 10.4628 11.3683 10.3495 11.0547 9.96941C10.8108 9.67341 10.3942 9.04572 9.6618 7.82564L9.35843 7.32003C9.14209 6.95969 8.93672 6.63555 8.74022 6.34399C8.77523 6.28974 8.81008 6.23678 8.84482 6.18515C9.39616 5.36545 9.88674 4.90559 10.4964 4.90559C11.06 4.90559 11.5724 5.27833 11.9677 5.88837C12.5247 6.74842 12.7776 7.95203 12.7776 9.03662Z" fill="white"></path> <defs> <lineargradient id="llama_flash_linear_color_1" x1="14" y1="2" x2="2" y2="14" gradientUnits="userSpaceOnUse"> <stop stop-color="#0081FB"></stop> <stop offset="1" stop-color="#0165E2"></stop> </lineargradient> <lineargradient id="llama_flash_linear_color_1" x1="12.5" y1="1.5" x2="2.5" y2="16" gradientUnits="userSpaceOnUse"> <stop stop-color="#F0A3DB"></stop> <stop offset="1" stop-color="#006AFF"></stop> </lineargradient> </defs> </svg></span> Llama 3.1 405B</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999]  aifnmjmchg-popper aifnmjmchg-popper-y aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-900 ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[170px] aifnmjmchg-w-full"><div class="aifnmjmchg-text-xs"><div class="aifnmjmchg-text-xs aifnmjmchg-break-words aifnmjmchg-whitespace-pre-wrap aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Model open-source terkuat milik Meta, bersaing dengan asisten AI terbaik dalam pengetahuan umum, matematika, dan kemampuan multibahasa.</div><div class="aifnmjmchg-text-[10px] aifnmjmchg-opacity-60 aifnmjmchg-mt-1 aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800">Memerlukan 1 Kueri Lanjutan.</div></div></div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li></div></ul></div></div><span class="aifnmjmchg-hide aifnmjmchg-my-2.5 aifnmjmchg-left-[-8px]"></span><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-relative aifnmjmchg-space-x-1 aifnmjmchg-grid-flow-row"><button data-aifnmjmchg-dropdown-toggle="aifnmjmchg-credit-dropdown" class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-relative dark:aifnmjmchg-text-neutral-200 aifnmjmchg-border aifnmjmchg-rounded-full aifnmjmchg-w-[45px]"><img src="chrome-extension://fnmihdojmnkclgjpcoonokmkhjpjechg/aitopia//assets/images/coin.png" width="16px" height="16px" alt="coin image" class="aifnmjmchg-w-4 aifnmjmchg-h-4"><div class="aifnmjmchg-text-sm">10</div></button><button type="button" id="aifnmjmchg-pricing" class="aifnmjmchg-text-neutral-500 hover:aifnmjmchg-text-neutral-50 hover:aifnmjmchg-bg-green-700 aifnmjmchg-ml-1 aifnmjmchg-rounded-lg focus:aifnmjmchg-outline-none aifnmjmchg-text-[10px] aifnmjmchg-px-1 aifnmjmchg-py-1 aifnmjmchg-text-center aifnmjmchg-pricing">Tingkatkan</button></div><div id="aifnmjmchg-credit-dropdown" class="aifnmjmchg-z-20 aifnmjmchg-left-0 aifnmjmchg-bottom-[40px] aifnmjmchg-width-full aifnmjmchg-absolute aifnmjmchg-hide aifnmjmchg-w-full aifnmjmchg-max-w-[220px] aifnmjmchg-bg-white aifnmjmchg-divide-y aifnmjmchg-divide-neutral-100 aifnmjmchg-rounded-lg aifnmjmchg-shadow dark:aifnmjmchg-bg-neutral-900 dark:aifnmjmchg-divide-neutral-700"><div class="aifnmjmchg-block aifnmjmchg-px-3 aifnmjmchg-py-3 aifnmjmchg-font-medium aifnmjmchg-text-center aifnmjmchg-text-neutral-700 aifnmjmchg-rounded-t-lg aifnmjmchg-bg-neutral-50 dark:aifnmjmchg-bg-neutral-950 dark:aifnmjmchg-text-white"><span class="aifnmjmchg-font-bold">Free Rencana</span><button type="button" class="aifnmjmchg-text-white aifnmjmchg-bg-green-700 hover:aifnmjmchg-opacity-90 focus:aifnmjmchg-outline-none focus:aifnmjmchg-ring-4 focus:aifnmjmchg-ring-green-300 aifnmjmchg-font-medium aifnmjmchg-rounded-full aifnmjmchg-text-sm aifnmjmchg-px-5 aifnmjmchg-py-1 aifnmjmchg-text-center aifnmjmchg-ml-5 aifnmjmchg-mr-2 dark:aifnmjmchg-bg-green-600 dark:hover:aifnmjmchg-bg-green-700 dark:focus:aifnmjmchg-ring-green-800 aifnmjmchg-pricing">Tingkatkan</button></div><div class="aifnmjmchg-divide-y aifnmjmchg-divide-neutral-100 dark:aifnmjmchg-divide-neutral-700"><div class="aifnmjmchg-flex aifnmjmchg-px-3 aifnmjmchg-py-3 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700"><div class="aifnmjmchg-w-full aifnmjmchg-px-1 aifnmjmchg-cursor-pointer"><div class="aifnmjmchg-grid aifnmjmchg-grid-cols-4 aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm aifnmjmchg-mb-1.5 dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-col-span-3">Fast Text <div class="aifnmjmchg-text-[10px] aifnmjmchg-text-neutral-500 aifnmjmchg-pt-2 dark:aifnmjmchg-text-neutral-400">GPT-4o Mini, Claude 3 Haiku, Gemini 1.5 Flash, Llama 3.1 70B, Dall-e 3, SDXL v1.0</div></div><div class="aifnmjmchg-text-right"><span class="aifnmjmchg-text-sm">10</span></div></div></div></div><div class="aifnmjmchg-flex aifnmjmchg-px-3 aifnmjmchg-py-3 hover:aifnmjmchg-bg-neutral-100 dark:hover:aifnmjmchg-bg-neutral-700"><div class="aifnmjmchg-w-full aifnmjmchg-px-1 aifnmjmchg-cursor-pointer"><div class="aifnmjmchg-grid aifnmjmchg-grid-cols-4 aifnmjmchg-gap-4 aifnmjmchg-text-neutral-900 dark:aifnmjmchg-text-white aifnmjmchg-text-sm aifnmjmchg-mb-1.5 dark:aifnmjmchg-text-neutral-400"><div class="aifnmjmchg-col-span-3">Advanced Text <div class="aifnmjmchg-text-[10px] aifnmjmchg-text-neutral-500 aifnmjmchg-pt-2 dark:aifnmjmchg-text-neutral-400">GPT-4o, o1 Mini, o1 Preview, Claude 3 Sonnet, Claude 3 Opus, Gemini 1.5 Pro, Llama 3.1 405B, SD3, SD3 Large Turbo</div></div><div class="aifnmjmchg-text-right"><span class="aifnmjmchg-text-sm">0</span></div></div></div></div></div></div><div class="aifnmjmchg-flex aifnmjmchg-flex-row aifnmjmchg-items-center aifnmjmchg-gap-1 aifnmjmchg-ml-2"><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><button class="aifnmjmchg-cursor-pointer aifnmjmchg-p-1.5 aifnmjmchg-rounded-full aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-center hover:aifnmjmchg-bg-neutral-300 dark:hover:aifnmjmchg-bg-neutral-900 aifnmjmchg-border aifnmjmchg-transition-all"><svg class="svg-inline--fa fa-scissors aifnmjmchg-w-4 aifnmjmchg-h-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="scissors" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M256 192l-39.5-39.5c4.9-12.6 7.5-26.2 7.5-40.5C224 50.1 173.9 0 112 0S0 50.1 0 112s50.1 112 112 112c14.3 0 27.9-2.7 40.5-7.5L192 256l-39.5 39.5c-12.6-4.9-26.2-7.5-40.5-7.5C50.1 288 0 338.1 0 400s50.1 112 112 112s112-50.1 112-112c0-14.3-2.7-27.9-7.5-40.5L499.2 76.8c7.1-7.1 7.1-18.5 0-25.6c-28.3-28.3-74.1-28.3-102.4 0L256 192zm22.6 150.6L396.8 460.8c28.3 28.3 74.1 28.3 102.4 0c7.1-7.1 7.1-18.5 0-25.6L342.6 278.6l-64 64zM64 112a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm48 240a48 48 0 1 1 0 96 48 48 0 1 1 0-96z"></path></svg></button><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999] aifnmjmchg-top-0 aifnmjmchg-left-1/2 aifnmjmchg-transform aifnmjmchg--translate-x-1/2 aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-900 dark:aifnmjmchg-text-gray-200 aifnmjmchg-translate-y-[-120%] ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[200px] aifnmjmchg-w-full">Ambil tangkapan layar</div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><button class="aifnmjmchg-cursor-pointer aifnmjmchg-p-1.5 aifnmjmchg-rounded-full aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-center hover:aifnmjmchg-bg-neutral-300 dark:hover:aifnmjmchg-bg-neutral-900 aifnmjmchg-border aifnmjmchg-transition-all"><svg class="svg-inline--fa fa-image aifnmjmchg-w-4 aifnmjmchg-h-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="image" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M0 96C0 60.7 28.7 32 64 32l384 0c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 96zM323.8 202.5c-4.5-6.6-11.9-10.5-19.8-10.5s-15.4 3.9-19.8 10.5l-87 127.6L170.7 297c-4.6-5.7-11.5-9-18.7-9s-14.2 3.3-18.7 9l-64 80c-5.8 7.2-6.9 17.1-2.9 25.4s12.4 13.6 21.6 13.6l96 0 32 0 208 0c8.9 0 17.1-4.9 21.2-12.8s3.6-17.4-1.4-24.7l-120-176zM112 192a48 48 0 1 0 0-96 48 48 0 1 0 0 96z"></path></svg></button><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999] aifnmjmchg-top-0 aifnmjmchg-left-1/2 aifnmjmchg-transform aifnmjmchg--translate-x-1/2 aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-900 dark:aifnmjmchg-text-gray-200 aifnmjmchg-translate-y-[-120%] ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[200px] aifnmjmchg-w-full">Unggah sebuah gambar</div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><button data-aifnmjmchg-dropdown-toggle="aifnmjmchg-pdf-upload-modal" class="aifnmjmchg-cursor-pointer aifnmjmchg-p-1.5 aifnmjmchg-rounded-full aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-center hover:aifnmjmchg-bg-neutral-300 dark:hover:aifnmjmchg-bg-neutral-900 aifnmjmchg-border aifnmjmchg-transition-all"><span><svg class="aifnmjmchg-w-4 aifnmjmchg-h-4 lg:aifnmjmchg-w-4 lg:aifnmjmchg-h-4 aifnmjmchg-chat_pdf_icon" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.79128 0.289062C2.90763 0.289062 2.19128 1.00541 2.19128 1.88906V2.33517C1.42585 2.45474 0.84021 3.11694 0.84021 3.91592V4.6181C0.84021 5.41709 1.42585 6.07929 2.19128 6.19886V13.4C2.19128 14.2837 2.90763 15 3.79128 15H12.6C13.4837 15 14.2 14.2837 14.2 13.4V1.88906C14.2 1.00541 13.4837 0.289062 12.6 0.289062H3.79128ZM3.39128 6.21811V13.4C3.39128 13.6209 3.57037 13.8 3.79128 13.8H12.6C12.8209 13.8 13 13.6209 13 13.4V1.88906C13 1.66815 12.8209 1.48906 12.6 1.48906H3.79128C3.57037 1.48906 3.39128 1.66815 3.39128 1.88906V2.31592H5.84458C6.72824 2.31592 7.44458 3.03226 7.44458 3.91592V4.6181C7.44458 5.50176 6.72824 6.21811 5.84458 6.21811H3.39128ZM2.04021 3.91592C2.04021 3.695 2.2193 3.51592 2.44021 3.51592H5.84458C6.0655 3.51592 6.24458 3.695 6.24458 3.91592V4.6181C6.24458 4.83902 6.0655 5.01811 5.84458 5.01811H2.44021C2.2193 5.01811 2.04021 4.83902 2.04021 4.6181V3.91592Z" fill="currentColor" fill-opacity="0.5"></path><path d="M11.2151 11.1661C10.6578 11.1247 10.1215 10.9178 9.68817 10.5452C8.84183 10.7314 8.03717 11.0006 7.23237 11.3317C6.59261 12.4699 5.99415 13.0492 5.47818 13.0492C5.37504 13.0492 5.2512 13.0284 5.1687 12.9664C4.94166 12.8629 4.81787 12.6353 4.81787 12.4078C4.81787 12.2215 4.85907 11.704 6.81975 10.8558C7.27352 10.028 7.62435 9.17948 7.91333 8.28976C7.6657 7.79314 7.12923 6.57219 7.50066 5.95153C7.62435 5.72383 7.87213 5.59969 8.14042 5.6204C8.34676 5.6204 8.55309 5.72387 8.67679 5.88942C8.94522 6.26196 8.92452 7.04815 8.5736 8.20704C8.90392 8.82784 9.3373 9.38643 9.85317 9.86254C10.2866 9.77972 10.7198 9.71756 11.1533 9.71756C12.1232 9.73822 12.2676 10.1937 12.2471 10.4624C12.2471 11.1661 11.5661 11.1661 11.2151 11.1661ZM5.43693 12.4491L5.49888 12.4281C5.78776 12.3248 6.01475 12.118 6.17989 11.8489C5.87026 11.9731 5.62262 12.1803 5.43693 12.4491ZM8.18162 6.2411H8.11957C8.09897 6.2411 8.05773 6.2411 8.03713 6.26191C7.95453 6.6136 8.01662 6.98614 8.16107 7.31722C8.28476 6.96543 8.28476 6.59284 8.18162 6.2411ZM8.32611 9.24164L8.30536 9.2831L8.28471 9.26235C8.09893 9.73817 7.89264 10.2144 7.66555 10.6694L7.70685 10.6488V10.6901C8.16107 10.5244 8.65619 10.3799 9.11031 10.2764L9.08951 10.2556H9.15146C8.84178 9.94502 8.553 9.59333 8.32611 9.24164ZM11.1326 10.3385C10.9469 10.3385 10.7819 10.3385 10.5961 10.3799C10.8024 10.4831 11.0087 10.5245 11.215 10.5453C11.3598 10.566 11.504 10.5453 11.6278 10.504C11.6278 10.4417 11.5453 10.3385 11.1326 10.3385Z" fill="currentColor"></path></svg></span></button><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999] aifnmjmchg-top-0 aifnmjmchg-left-1/2 aifnmjmchg-transform aifnmjmchg--translate-x-1/2 aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-900 dark:aifnmjmchg-text-gray-200 aifnmjmchg-translate-y-[-120%] ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[200px] aifnmjmchg-w-full">Unggah pdf</div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li><input type="file" id="imageFileInput" accept="image/jpeg,image/png" style="display: none;"></div><div id="aifnmjmchg-image-vision-modal" class="aifnmjmchg-hide"><div tabindex="-1" aria-hide="true" class="aifnmjmchg-fixed !aifnmjmchg-z-[999999] aifnmjmchg-modal aifnmjmchg-m-0 aifnmjmchg-bg-[rgba(0,0,0,.5)] aifnmjmchg-top-0 aifnmjmchg-left-0 aifnmjmchg-bottom-0 aifnmjmchg-right-0 aifnmjmchg-w-full aifnmjmchg-p-4 aifnmjmchg-overflow-x-hidden aifnmjmchg-overflow-y-auto lg:aifnmjmchg-inset-0 h-[calc(100%)] aifnmjmchg-max-h-full aifnmjmchg-justify-center aifnmjmchg-flex aifnmjmchg-w-full aifnmjmchg-items-center" data-modal-hide=""><div class="aifnmjmchg-relative aifnmjmchg-w-full lg:aifnmjmchg-max-w-screen-xl aifnmjmchg-max-h-full"><div class="aifnmjmchg-relative aifnmjmchg-bg-white aifnmjmchg-rounded-lg aifnmjmchg-shadow dark:aifnmjmchg-bg-neutral-800"><div class="aifnmjmchg-px-6 aifnmjmchg-py-4 aifnmjmchg-border-b aifnmjmchg-rounded-t dark:aifnmjmchg-border-neutral-600"><h3 class="aifnmjmchg-text-base aifnmjmchg-font-semibold aifnmjmchg-text-neutral-900 lg:aifnmjmchg-text-lg dark:aifnmjmchg-text-white aifnmjmchg-text-center">Vision</h3><button type="button" class="aifnmjmchg-absolute aifnmjmchg-top-3 aifnmjmchg-right-2.5 aifnmjmchg-text-neutral-400 aifnmjmchg-bg-transparent hover:aifnmjmchg-bg-neutral-200 hover:aifnmjmchg-text-neutral-900 aifnmjmchg-rounded-lg aifnmjmchg-text-sm aifnmjmchg-w-8 aifnmjmchg-h-8 aifnmjmchg-ml-auto aifnmjmchg-inline-flex aifnmjmchg-justify-center aifnmjmchg-items-center dark:hover:aifnmjmchg-bg-neutral-600 dark:hover:aifnmjmchg-text-white" data-modal-hide=""><svg class="aifnmjmchg-w-3 aifnmjmchg-h-3" aria-hide="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"></path></svg><span class="aifnmjmchg-sr-only">Close modal</span></button></div><div class="aifnmjmchg-p-4 aifnmjmchg-w-full aifnmjmchg-text-center aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center aifnmjmchg-gap-3"><p class="aifnmjmchg-px-4 aifnmjmchg-text-sm aifnmjmchg-text-neutral-600 dark:aifnmjmchg-text-neutral-400">Unggah gambar untuk dengan mudah mendapatkan penjelasan cerdas dan mengekstrak teks dari gambar Anda.</p><input type="file" id="imageFileInput" accept="image/jpeg,image/png" style="display: none;"><label for="imageFileInput" class="aifnmjmchg-w-full aifnmjmchg-h-full aifnmjmchg-relative aifnmjmchg-z-[9999]"><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-w-full aifnmjmchg-p-6 aifnmjmchg-items-center aifnmjmchg-justify-center aifnmjmchg-mt-4 aifnmjmchg-border-2 aifnmjmchg-border-dotted aifnmjmchg-border-neutral-300 dark:aifnmjmchg-border-neutral-700 aifnmjmchg-rounded-lg aifnmjmchg-text-neutral-600 dark:aifnmjmchg-text-neutral-400 aifnmjmchg-text-center aifnmjmchg-cursor-pointer aifnmjmchg-transition-all hover:aifnmjmchg-opacity-70"><svg class="svg-inline--fa fa-image aifnmjmchg-w-24 aifnmjmchg-h-24 aifnmjmchg-opacity-60" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="image" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M0 96C0 60.7 28.7 32 64 32l384 0c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 96zM323.8 202.5c-4.5-6.6-11.9-10.5-19.8-10.5s-15.4 3.9-19.8 10.5l-87 127.6L170.7 297c-4.6-5.7-11.5-9-18.7-9s-14.2 3.3-18.7 9l-64 80c-5.8 7.2-6.9 17.1-2.9 25.4s12.4 13.6 21.6 13.6l96 0 32 0 208 0c8.9 0 17.1-4.9 21.2-12.8s3.6-17.4-1.4-24.7l-120-176zM112 192a48 48 0 1 0 0-96 48 48 0 1 0 0 96z"></path></svg><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center aifnmjmchg-gap-1 aifnmjmchg-mt-2"><span class="aifnmjmchg-block aifnmjmchg-text-xs">Jenis gambar yang didukung adalah JPEG dan PNG.</span></div><span class="aifnmjmchg-block aifnmjmchg-mt-2 aifnmjmchg-opacity-60">Seret gambar Anda ke sini atau klik untuk mengunggah</span></div></label></div><div class="aifnmjmchg-flex aifnmjmchg-flex-row aifnmjmchg-justify-center aifnmjmchg-items-center aifnmjmchg-gap-2 aifnmjmchg-px-4"><div class="aifnmjmchg-h-[1px] aifnmjmchg-w-1/2 aifnmjmchg-bg-neutral-200 dark:aifnmjmchg-bg-neutral-600"></div><p class="aifnmjmchg-text-center aifnmjmchg-text-neutral-600 dark:aifnmjmchg-text-neutral-400 aifnmjmchg-text-lg aifnmjmchg-my-4">Atau</p><div class="aifnmjmchg-h-[1px] aifnmjmchg-w-1/2 aifnmjmchg-bg-neutral-200 dark:aifnmjmchg-bg-neutral-600"></div></div><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-px-4 aifnmjmchg-mt-2"><button class="aifnmjmchg-cursor-pointer aifnmjmchg-w-full aifnmjmchg-font-semibold aifnmjmchg-text-white aifnmjmchg-text-sm aifnmjmchg-py-2 aifnmjmchg-rounded-md aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-gap-2 aifnmjmchg-justify-center aifnmjmchg-bg-[var(--aifnmjmchg-link-color)] hover:aifnmjmchg-opacity-90 aifnmjmchg-transition-all"><svg class="svg-inline--fa fa-scissors aifnmjmchg-w-3 aifnmjmchg-h-3" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="scissors" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M256 192l-39.5-39.5c4.9-12.6 7.5-26.2 7.5-40.5C224 50.1 173.9 0 112 0S0 50.1 0 112s50.1 112 112 112c14.3 0 27.9-2.7 40.5-7.5L192 256l-39.5 39.5c-12.6-4.9-26.2-7.5-40.5-7.5C50.1 288 0 338.1 0 400s50.1 112 112 112s112-50.1 112-112c0-14.3-2.7-27.9-7.5-40.5L499.2 76.8c7.1-7.1 7.1-18.5 0-25.6c-28.3-28.3-74.1-28.3-102.4 0L256 192zm22.6 150.6L396.8 460.8c28.3 28.3 74.1 28.3 102.4 0c7.1-7.1 7.1-18.5 0-25.6L342.6 278.6l-64 64zM64 112a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm48 240a48 48 0 1 1 0 96 48 48 0 1 1 0-96z"></path></svg> Ambil tangkapan layar</button></div><div class="aifnmjmchg-h-6 aifnmjmchg-mt-4"><!----></div><!----></div></div></div></div><div id="aifnmjmchg-pdf-upload-modal" class="aifnmjmchg-hide"><div tabindex="-1" aria-hide="true" class="aifnmjmchg-fixed !aifnmjmchg-z-[999999] aifnmjmchg-modal aifnmjmchg-m-0 aifnmjmchg-bg-[rgba(0,0,0,.5)] aifnmjmchg-top-0 aifnmjmchg-left-0 aifnmjmchg-bottom-0 aifnmjmchg-right-0 aifnmjmchg-w-full aifnmjmchg-p-4 aifnmjmchg-overflow-x-hidden aifnmjmchg-overflow-y-auto lg:aifnmjmchg-inset-0 h-[calc(100%)] aifnmjmchg-max-h-full aifnmjmchg-justify-center aifnmjmchg-flex aifnmjmchg-items-center" data-modal-hide=""><div class="aifnmjmchg-relative aifnmjmchg-w-full lg:aifnmjmchg-max-w-screen-xl aifnmjmchg-max-h-full"><div class="aifnmjmchg-relative aifnmjmchg-bg-white aifnmjmchg-rounded-lg aifnmjmchg-shadow dark:aifnmjmchg-bg-neutral-800"><div class="aifnmjmchg-px-6 aifnmjmchg-py-4 aifnmjmchg-border-b aifnmjmchg-rounded-t dark:aifnmjmchg-border-neutral-600"><h3 class="aifnmjmchg-text-base aifnmjmchg-font-semibold aifnmjmchg-text-neutral-900 lg:aifnmjmchg-text-lg dark:aifnmjmchg-text-white aifnmjmchg-text-center">Unggah PDF ke Bahasa Indonesia. Berikan saya terjemahan yang tepat, tidak ada yang lain. Jangan melakukan operasi pada nomor yang mengandung tanda kutip ganda.</h3><button type="button" class="aifnmjmchg-absolute aifnmjmchg-top-3 aifnmjmchg-right-2.5 aifnmjmchg-text-neutral-400 aifnmjmchg-bg-transparent hover:aifnmjmchg-bg-neutral-200 hover:aifnmjmchg-text-neutral-900 aifnmjmchg-rounded-lg aifnmjmchg-text-sm aifnmjmchg-w-8 aifnmjmchg-h-8 aifnmjmchg-ml-auto aifnmjmchg-inline-flex aifnmjmchg-justify-center aifnmjmchg-items-center dark:hover:aifnmjmchg-bg-neutral-600 dark:hover:aifnmjmchg-text-white" data-modal-hide=""><svg class="aifnmjmchg-w-3 aifnmjmchg-h-3" aria-hide="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"></path></svg><span class="aifnmjmchg-sr-only">Close modal</span></button></div><div class="aifnmjmchg-p-4 aifnmjmchg-w-full aifnmjmchg-text-center aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center aifnmjmchg-gap-3"><p class="aifnmjmchg-px-4 aifnmjmchg-text-sm aifnmjmchg-text-neutral-600 dark:aifnmjmchg-text-neutral-400">Unggah File PDF untuk dengan mudah mendapatkan ringkasan cerdas dan jawaban untuk dokumen Anda.</p><input type="file" id="fileInputPDF" accept="application/pdf" style="display: none;"><label for="fileInputPDF" class="aifnmjmchg-w-full aifnmjmchg-h-full aifnmjmchg-relative aifnmjmchg-z-[9999]"><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-w-full aifnmjmchg-p-6 aifnmjmchg-items-center aifnmjmchg-justify-center aifnmjmchg-mt-4 aifnmjmchg-border-2 aifnmjmchg-border-dotted aifnmjmchg-border-neutral-300 dark:aifnmjmchg-border-neutral-700 aifnmjmchg-rounded-lg aifnmjmchg-text-neutral-600 dark:aifnmjmchg-text-neutral-400 aifnmjmchg-text-center aifnmjmchg-cursor-pointer aifnmjmchg-transition-all hover:aifnmjmchg-opacity-70"><span><svg class="aifnmjmchg-w-16 aifnmjmchg-h-16 aifnmjmchg-opacity-60 aifnmjmchg-pdf_icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 309.267 309.267" xml:space="preserve"><path style="fill:#e2574c" d="M38.658 0h164.23l87.049 86.711v203.227c0 10.679-8.659 19.329-19.329 19.329H38.658c-10.67 0-19.329-8.65-19.329-19.329V19.329C19.329 8.65 27.989 0 38.658 0z"></path><path style="fill:#b53629" d="M289.658 86.981h-67.372c-10.67 0-19.329-8.659-19.329-19.329V.193l86.701 86.788z"></path><path style="fill:#fff" d="M217.434 146.544c3.238 0 4.823-2.822 4.823-5.557 0-2.832-1.653-5.567-4.823-5.567h-18.44c-3.605 0-5.615 2.986-5.615 6.282v45.317c0 4.04 2.3 6.282 5.412 6.282 3.093 0 5.403-2.242 5.403-6.282v-12.438h11.153c3.46 0 5.19-2.832 5.19-5.644 0-2.754-1.73-5.49-5.19-5.49h-11.153v-16.903h13.24zm-62.327-11.124h-13.492c-3.663 0-6.263 2.513-6.263 6.243v45.395c0 4.629 3.74 6.079 6.417 6.079h14.159c16.758 0 27.824-11.027 27.824-28.047-.009-17.995-10.427-29.67-28.645-29.67zm.648 46.526h-8.225v-35.334h7.413c11.221 0 16.101 7.529 16.101 17.918 0 9.723-4.794 17.416-15.289 17.416zM106.33 135.42H92.964c-3.779 0-5.886 2.493-5.886 6.282v45.317c0 4.04 2.416 6.282 5.663 6.282s5.663-2.242 5.663-6.282v-13.231h8.379c10.341 0 18.875-7.326 18.875-19.107.001-11.529-8.233-19.261-19.328-19.261zm-.222 27.738h-7.703v-17.097h7.703c4.755 0 7.78 3.711 7.78 8.553-.01 4.833-3.025 8.544-7.78 8.544z"></path></svg></span><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center aifnmjmchg-gap-1 aifnmjmchg-mt-2"><span class="aifnmjmchg-block aifnmjmchg-text-xs">Jenis file yang didukung adalah PDF</span></div><span class="aifnmjmchg-block aifnmjmchg-mt-2 aifnmjmchg-opacity-60">Seret PDF Anda ke sini atau klik untuk mengunggah</span></div></label><!----><div class="aifnmjmchg-h-6"><!----></div></div><!----><!----></div></div></div></div></div></div><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-relative aifnmjmchg-items-end aifnmjmchg-p-1 aifnmjmchg-space-x-1 aifnmjmchg-border aifnmjmchg-rounded-xl aifnmjmchg-h-[120px]"><!----><div class="aifnmjmchg-flex aifnmjmchg-flex-wrap aifnmjmchg-gap-[6px] aifnmjmchg-max-w-full aifnmjmchg-place-self-end aifnmjmchg-self-center aifnmjmchg-min-w-[55px]"><ul class="aifnmjmchg-group-model-dropdown aifnmjmchg-hide aifnmjmchg-absolute aifnmjmchg-z-20 aifnmjmchg-width-full aifnmjmchg-w-max aifnmjmchg-min-w-[180px] aifnmjmchg-max-w-[250px] aifnmjmchg-bg-white aifnmjmchg-divide-y aifnmjmchg-divide-neutral-100 aifnmjmchg-rounded-lg aifnmjmchg-shadow dark:aifnmjmchg-bg-neutral-900 dark:aifnmjmchg-divide-neutral-700"><div class="aifnmjmchg-divide-y aifnmjmchg-divide-neutral-100 dark:aifnmjmchg-divide-neutral-700"><!----></div></ul></div><span class="aifnmjmchg-hide aifnmjmchg-my-2.5 aifnmjmchg-left-[-8px]"></span><textarea name="ask" class="aifnmjmchg-selection-container aifnmjmchg-ai-aifnmjmchgtext-item aifnmjmchg-relative aifnmjmchg-w-full aifnmjmchg-h-full aifnmjmchg-p-1 aifnmjmchg-border-0 focus:aifnmjmchg-border-0 focus:aifnmjmchg-shadow-none aifnmjmchg-outline-none aifnmjmchg-resize-none dark:aifnmjmchg-bg-neutral-700 dark:aifnmjmchg-text-neutral-200" id="ask" rows="4" placeholder="Tanyakan saya apa saja..."></textarea><button class="clear_selection"><svg xmlns="http://www.w3.org/2000/svg" title="jelas" height="14px" viewBox="0 0 384 512"><path d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"></path></svg></button><div class="aifnmjmchg-flex aifnmjmchg-w-full aifnmjmchg-justify-between aifnmjmchg-items-center aifnmjmchg-gap-2 aifnmjmchg-p-0.5"><div class="aifnmjmchg-flex aifnmjmchg-gap-1.5 aifnmjmchg-ml-1.5"><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-start aifnmjmchg-gap-3"><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><button class="aifnmjmchg-cursor-pointer aifnmjmchg-p-1 aifnmjmchg-rounded-full aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-center hover:aifnmjmchg-bg-neutral-300 dark:hover:aifnmjmchg-bg-neutral-900 aifnmjmchg-border aifnmjmchg-transition-all"><span><svg class="aifnmjmchg-w-3.5 aifnmjmchg-h-3.5 aifnmjmchg-at_icon" width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M11.03 2.31c1.014 1.048 1.36 2.47 1.36 3.688 0 1.294-.638 2.546-1.408 3.393-.388.427-.833.778-1.286.983-.445.201-.977.293-1.459.053a1 1 0 0 1-.475-.528c-.797.772-1.983 1.077-3.082.528-1.136-.568-1.424-1.846-1.347-2.948.077-1.114.535-2.308 1.21-2.983.945-.945 2.12-1.329 3.126-1.055.555.152 1.01.49 1.313.973q.073-.171.142-.326a.525.525 0 0 1 .977.38c-.26.779-.765 2.243-1.208 3.38-.129.509-.203.95-.207 1.28a1.1 1.1 0 0 0 .047.37c.092.035.26.041.53-.08.29-.132.622-.382.942-.733.644-.708 1.136-1.719 1.136-2.687 0-1.045-.3-2.168-1.066-2.958-.746-.771-2.02-1.314-4.164-1.046-1.827.228-3.242 1.494-3.944 3.13-.703 1.638-.661 3.581.357 5.108.611.917 1.893 1.64 3.475 1.855a7.17 7.17 0 0 0 4.911-1.117.525.525 0 1 1 .58.875 8.22 8.22 0 0 1-5.633 1.282c-1.778-.242-3.379-1.07-4.207-2.313C.405 8.947.382 6.621 1.202 4.71 2.023 2.797 3.72 1.235 5.981.952c2.38-.297 4.017.291 5.049 1.358M8.35 6.039v-.041c0-.937-.446-1.405-.957-1.544-.55-.15-1.354.031-2.107.784-.45.45-.84 1.377-.906 2.314-.066.951.209 1.655.77 1.936.824.412 1.826.025 2.287-.897.124-.247.282-.624.454-1.063l.017-.066c.122-.464.277-.95.443-1.423" fill="currentColor"></path></svg></span></button><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999] aifnmjmchg-top-0 aifnmjmchg-left-1/2 aifnmjmchg-transform aifnmjmchg--translate-x-1/2 aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-900 dark:aifnmjmchg-text-gray-200 aifnmjmchg-translate-y-[-120%] ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[200px] aifnmjmchg-w-full">Obrolan Grup</div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li></div><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-start aifnmjmchg-gap-3"><label class="aifnmjmchg-relative aifnmjmchg-inline-flex aifnmjmchg-items-center aifnmjmchg-cursor-pointer"><input type="checkbox" class="aifnmjmchg-ai-aifnmjmchgweb-access-checkbox aifnmjmchg-sr-only aifnmjmchg-peer" value="1"><div class="aifnmjmchg-w-7 aifnmjmchg-h-4 aifnmjmchg-bg-neutral-200 aifnmjmchg-rounded-full aifnmjmchg-peer peer-focus:aifnmjmchg-ring-3 dark:peer-focus:aifnmjmchg-ring-[var(--aifnmjmchg-link-color)] dark:aifnmjmchg-bg-neutral-700 peer-checked:after:aifnmjmchg-translate-x-full rtl:peer-checked:after:-aifnmjmchg-translate-x-full peer-checked:after:aifnmjmchg-border-white after:aifnmjmchg-content-[&#39;&#39;] after:aifnmjmchg-absolute after:aifnmjmchg-top-0.5 after:aifnmjmchg-start-[2px] after:aifnmjmchg-bg-white after:aifnmjmchg-border-neutral-300 after:aifnmjmchg-border after:aifnmjmchg-rounded-full after:aifnmjmchg-h-3 after:aifnmjmchg-w-3 after:aifnmjmchg-transition-all dark:aifnmjmchg-border-neutral-600 peer-checked:aifnmjmchg-bg-[var(--aifnmjmchg-link-color)]"></div><span class="aifnmjmchg-ms-1.5 aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-[var(--aifnmjmchg-link-color)] aifnmjmchg-opacity-60 aifnmjmchg-transition-all aifnmjmchg-select-none peer-checked:aifnmjmchg-opacity-100">Akses Web</span></label></div></div><li data-v-95af7b0c="" class="aifnmjmchg-relative aifnmjmchg-block aifnmjmchg-popper-container"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAz0lEQVR4nN3VoU7CURTH8Y9IsNAwSjDZfALGeAgak2IxWbXpE5jceIZ/hsRG+j8BFDpJosnirnO7bMY/jPNX+W3fdu++O7v3nMOxpokRhjiLkjwiZda4zeKDpvgh2bLCACeRki2LLAuVpEyJbrQkZWa4jpYkfOY7l7tIxjtKUuYDLzivIrnABG97yt7xhFbVqtro4Q6vmGNTUfZ97h4Ne+YKz1hWkPV/rZIOptFvMq7jdxV19EnxVzq+jJxdi8gpfPB98lDHZjzFTfSO92/zBcBszGtUUreMAAAAAElFTkSuQmCC" class="aifnmjmchg-w-5 aifnmjmchg-h-5 aifnmjmchg-opacity-80 aifnmjmchg-cursor-pointer dark:aifnmjmchg-invert" style=""><div data-v-95af7b0c="" class="aifnmjmchg-absolute aifnmjmchg-z-[9999999] aifnmjmchg-top-0 aifnmjmchg-left-1/2 aifnmjmchg-transform aifnmjmchg--translate-x-1/2 aifnmjmchg-py-1 aifnmjmchg-px-2 aifnmjmchg-rounded-md aifnmjmchg-shadow-lg dark:aifnmjmchg-bg-neutral-100 aifnmjmchg-bg-neutral-800 aifnmjmchg-text-gray-900 dark:aifnmjmchg-text-gray-200 aifnmjmchg-translate-y-[-120%] ait:border-[1px] dark:aifnmjmchg-border-neutral-200 aifnmjmchg-border-neutral-300" style="display: none;"><div data-v-95af7b0c="" class="aifnmjmchg-text-xs aifnmjmchg-font-medium aifnmjmchg-text-gray-200 dark:aifnmjmchg-text-gray-800 aifnmjmchg-whitespace-nowrap aifnmjmchg-max-w-[200px] aifnmjmchg-w-full">kirim</div></div><div data-v-95af7b0c="" class="aifnmjmchg-hide aifnmjmchg-left-0 aifnmjmchg-top-0 aifnmjmchg-bottom-0 aifnmjmchg-left-0 aifnmjmchg-top-1/2 aifnmjmchg-left-1/2 aifnmjmchg-right-1/2 aifnmjmchg-bottom-1/2 aifnmjmchg-translate-x-[-100%] aifnmjmchg-translate-y-[-100%] aifnmjmchg-translate-x-[-120%] aifnmjmchg-translate-y-[-120%]"></div></li></div></div></div></div></div><div class="aifnmjmchg-flex aifnmjmchg-relative aifnmjmchg-items-end aifnmjmchg-justify-between"><div class="aifnmjmchg-w-full aifnmjmchg-text-center aifnmjmchg-pr-3"><button type="button" class="aifnmjmchg-flex-col aifnmjmchg-text-[11px] aifnmjmchg-text-[var(--aifnmjmchg-master-link-color)] hover:aifnmjmchg-text-[var(--aifnmjmchg-master-link-hover-color)] dark:hover:aifnmjmchg-text-[var(--aifnmjmchg-master-link-hover-color)]">Didukung oleh AITOPIA <span><span title="5.4.0"><svg class="aifnmjmchg-w-[13px] aifnmjmchg-flex-initial aifnmjmchg-logo" xmlns="http://www.w3.org/2000/svg" baseProfile="tiny" viewBox="0 0 125 121.7" overflow="visible"><circle fill="#01a77d" cx="63.4" cy="61.2" r="57.8"></circle><g fill="#fff"><path d="M46.9 60.5h-.4c-1.9-.2-3.3-1.9-3.1-3.8.6-6.3 4.5-38 17.3-41.2 8.2-2 14.4 7.5 16.5 10.6 1.1 1.6.6 3.8-1 4.9s-3.8.6-4.9-1c-3.5-5.3-6.9-8.2-9-7.7-4.2 1-10 14.8-12 35.1-.2 1.7-1.7 3.1-3.4 3.1zm51.9-4.9c-.5 0-1-.1-1.4-.3-1.8-.8-2.6-2.9-1.8-4.6 2.6-5.8 3.2-10.2 1.7-11.7-3.1-3-17.8-.6-36.1 8.6-1.7.9-3.8.2-4.7-1.6-.9-1.7-.2-3.8 1.6-4.7.3-.2 8.3-4.1 17.4-7.1 13.4-4.5 22.2-4.5 26.7-.2 6.1 5.8 1.4 16.2-.1 19.6-.7 1.3-2 2-3.3 2zM88.2 89.5c-1.8 0-3.3-1.3-3.5-3.1-.2-1.9 1.1-3.7 3.1-3.9 6.3-.7 10.4-2.5 10.9-4.6 1-4.2-8.7-15.6-25.9-26.6-1.6-1-2.1-3.2-1.1-4.8s3.2-2.1 4.8-1.1c.3.2 7.8 5 15.1 11.3 10.7 9.3 15.3 16.7 13.9 22.8-1.9 8.2-13.2 9.5-16.9 10h-.4zm-25.9 18.1c-7.2 0-12.4-8.3-14.2-11.2-1-1.6-.5-3.8 1.1-4.8s3.8-.5 4.8 1.1c3.4 5.4 6.7 8.3 8.8 7.9 4.2-.9 10.3-14.5 12.9-34.8.2-1.9 2-3.3 3.9-3 1.9.2 3.3 2 3 3.9-.8 6.3-5.4 37.9-18.4 40.7-.5.1-1.2.2-1.9.2zm-25-18.1c-5.5 0-9.4-1.3-11.8-4-5.6-6.3-.1-16.3 1.6-19.5.9-1.7 3.1-2.3 4.7-1.4 1.7.9 2.3 3.1 1.4 4.7-3.1 5.6-4 9.9-2.6 11.5 2.9 3.2 17.7 1.9 36.7-5.7a3.57 3.57 0 0 1 4.6 1.9 3.57 3.57 0 0 1-1.9 4.6c-.3.1-8.6 3.5-17.9 5.8-5.9 1.4-10.8 2.1-14.8 2.1zm16.5-12.6c-.6 0-1.2-.2-1.8-.5-.3-.2-7.9-4.8-15.4-10.8-11-8.9-15.8-16.2-14.6-22.3 1.6-8.2 12.9-9.9 16.6-10.5 1.9-.3 3.7 1 4 2.9s-1 3.7-2.9 4c-6.3.9-10.3 2.8-10.7 4.9-1 4.3 9 15.3 26.6 25.8 1.7 1 2.2 3.1 1.2 4.8-.7 1.1-1.8 1.7-3 1.7z"></path><circle cx="63.8" cy="60.5" r="8.4"></circle></g></svg></span></span></button></div></div></div><!----><!----><!----><!----><!----><div class="aifnmjmchg-switchbar aifnmjmchg-w-[60px] aifnmjmchg-min-w-[60px] aifnmjmchg-bg-[var(--aifnmjmchg-switchbar-bg-color)] aifnmjmchg-py-2 aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center aifnmjmchg-gap-4 aifnmjmchg-h-full aifnmjmchg-flex-grow aifnmjmchg-overflow-x-hidden" style="box-shadow: none;"><div><div class="aifnmjmchg-w-8 aifnmjmchg-h-8 aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-center aifnmjmchg-rounded-lg aifnmjmchg-cursor-pointer text-[var(--aifnmjmchg-secondary-text-color)] hover:bg-[var(--aifnmjmchg-switchbar-btn-hover-bg-color)] !w-[30px] !h-[30px]"><span><svg class="aifnmjmchg-w-4.5 aifnmjmchg-h-4.5 aifnmjmchg-collapse_sidebar_icon" aria-hide="true" focusable="false" role="img" viewBox="0 0 16 16" width="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"> <path d="M6.823 7.823a.25.25 0 0 1 0 .354l-2.396 2.396A.25.25 0 0 1 4 10.396V5.604a.25.25 0 0 1 .427-.177Z"></path> <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25H9.5v-13H1.75a.25.25 0 0 0-.25.25ZM11 14.5h3.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11Z"></path> </svg></span></div></div><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-gap-2 aifnmjmchg-justify-center"><div class="aifnmjmchg-switchbar-tab-item aifnmjmchg-rounded-lg aifnmjmchg-p-2 aifnmjmchg-cursor-pointer aifnmjmchg-arc-edge aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center  active"><span><span><svg class="aifnmjmchg-w-5 aifnmjmchg-h-5 aifnmjmchg-chat_icon" viewBox="0 0 31 32" version="1.1" xmlns="http://www.w3.org/2000/svg"> <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage"> <g sketch:type="MSLayerGroup" transform="translate(-259.000000, -257.000000)" fill="currentColor"> <path d="M265.5,267 C266.329,267 267,267.672 267,268.5 C267,269.329 266.329,270 265.5,270 C264.671,270 264,269.329 264,268.5 C264,267.672 264.671,267 265.5,267 L265.5,267 Z M271.5,267 C272.329,267 273,267.672 273,268.5 C273,269.329 272.329,270 271.5,270 C270.671,270 270,269.329 270,268.5 C270,267.672 270.671,267 271.5,267 L271.5,267 Z M277.5,267 C278.329,267 279,267.672 279,268.5 C279,269.329 278.329,270 277.5,270 C276.671,270 276,269.329 276,268.5 C276,267.672 276.671,267 277.5,267 L277.5,267 Z M268.637,279.736 C269.414,279.863 271.181,280 272,280 C279.18,280 284,274.657 284,268.375 C284,262.093 277.977,257 272,257 C264.811,257 259,262.093 259,268.375 C259,272.015 260.387,275.104 263,277.329 L263,283 L268.637,279.736 L268.637,279.736 Z M285.949,266.139 L286,267 C286.008,267.817 286,267.742 286,268.5 C286,276.475 279.716,282 271,282 L268,282 C270.38,284.328 273.149,285.75 277,285.75 C277.819,285.75 278.618,285.676 279.395,285.549 L285,289 L285,283.329 C288.04,281.246 290,278.015 290,274.375 C290,271.131 288.439,268.211 285.949,266.139 L285.949,266.139 Z" id="comments" sketch:type="MSShapeGroup"></path> </g> </g> </svg></span></span><span class="aifnmjmchg-pt-2 aifnmjmchg-text-[10px]">Obrolan</span></div><div class="aifnmjmchg-switchbar-tab-item aifnmjmchg-rounded-lg aifnmjmchg-p-2 aifnmjmchg-cursor-pointer aifnmjmchg-arc-edge aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center"><span><span><svg class="aifnmjmchg-w-5 aifnmjmchg-h-5 aifnmjmchg-ask_icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256"><rect width="256" height="256" fill="none"></rect><path fill="currentColor" d="M225.86,102.82c-3.77-3.94-7.67-8-9.14-11.57-1.36-3.27-1.44-8.69-1.52-13.94-.15-9.76-.31-20.82-8-28.51s-18.75-7.85-28.51-8c-5.25-.08-10.67-.16-13.94-1.52-3.56-1.47-7.63-5.37-11.57-9.14C146.28,23.51,138.44,16,128,16s-18.27,7.51-25.18,14.14c-3.94,3.77-8,7.67-11.57,9.14C88,40.64,82.56,40.72,77.31,40.8c-9.76.15-20.82.31-28.51,8S41,67.55,40.8,77.31c-.08,5.25-.16,10.67-1.52,13.94-1.47,3.56-5.37,7.63-9.14,11.57C23.51,109.72,16,117.56,16,128s7.51,18.27,14.14,25.18c3.77,3.94,7.67,8,9.14,11.57,1.36,3.27,1.44,8.69,1.52,13.94.15,9.76.31,20.82,8,28.51s18.75,7.85,28.51,8c5.25.08,10.67.16,13.94,1.52,3.56,1.47,7.63,5.37,11.57,9.14C109.72,232.49,117.56,240,128,240s18.27-7.51,25.18-14.14c3.94-3.77,8-7.67,11.57-9.14,3.27-1.36,8.69-1.44,13.94-1.52,9.76-.15,20.82-.31,28.51-8s7.85-18.75,8-28.51c.08-5.25.16-10.67,1.52-13.94,1.47-3.56,5.37-7.63,9.14-11.57C232.49,146.28,240,138.44,240,128S232.49,109.73,225.86,102.82ZM128,192a12,12,0,1,1,12-12A12,12,0,0,1,128,192Zm8-48.72V144a8,8,0,0,1-16,0v-8a8,8,0,0,1,8-8c13.23,0,24-9,24-20s-10.77-20-24-20-24,9-24,20v4a8,8,0,0,1-16,0v-4c0-19.85,17.94-36,40-36s40,16.15,40,36C168,125.38,154.24,139.93,136,143.28Z"></path></svg></span></span><span class="aifnmjmchg-pt-2 aifnmjmchg-text-[10px]">Bertanya</span></div><div class="aifnmjmchg-switchbar-tab-item aifnmjmchg-rounded-lg aifnmjmchg-p-2 aifnmjmchg-cursor-pointer aifnmjmchg-arc-edge aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center"><span><svg class="svg-inline--fa fa-magnifying-glass aifnmjmchg-h-5 aifnmjmchg-w-5" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="magnifying-glass" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376c-34.4 25.2-76.8 40-122.7 40C93.1 416 0 322.9 0 208S93.1 0 208 0S416 93.1 416 208zM208 352a144 144 0 1 0 0-288 144 144 0 1 0 0 288z"></path></svg></span><span class="aifnmjmchg-pt-2 aifnmjmchg-text-[10px]">Cari</span></div><div class="aifnmjmchg-switchbar-tab-item aifnmjmchg-rounded-lg aifnmjmchg-p-2 aifnmjmchg-cursor-pointer aifnmjmchg-arc-edge aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center"><span><svg class="svg-inline--fa fa-square-pen aifnmjmchg-h-5 aifnmjmchg-w-5" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="square-pen" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path class="" fill="currentColor" d="M64 32C28.7 32 0 60.7 0 96L0 416c0 35.3 28.7 64 64 64l320 0c35.3 0 64-28.7 64-64l0-320c0-35.3-28.7-64-64-64L64 32zM325.8 139.7l14.4 14.4c15.6 15.6 15.6 40.9 0 56.6l-21.4 21.4-71-71 21.4-21.4c15.6-15.6 40.9-15.6 56.6 0zM119.9 289L225.1 183.8l71 71L190.9 359.9c-4.1 4.1-9.2 7-14.9 8.4l-60.1 15c-5.5 1.4-11.2-.2-15.2-4.2s-5.6-9.7-4.2-15.2l15-60.1c1.4-5.6 4.3-10.8 8.4-14.9z"></path></svg></span><span class="aifnmjmchg-pt-2 aifnmjmchg-text-[10px]">Tulis</span></div><div class="aifnmjmchg-switchbar-tab-item aifnmjmchg-rounded-lg aifnmjmchg-p-2 aifnmjmchg-cursor-pointer aifnmjmchg-arc-edge aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center"><span><svg class="svg-inline--fa fa-image aifnmjmchg-h-5 aifnmjmchg-w-5" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="image" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M0 96C0 60.7 28.7 32 64 32l384 0c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 96zM323.8 202.5c-4.5-6.6-11.9-10.5-19.8-10.5s-15.4 3.9-19.8 10.5l-87 127.6L170.7 297c-4.6-5.7-11.5-9-18.7-9s-14.2 3.3-18.7 9l-64 80c-5.8 7.2-6.9 17.1-2.9 25.4s12.4 13.6 21.6 13.6l96 0 32 0 208 0c8.9 0 17.1-4.9 21.2-12.8s3.6-17.4-1.4-24.7l-120-176zM112 192a48 48 0 1 0 0-96 48 48 0 1 0 0 96z"></path></svg></span><span class="aifnmjmchg-pt-2 aifnmjmchg-text-[10px]">Gambar</span></div><div class="aifnmjmchg-switchbar-tab-item aifnmjmchg-rounded-lg aifnmjmchg-p-2 aifnmjmchg-cursor-pointer aifnmjmchg-arc-edge aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center" data-aifnmjmchg-dropdown-toggle="aifnmjmchg-pdf-upload-modal"><span><svg class="aifnmjmchg-w-5 aifnmjmchg-h-5 aifnmjmchg-chat_pdf_icon" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.79128 0.289062C2.90763 0.289062 2.19128 1.00541 2.19128 1.88906V2.33517C1.42585 2.45474 0.84021 3.11694 0.84021 3.91592V4.6181C0.84021 5.41709 1.42585 6.07929 2.19128 6.19886V13.4C2.19128 14.2837 2.90763 15 3.79128 15H12.6C13.4837 15 14.2 14.2837 14.2 13.4V1.88906C14.2 1.00541 13.4837 0.289062 12.6 0.289062H3.79128ZM3.39128 6.21811V13.4C3.39128 13.6209 3.57037 13.8 3.79128 13.8H12.6C12.8209 13.8 13 13.6209 13 13.4V1.88906C13 1.66815 12.8209 1.48906 12.6 1.48906H3.79128C3.57037 1.48906 3.39128 1.66815 3.39128 1.88906V2.31592H5.84458C6.72824 2.31592 7.44458 3.03226 7.44458 3.91592V4.6181C7.44458 5.50176 6.72824 6.21811 5.84458 6.21811H3.39128ZM2.04021 3.91592C2.04021 3.695 2.2193 3.51592 2.44021 3.51592H5.84458C6.0655 3.51592 6.24458 3.695 6.24458 3.91592V4.6181C6.24458 4.83902 6.0655 5.01811 5.84458 5.01811H2.44021C2.2193 5.01811 2.04021 4.83902 2.04021 4.6181V3.91592Z" fill="currentColor" fill-opacity="0.5"></path><path d="M11.2151 11.1661C10.6578 11.1247 10.1215 10.9178 9.68817 10.5452C8.84183 10.7314 8.03717 11.0006 7.23237 11.3317C6.59261 12.4699 5.99415 13.0492 5.47818 13.0492C5.37504 13.0492 5.2512 13.0284 5.1687 12.9664C4.94166 12.8629 4.81787 12.6353 4.81787 12.4078C4.81787 12.2215 4.85907 11.704 6.81975 10.8558C7.27352 10.028 7.62435 9.17948 7.91333 8.28976C7.6657 7.79314 7.12923 6.57219 7.50066 5.95153C7.62435 5.72383 7.87213 5.59969 8.14042 5.6204C8.34676 5.6204 8.55309 5.72387 8.67679 5.88942C8.94522 6.26196 8.92452 7.04815 8.5736 8.20704C8.90392 8.82784 9.3373 9.38643 9.85317 9.86254C10.2866 9.77972 10.7198 9.71756 11.1533 9.71756C12.1232 9.73822 12.2676 10.1937 12.2471 10.4624C12.2471 11.1661 11.5661 11.1661 11.2151 11.1661ZM5.43693 12.4491L5.49888 12.4281C5.78776 12.3248 6.01475 12.118 6.17989 11.8489C5.87026 11.9731 5.62262 12.1803 5.43693 12.4491ZM8.18162 6.2411H8.11957C8.09897 6.2411 8.05773 6.2411 8.03713 6.26191C7.95453 6.6136 8.01662 6.98614 8.16107 7.31722C8.28476 6.96543 8.28476 6.59284 8.18162 6.2411ZM8.32611 9.24164L8.30536 9.2831L8.28471 9.26235C8.09893 9.73817 7.89264 10.2144 7.66555 10.6694L7.70685 10.6488V10.6901C8.16107 10.5244 8.65619 10.3799 9.11031 10.2764L9.08951 10.2556H9.15146C8.84178 9.94502 8.553 9.59333 8.32611 9.24164ZM11.1326 10.3385C10.9469 10.3385 10.7819 10.3385 10.5961 10.3799C10.8024 10.4831 11.0087 10.5245 11.215 10.5453C11.3598 10.566 11.504 10.5453 11.6278 10.504C11.6278 10.4417 11.5453 10.3385 11.1326 10.3385Z" fill="currentColor"></path></svg></span><span class="aifnmjmchg-pt-2 aifnmjmchg-text-[10px]">ChatPDF</span></div><div class="aifnmjmchg-switchbar-tab-item aifnmjmchg-rounded-lg aifnmjmchg-p-2 aifnmjmchg-cursor-pointer aifnmjmchg-arc-edge aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center" data-aifnmjmchg-dropdown-toggle="aifnmjmchg-image-vision-modal"><span><svg class="svg-inline--fa fa-eye aifnmjmchg-h-5 aifnmjmchg-w-5" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="eye" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path class="" fill="currentColor" d="M288 32c-80.8 0-145.5 36.8-192.6 80.6C48.6 156 17.3 208 2.5 243.7c-3.3 7.9-3.3 16.7 0 24.6C17.3 304 48.6 356 95.4 399.4C142.5 443.2 207.2 480 288 480s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C433.5 68.8 368.8 32 288 32zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64c-7.1 0-13.9-1.2-20.3-3.3c-5.5-1.8-11.9 1.6-11.7 7.4c.3 6.9 1.3 13.8 3.2 20.7c13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3z"></path></svg></span><span class="aifnmjmchg-pt-2 aifnmjmchg-text-[10px]">Visi</span></div></div><div class="divider w-[70%] aifnmjmchg-mx-auto h-[1px] bg-[var(--aifnmjmchg-switchbar-btn-hover-bg-color)]"></div><div class="bottom-area aifnmjmchg-mt-auto aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-justify-center aifnmjmchg-items-center aifnmjmchg-gap-2 aifnmjmchg-mb-4"><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-w-full aifnmjmchg-gap-1 aifnmjmchg-cursor-pointer"><div class="aifnmjmchg-switchbar-tab-item aifnmjmchg-rounded-lg aifnmjmchg-p-1 aifnmjmchg-cursor-pointer aifnmjmchg-items-center aifnmjmchg-flex aifnmjmchg-flex-col"><span><svg class="aifnmjmchg-w-4 aifnmjmchg-h-4 aifnmjmchg-full_screen_icon" style="width: 1em; height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M237.248 192H352a32 32 0 1 0 0-64H160a32 32 0 0 0-32 32v192a32 32 0 1 0 64 0v-114.752l137.36 137.36a32 32 0 1 0 45.232-45.264L237.248 192zM832 237.248V352a32 32 0 1 0 64 0V160a32 32 0 0 0-32-32H672a32 32 0 1 0 0 64h114.752l-137.36 137.36a32 32 0 1 0 45.264 45.232L832 237.248zM237.248 832H352a32 32 0 1 1 0 64H160a32 32 0 0 1-32-32V672a32 32 0 1 1 64 0v114.752l137.36-137.36a32 32 0 1 1 45.232 45.264L237.248 832zM832 786.752V672a32 32 0 1 1 64 0v192a32 32 0 0 1-32 32H672a32 32 0 1 1 0-64h114.752l-137.36-137.36a32 32 0 1 1 45.264-45.232L832 786.752z"></path></svg></span><label class="aifnmjmchg-cursor-pointer" style="font-size: 8px;">Halaman Penuh</label></div></div><!----><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-gap-1 aifnmjmchg-w-full aifnmjmchg-cursor-pointer"><div class="aifnmjmchg-switchbar-tab-item aifnmjmchg-rounded-lg aifnmjmchg-p-1 aifnmjmchg-cursor-pointer aifnmjmchg-items-center aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-min-h-[36px] aifnmjmchg-justify-center"><svg class="svg-inline--fa fa-envelope aifnmjmchg-h-4 aifnmjmchg-w-4 aifnmjmchg-contact" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="envelope" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M48 64C21.5 64 0 85.5 0 112c0 15.1 7.1 29.3 19.2 38.4L236.8 313.6c11.4 8.5 27 8.5 38.4 0L492.8 150.4c12.1-9.1 19.2-23.3 19.2-38.4c0-26.5-21.5-48-48-48L48 64zM0 176L0 384c0 35.3 28.7 64 64 64l384 0c35.3 0 64-28.7 64-64l0-208L294.4 339.2c-22.8 17.1-54 17.1-76.8 0L0 176z"></path></svg></div></div><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-gap-1 aifnmjmchg-w-full aifnmjmchg-cursor-pointer"><div class="aifnmjmchg-switchbar-tab-item aifnmjmchg-rounded-lg aifnmjmchg-p-1 aifnmjmchg-cursor-pointer aifnmjmchg-items-center aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-min-h-[36px] aifnmjmchg-justify-center aifnmjmchg-options"><svg class="svg-inline--fa fa-gear aifnmjmchg-h-4 aifnmjmchg-w-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="gear" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M495.9 166.6c3.2 8.7 .5 18.4-6.4 24.6l-43.3 39.4c1.1 8.3 1.7 16.8 1.7 25.4s-.6 17.1-1.7 25.4l43.3 39.4c6.9 6.2 9.6 15.9 6.4 24.6c-4.4 11.9-9.7 23.3-15.8 34.3l-4.7 8.1c-6.6 11-14 21.4-22.1 31.2c-5.9 7.2-15.7 9.6-24.5 6.8l-55.7-17.7c-13.4 10.3-28.2 18.9-44 25.4l-12.5 57.1c-2 9.1-9 16.3-18.2 17.8c-13.8 2.3-28 3.5-42.5 3.5s-28.7-1.2-42.5-3.5c-9.2-1.5-16.2-8.7-18.2-17.8l-12.5-57.1c-15.8-6.5-30.6-15.1-44-25.4L83.1 425.9c-8.8 2.8-18.6 .3-24.5-6.8c-8.1-9.8-15.5-20.2-22.1-31.2l-4.7-8.1c-6.1-11-11.4-22.4-15.8-34.3c-3.2-8.7-.5-18.4 6.4-24.6l43.3-39.4C64.6 273.1 64 264.6 64 256s.6-17.1 1.7-25.4L22.4 191.2c-6.9-6.2-9.6-15.9-6.4-24.6c4.4-11.9 9.7-23.3 15.8-34.3l4.7-8.1c6.6-11 14-21.4 22.1-31.2c5.9-7.2 15.7-9.6 24.5-6.8l55.7 17.7c13.4-10.3 28.2-18.9 44-25.4l12.5-57.1c2-9.1 9-16.3 18.2-17.8C227.3 1.2 241.5 0 256 0s28.7 1.2 42.5 3.5c9.2 1.5 16.2 8.7 18.2 17.8l12.5 57.1c15.8 6.5 30.6 15.1 44 25.4l55.7-17.7c8.8-2.8 18.6-.3 24.5 6.8c8.1 9.8 15.5 20.2 22.1 31.2l4.7 8.1c6.1 11 11.4 22.4 15.8 34.3zM256 336a80 80 0 1 0 0-160 80 80 0 1 0 0 160z"></path></svg></div></div><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-gap-1 aifnmjmchg-w-full aifnmjmchg-cursor-pointer"><div data-aifnmjmchg-dropdown-toggle="aifnmjmchg-user-dropdown" data-placement="top-end" class="aifnmjmchg-switchbar-tab-item aifnmjmchg-rounded-lg aifnmjmchg-p-1 aifnmjmchg-cursor-pointer aifnmjmchg-items-center aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-min-h-[36px] aifnmjmchg-justify-center"><svg class="svg-inline--fa fa-user aifnmjmchg-h-4 aifnmjmchg-w-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="user" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path class="" fill="currentColor" d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512l388.6 0c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304l-91.4 0z"></path></svg></div></div></div></div><div id="aifnmjmchg-user-dropdown" class="aifnmjmchg-stroke aifnmjmchg-z-20 aifnmjmchg-width-full aifnmjmchg-hide aifnmjmchg-w-max aifnmjmchg-min-w-[180px] aifnmjmchg-max-w-[250px] aifnmjmchg-bg-white aifnmjmchg-divide-y aifnmjmchg-divide-neutral-100 aifnmjmchg-rounded-lg aifnmjmchg-shadow dark:aifnmjmchg-bg-neutral-900 dark:aifnmjmchg-divide-neutral-700"><div class="aifnmjmchg-p-2 aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-gap-2 aifnmjmchg-min-w-[240px]"><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-cursor-pointer aifnmjmchg-rounded-lg aifnmjmchg-text-white aifnmjmchg-bg-green-700 hover:aifnmjmchg-opacity-90 aifnmjmchg-px-3 aifnmjmchg-py-1 aifnmjmchg-text-center dark:aifnmjmchg-bg-green-600 dark:hover:aifnmjmchg-bg-green-700"><div class="aifnmjmchg-flex aifnmjmchg-cursor-pointer aifnmjmchg-h-8 aifnmjmchg-w-8 aifnmjmchg-flex-center aifnmjmchg-justify-center aifnmjmchg-items-center"><div class="aifnmjmchg-relative aifnmjmchg-flex-shrink-0"><svg class="svg-inline--fa fa-user aifnmjmchg-h-4 aifnmjmchg-w-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="user" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path class="" fill="currentColor" d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512l388.6 0c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304l-91.4 0z"></path></svg></div></div><div class="aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-ml-1 aifnmjmchg-login-prefix"><div class="aifnmjmchg-flex aifnmjmchg-items-center"><div class="aifnmjmchg-text-sm aifnmjmchg-leading-5 aifnmjmchg-truncate aifnmjmchg-w-full aifnmjmchg-text-white aifnmjmchg-login-prefix">Masuk sebagai pengguna</div></div><!----></div></div><div><!----><!----><!----><div class="aifnmjmchg-flex aifnmjmchg-flex-align aifnmjmchg-gap-3 hover:aifnmjmchg-bg-[var(--aifnmjmchg-tab-menu-active-bg-color)] aifnmjmchg-rounded-lg aifnmjmchg-py-2 aifnmjmchg-px-3 aifnmjmchg-cursor-pointer aifnmjmchg-contact"><div class="aifnmjmchg-size-[16px] aifnmjmchg-flex-center aifnmjmchg-items-center"><svg class="svg-inline--fa fa-envelope aifnmjmchg-h-4 aifnmjmchg-w-4" aria-hidden="true" focusable="false" data-prefix="far" data-icon="envelope" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M64 112c-8.8 0-16 7.2-16 16l0 22.1L220.5 291.7c20.7 17 50.4 17 71.1 0L464 150.1l0-22.1c0-8.8-7.2-16-16-16L64 112zM48 212.2L48 384c0 8.8 7.2 16 16 16l384 0c8.8 0 16-7.2 16-16l0-171.8L322 328.8c-38.4 31.5-93.7 31.5-132 0L48 212.2zM0 128C0 92.7 28.7 64 64 64l384 0c35.3 0 64 28.7 64 64l0 256c0 35.3-28.7 64-64 64L64 448c-35.3 0-64-28.7-64-64L0 128z"></path></svg></div><div>Umpan balik</div></div><!----><!----></div></div></div></div><div><!----></div><div id="aifnmjmchg-invite-friends" class="aifnmjmchg-hide"><div tabindex="-1" aria-hide="true" class="aifnmjmchg-fixed !aifnmjmchg-z-[999999] aifnmjmchg-modal aifnmjmchg-m-0 aifnmjmchg-bg-[rgba(0,0,0,.5)] aifnmjmchg-top-0 aifnmjmchg-left-0 aifnmjmchg-bottom-0 aifnmjmchg-right-0 aifnmjmchg-w-full aifnmjmchg-p-4 aifnmjmchg-overflow-x-hidden aifnmjmchg-overflow-y-auto lg:aifnmjmchg-inset-0 h-[calc(100%)] aifnmjmchg-max-h-full aifnmjmchg-justify-center aifnmjmchg-flex aifnmjmchg-items-center" data-modal-hide=""><div class="aifnmjmchg-relative aifnmjmchg-w-full lg:aifnmjmchg-max-w-screen-xl aifnmjmchg-max-h-full"><div class="aifnmjmchg-relative aifnmjmchg-bg-white aifnmjmchg-rounded-lg aifnmjmchg-shadow dark:aifnmjmchg-bg-neutral-800"><div class="aifnmjmchg-px-6 aifnmjmchg-py-4 aifnmjmchg-border-b aifnmjmchg-rounded-t dark:aifnmjmchg-border-neutral-600"><h3 class="aifnmjmchg-text-base aifnmjmchg-font-semibold aifnmjmchg-text-neutral-900 lg:aifnmjmchg-text-lg dark:aifnmjmchg-text-white aifnmjmchg-text-center">Undang Teman &amp; Dapatkan Kredit</h3><button type="button" class="aifnmjmchg-absolute aifnmjmchg-top-3 aifnmjmchg-right-2.5 aifnmjmchg-text-neutral-400 aifnmjmchg-bg-transparent hover:aifnmjmchg-bg-neutral-200 hover:aifnmjmchg-text-neutral-900 aifnmjmchg-rounded-lg aifnmjmchg-text-sm aifnmjmchg-w-8 aifnmjmchg-h-8 aifnmjmchg-ml-auto aifnmjmchg-inline-flex aifnmjmchg-justify-center aifnmjmchg-items-center dark:hover:aifnmjmchg-bg-neutral-600 dark:hover:aifnmjmchg-text-white" data-modal-hide=""><svg class="aifnmjmchg-w-3 aifnmjmchg-h-3" aria-hide="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"></path></svg><span class="aifnmjmchg-sr-only">Close modal</span></button></div><div class="aifnmjmchg-p-4 aifnmjmchg-w-full aifnmjmchg-text-center aifnmjmchg-flex aifnmjmchg-flex-col aifnmjmchg-items-center aifnmjmchg-gap-3"><div class="aifnmjmchg-w-full aifnmjmchg-text-start aifnmjmchg-p-[10px]"><span>Dapatkan <span class="\&quot;text-primary-600" font-bold\"="">5 Kredit Cepat &amp; 1 Kredit Lanjut</span> untuk Anda dan teman Anda.</span><span class="aifnmjmchg-font-bold">Dapatkan lebih banyak ketika Anda merujuk lebih banyak!</span><div class="aifnmjmchg-w-full aifnmjmchg-px-[40px] aifnmjmchg-my-[30px]"><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-gap-[12px]"><svg width="20" height="22" viewBox="0 0 43 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M22.8423 3.0436C24.885 1.06876 27.6211 -0.0242977 30.4616 0.000409932C33.302 0.0251175 36.0188 1.1656 38.0268 3.17566C40.0348 5.18565 41.1735 7.90432 41.1981 10.746C41.2228 13.5877 40.1315 16.3257 38.1588 18.3703L38.1371 18.3928L32.7165 23.8185C32.7164 23.8186 32.7165 23.8184 32.7165 23.8185C31.6186 24.9178 30.297 25.7683 28.8418 26.3117C27.3864 26.8551 25.8313 27.0789 24.2819 26.9678C22.7324 26.8568 21.2251 26.4134 19.862 25.668C18.499 24.9225 17.3122 23.8924 16.382 22.6477C15.7881 21.8528 15.9509 20.7269 16.7458 20.133C17.5407 19.539 18.6665 19.7019 19.2605 20.4967C19.8823 21.3288 20.6755 22.0172 21.5862 22.5153C22.4969 23.0133 23.5039 23.3095 24.5388 23.3837C25.5737 23.4579 26.6125 23.3084 27.5848 22.9454C28.557 22.5823 29.44 22.0142 30.1738 21.2793L35.5831 15.8647C36.8952 14.4992 37.6214 12.673 37.6049 10.7772C37.5884 8.87653 36.8268 7.05875 35.4847 5.71527C34.1426 4.37185 32.3275 3.61014 30.4303 3.59364C28.5373 3.57717 26.713 4.304 25.3488 5.61846L22.2507 8.70169C21.5473 9.40164 20.4098 9.3989 19.7098 8.69556C19.0098 7.99222 19.0126 6.85462 19.7159 6.15467L22.8423 3.0436ZM14.0283 13.2153C15.4836 12.6719 17.0388 12.4481 18.5882 12.5592C20.1376 12.6703 21.645 13.1136 23.008 13.8591C24.3711 14.6045 25.5579 15.6346 26.488 16.8793C27.082 17.6742 26.9191 18.8001 26.1243 19.3941C25.3294 19.988 24.2035 19.8252 23.6095 19.0303C22.9878 18.1982 22.1946 17.5098 21.2838 17.0117C20.3731 16.5137 19.3662 16.2176 18.3312 16.1434C17.2963 16.0692 16.2575 16.2186 15.2853 16.5817C14.3131 16.9447 13.43 17.5129 12.6962 18.2477L7.28698 23.6624C5.97482 25.0279 5.24869 26.8541 5.26515 28.7498C5.28165 30.6505 6.04327 32.4683 7.3854 33.8118C8.72747 35.1552 10.5426 35.9169 12.4397 35.9334C14.3319 35.9499 16.1554 35.2237 17.5195 33.9103L20.5976 30.829C21.2989 30.127 22.4365 30.1265 23.1385 30.8278C23.8405 31.5291 23.8411 32.6667 23.1398 33.3687L20.0279 36.4836C17.9853 38.4585 15.2489 39.5513 12.4085 39.5266C9.56802 39.5019 6.85126 38.3614 4.84322 36.3514C2.83525 34.3414 1.69659 31.6227 1.67192 28.781C1.64725 25.9393 2.73854 23.2013 4.7113 21.1567L4.73298 21.1342L10.1536 15.7085C10.1537 15.7085 10.1535 15.7086 10.1536 15.7085C11.2515 14.6092 12.573 13.7587 14.0283 13.2153Z" fill="white"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M22.8423 3.0436C24.885 1.06876 27.6211 -0.0242977 30.4616 0.000409932C33.302 0.0251175 36.0188 1.1656 38.0268 3.17566C40.0348 5.18565 41.1735 7.90432 41.1981 10.746C41.2228 13.5877 40.1315 16.3257 38.1588 18.3703L38.1371 18.3928L32.7165 23.8185C32.7164 23.8186 32.7165 23.8184 32.7165 23.8185C31.6186 24.9178 30.297 25.7683 28.8418 26.3117C27.3864 26.8551 25.8313 27.0789 24.2819 26.9678C22.7324 26.8568 21.2251 26.4134 19.862 25.668C18.499 24.9225 17.3122 23.8924 16.382 22.6477C15.7881 21.8528 15.9509 20.7269 16.7458 20.133C17.5407 19.539 18.6665 19.7019 19.2605 20.4967C19.8823 21.3288 20.6755 22.0172 21.5862 22.5153C22.4969 23.0133 23.5039 23.3095 24.5388 23.3837C25.5737 23.4579 26.6125 23.3084 27.5848 22.9454C28.557 22.5823 29.44 22.0142 30.1738 21.2793L35.5831 15.8647C36.8952 14.4992 37.6214 12.673 37.6049 10.7772C37.5884 8.87653 36.8268 7.05875 35.4847 5.71527C34.1426 4.37185 32.3275 3.61014 30.4303 3.59364C28.5373 3.57717 26.713 4.304 25.3488 5.61846L22.2507 8.70169C21.5473 9.40164 20.4098 9.3989 19.7098 8.69556C19.0098 7.99222 19.0126 6.85462 19.7159 6.15467L22.8423 3.0436ZM14.0283 13.2153C15.4836 12.6719 17.0388 12.4481 18.5882 12.5592C20.1376 12.6703 21.645 13.1136 23.008 13.8591C24.3711 14.6045 25.5579 15.6346 26.488 16.8793C27.082 17.6742 26.9191 18.8001 26.1243 19.3941C25.3294 19.988 24.2035 19.8252 23.6095 19.0303C22.9878 18.1982 22.1946 17.5098 21.2838 17.0117C20.3731 16.5137 19.3662 16.2176 18.3312 16.1434C17.2963 16.0692 16.2575 16.2186 15.2853 16.5817C14.3131 16.9447 13.43 17.5129 12.6962 18.2477L7.28698 23.6624C5.97482 25.0279 5.24869 26.8541 5.26515 28.7498C5.28165 30.6505 6.04327 32.4683 7.3854 33.8118C8.72747 35.1552 10.5426 35.9169 12.4397 35.9334C14.3319 35.9499 16.1554 35.2237 17.5195 33.9103L20.5976 30.829C21.2989 30.127 22.4365 30.1265 23.1385 30.8278C23.8405 31.5291 23.8411 32.6667 23.1398 33.3687L20.0279 36.4836C17.9853 38.4585 15.2489 39.5513 12.4085 39.5266C9.56802 39.5019 6.85126 38.3614 4.84322 36.3514C2.83525 34.3414 1.69659 31.6227 1.67192 28.781C1.64725 25.9393 2.73854 23.2013 4.7113 21.1567L4.73298 21.1342L10.1536 15.7085C10.1537 15.7085 10.1535 15.7086 10.1536 15.7085C11.2515 14.6092 12.573 13.7587 14.0283 13.2153Z" fill="url(#paint0_linear_18047_3202)"></path><defs><lineargradient id="paint0_linear_18047_3202" x1="10.1416" y1="17.5048" x2="25.9524" y2="40.0917" gradientUnits="userSpaceOnUse"><stop stop-color="rgba(1, 167, 125, .9)"></stop><stop offset="1" stop-color="#60a5fa"></stop></lineargradient></defs></svg><span class="aifnmjmchg-text-[14px]">Undang teman Anda dengan tautan undangan</span></div><svg class="svg-inline--fa fa-arrow-down aifnmjmchg-w-[11px] aifnmjmchg-mx-[4px] aifnmjmchg-mt-[4px] aifnmjmchg-mb-[10px]" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-down" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path class="" fill="currentColor" d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"></path></svg><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-gap-[12px]"><svg width="18" height="19" viewBox="0 0 38 39" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M11.8795 10.3401C11.8795 6.79968 14.7411 3.84276 18.3761 3.84276C22.011 3.84276 24.8727 6.79968 24.8727 10.3401C24.8727 13.8804 22.011 16.8374 18.3761 16.8374C18.1848 16.8374 18.0003 16.8673 17.8267 16.9229C15.64 17.0126 13.4838 17.502 11.4584 18.3704C9.20642 19.336 7.16019 20.7513 5.43658 22.5354C3.71298 24.3196 2.34573 26.4377 1.41292 28.7689C0.480111 31.1 0 33.5985 0 36.1217C0 37.1828 0.831034 38.043 1.85617 38.043H35.2672C36.2923 38.043 37.1233 37.1828 37.1233 36.1217C37.1233 33.5985 36.6432 31.1 35.7104 28.7689C34.7776 26.4377 33.4104 24.3196 31.6867 22.5354C30.9619 21.7851 29.7866 21.7851 29.0617 22.5354C28.3368 23.2858 28.3368 24.5023 29.0617 25.2527C30.4406 26.68 31.5344 28.3745 32.2807 30.2394C32.7889 31.5096 33.1292 32.8419 33.2945 34.2003L3.8288 34.2003C3.99413 32.8419 4.3344 31.5096 4.84267 30.2394C5.58892 28.3745 6.68271 26.68 8.0616 25.2527C9.44049 23.8254 11.0775 22.6931 12.8791 21.9207C14.6807 21.1482 16.6116 20.7506 18.5617 20.7506C18.7692 20.7506 18.9688 20.7154 19.1551 20.6503C24.3899 20.2483 28.585 15.8289 28.585 10.3401C28.585 4.58142 23.9673 0 18.3761 0C12.7848 0 8.16717 4.58142 8.16717 10.3401C8.16717 11.4012 8.9982 12.2614 10.0233 12.2614C11.0485 12.2614 11.8795 11.4012 11.8795 10.3401Z" fill="white"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M11.8795 10.3401C11.8795 6.79968 14.7411 3.84276 18.3761 3.84276C22.011 3.84276 24.8727 6.79968 24.8727 10.3401C24.8727 13.8804 22.011 16.8374 18.3761 16.8374C18.1848 16.8374 18.0003 16.8673 17.8267 16.9229C15.64 17.0126 13.4838 17.502 11.4584 18.3704C9.20642 19.336 7.16019 20.7513 5.43658 22.5354C3.71298 24.3196 2.34573 26.4377 1.41292 28.7689C0.480111 31.1 0 33.5985 0 36.1217C0 37.1828 0.831034 38.043 1.85617 38.043H35.2672C36.2923 38.043 37.1233 37.1828 37.1233 36.1217C37.1233 33.5985 36.6432 31.1 35.7104 28.7689C34.7776 26.4377 33.4104 24.3196 31.6867 22.5354C30.9619 21.7851 29.7866 21.7851 29.0617 22.5354C28.3368 23.2858 28.3368 24.5023 29.0617 25.2527C30.4406 26.68 31.5344 28.3745 32.2807 30.2394C32.7889 31.5096 33.1292 32.8419 33.2945 34.2003L3.8288 34.2003C3.99413 32.8419 4.3344 31.5096 4.84267 30.2394C5.58892 28.3745 6.68271 26.68 8.0616 25.2527C9.44049 23.8254 11.0775 22.6931 12.8791 21.9207C14.6807 21.1482 16.6116 20.7506 18.5617 20.7506C18.7692 20.7506 18.9688 20.7154 19.1551 20.6503C24.3899 20.2483 28.585 15.8289 28.585 10.3401C28.585 4.58142 23.9673 0 18.3761 0C12.7848 0 8.16717 4.58142 8.16717 10.3401C8.16717 11.4012 8.9982 12.2614 10.0233 12.2614C11.0485 12.2614 11.8795 11.4012 11.8795 10.3401Z" fill="url(#paint0_linear_18047_3240)"></path><defs><lineargradient id="paint0_linear_18047_3240" x1="7.955" y1="16.8477" x2="23.2962" y2="38.2338" gradientUnits="userSpaceOnUse"><stop stop-color="rgba(1, 167, 125, .9)"></stop><stop offset="1" stop-color="#60a5fa"></stop></lineargradient></defs></svg><span class="aifnmjmchg-text-[14px]">Teman-temanmu mendaftar</span></div><svg class="svg-inline--fa fa-arrow-down aifnmjmchg-w-[11px] aifnmjmchg-mx-[4px] aifnmjmchg-mt-[10px] aifnmjmchg-mb-[3px]" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-down" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path class="" fill="currentColor" d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"></path></svg><div class="aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-gap-[12px]"><svg width="25" height="25" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" style="max-width: 25px;"><path fill-rule="evenodd" clip-rule="evenodd" d="M11.1524 6.83074C11.1524 3.6117 13.7641 1 16.9831 1C20.2021 1 22.8138 3.6117 22.8138 6.83074V7.76822H27.9815C30.7352 7.76822 32.9662 9.99923 32.9662 12.7529V17.9206H33.9037C37.1227 17.9206 39.7344 20.5323 39.7344 23.7514C39.7344 26.9704 37.1227 29.5821 33.9037 29.5821H32.9662V34.7497C32.9662 37.5034 30.7352 39.7344 27.9815 39.7344H19.9511V35.5957C19.9511 33.9586 18.6203 32.6278 16.9831 32.6278C15.3459 32.6278 14.0151 33.9586 14.0151 35.5957V39.7344H5.98473C3.23101 39.7344 1 37.5034 1 34.7497L1.01059 26.7193H5.13867C6.77585 26.7193 8.10663 25.3885 8.10663 23.7513C8.10663 22.1141 6.77585 20.7833 5.13867 20.7833H1.00633L1.01692 12.7529C1.01692 12.7526 1.01692 12.7522 1.01692 12.7518C1.01755 10.0091 3.22096 7.76822 5.98473 7.76822H11.1524V6.83074ZM16.9831 4.20119C15.532 4.20119 14.3535 5.37967 14.3535 6.83074V10.9694H5.98473C5.00942 10.9694 4.21811 11.7567 4.21811 12.7529L4.21174 17.5822H5.13867C8.54382 17.5822 11.3078 20.3462 11.3078 23.7513C11.3078 27.1565 8.54382 29.9205 5.13867 29.9205H4.20756L4.20119 34.7497C4.20119 34.75 4.20119 34.7503 4.20119 34.7506C4.20168 35.7359 4.99928 36.5332 5.98473 36.5332H10.8139V35.5957C10.8139 32.1906 13.5779 29.4266 16.9831 29.4266C20.3882 29.4266 23.1522 32.1906 23.1522 35.5957V36.5332H27.9815C28.9672 36.5332 29.765 35.7354 29.765 34.7497V26.3809H33.9037C35.3547 26.3809 36.5332 25.2024 36.5332 23.7514C36.5332 22.3003 35.3547 21.1218 33.9037 21.1218H29.765V12.7529C29.765 11.7672 28.9672 10.9694 27.9815 10.9694H19.6126V6.83074C19.6126 5.37967 18.4342 4.20119 16.9831 4.20119Z" fill="white"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M11.1524 6.83074C11.1524 3.6117 13.7641 1 16.9831 1C20.2021 1 22.8138 3.6117 22.8138 6.83074V7.76822H27.9815C30.7352 7.76822 32.9662 9.99923 32.9662 12.7529V17.9206H33.9037C37.1227 17.9206 39.7344 20.5323 39.7344 23.7514C39.7344 26.9704 37.1227 29.5821 33.9037 29.5821H32.9662V34.7497C32.9662 37.5034 30.7352 39.7344 27.9815 39.7344H19.9511V35.5957C19.9511 33.9586 18.6203 32.6278 16.9831 32.6278C15.3459 32.6278 14.0151 33.9586 14.0151 35.5957V39.7344H5.98473C3.23101 39.7344 1 37.5034 1 34.7497L1.01059 26.7193H5.13867C6.77585 26.7193 8.10663 25.3885 8.10663 23.7513C8.10663 22.1141 6.77585 20.7833 5.13867 20.7833H1.00633L1.01692 12.7529C1.01692 12.7526 1.01692 12.7522 1.01692 12.7518C1.01755 10.0091 3.22096 7.76822 5.98473 7.76822H11.1524V6.83074ZM16.9831 4.20119C15.532 4.20119 14.3535 5.37967 14.3535 6.83074V10.9694H5.98473C5.00942 10.9694 4.21811 11.7567 4.21811 12.7529L4.21174 17.5822H5.13867C8.54382 17.5822 11.3078 20.3462 11.3078 23.7513C11.3078 27.1565 8.54382 29.9205 5.13867 29.9205H4.20756L4.20119 34.7497C4.20119 34.75 4.20119 34.7503 4.20119 34.7506C4.20168 35.7359 4.99928 36.5332 5.98473 36.5332H10.8139V35.5957C10.8139 32.1906 13.5779 29.4266 16.9831 29.4266C20.3882 29.4266 23.1522 32.1906 23.1522 35.5957V36.5332H27.9815C28.9672 36.5332 29.765 35.7354 29.765 34.7497V26.3809H33.9037C35.3547 26.3809 36.5332 25.2024 36.5332 23.7514C36.5332 22.3003 35.3547 21.1218 33.9037 21.1218H29.765V12.7529C29.765 11.7672 28.9672 10.9694 27.9815 10.9694H19.6126V6.83074C19.6126 5.37967 18.4342 4.20119 16.9831 4.20119Z" fill="url(#paint0_linear_18267_3259)"></path><defs><lineargradient id="paint0_linear_18267_3259" x1="9.30023" y1="18.1538" x2="24.794" y2="40.2877" gradientUnits="userSpaceOnUse"><stop stop-color="rgba(1, 167, 125, .9)"></stop><stop offset="1" stop-color="#60a5fa"></stop></lineargradient></defs></svg><span class="aifnmjmchg-text-[14px]">Mereka memasang ekstensi &amp; masuk. Kalian berdua mendapatkan kredit!</span></div></div><div class="aifnmjmchg-copy-link-wrapper aifnmjmchg-flex aifnmjmchg-items-center aifnmjmchg-justify-between aifnmjmchg-mt-[10px] aifnmjmchg-cursor-not-allowed"><span class="aifnmjmchg-overflow-hidden aifnmjmchg-w-5/12 aifnmjmchg-whitespace-nowrap aifnmjmchg-text-ellipsis aifnmjmchg-px-[18px] aifnmjmchg-opacity-50"></span><button type="button" class="aifnmjmchg-w-7/12 aifnmjmchg-h-[36px] aifnmjmchg-rounded-full hover:aifnmjmchg-opacity-90 active:aifnmjmchg-opacity-80 aifnmjmchg-text-white aifnmjmchg-bg-gradient-to-r aifnmjmchg-from-[#01a77d] aifnmjmchg-to-[#60a5fa]" style="text-shadow: rgba(0, 0, 0, 0.3) 1px 1px 1px;"><span class="aifnmjmchg-text-white">Salin Tautan Undangan</span></button></div><div class="aifnmjmchg-mt-[18px] aifnmjmchg-text-[--aifnmjmchg-tab-menu-active-bg-color] aifnmjmchg-cursor-pointer aifnmjmchg-text-center"><span class="aifnmjmchg-cursor-[pointer]">Periksa Catatan Undangan</span></div></div></div><!----></div></div></div></div><div class="ai-aifnmjmchgel-resize"></div></div></div><div id="aifnmjmchg-sidebar-opener" class="aifnmjmchg-cursor-pointer aifnmjmchg-show" style="bottom: 70px; right: 0px;"><div class="ai-aifnmjmchgopener-close"><svg class="svg-inline--fa fa-circle-xmark aifnmjmchg-w-4 aifnmjmchg-h-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="circle-xmark" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM175 175c9.4-9.4 24.6-9.4 33.9 0l47 47 47-47c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9l-47 47 47 47c9.4 9.4 9.4 24.6 0 33.9s-24.6 9.4-33.9 0l-47-47-47 47c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9l47-47-47-47c-9.4-9.4-9.4-24.6 0-33.9z"></path></svg></div><div class="opener-logo"><span name="logo" class="aifnmjmchg-w-[45px] aifnmjmchg-h-[45px]"><svg class=" aifnmjmchg-w-[45px] aifnmjmchg-h-[45px] aifnmjmchg-logo-dark aifnmjmchg-logo aifnmjmchg-p-0.5 " xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830.12 868.33">    <path fill="currentColor" d="M424.14,825.57c-114.47,0-207.59-93.13-207.59-207.59V261.32c0-114.46,93.12-207.59,207.59-207.59s207.59,93.13,207.59,207.59V618C631.73,732.44,538.6,825.57,424.14,825.57Zm0-713.31c-82.19,0-149.06,66.87-149.06,149.06V618C275.08,700.17,342,767,424.14,767S573.2,700.17,573.2,618V261.32C573.2,179.13,506.33,112.26,424.14,112.26Z"></path>    <path fill="currentColor" d="M578.23,736.49a206.33,206.33,0,0,1-103.45-27.9L165.91,530.27a207.59,207.59,0,0,1-76-283.58c57.24-99.13,184.45-133.21,283.58-76L682.37,349c99.13,57.23,133.22,184.45,76,283.58A206.21,206.21,0,0,1,632.3,729.33,208.85,208.85,0,0,1,578.23,736.49ZM270,201.45A149.18,149.18,0,0,0,140.61,276C99.52,347.13,124,438.48,195.17,479.58L504,657.9c71.18,41.1,162.53,16.63,203.62-54.56h0A149.06,149.06,0,0,0,653.1,399.72L344.23,221.39A148.22,148.22,0,0,0,270,201.45Z"></path>    <path fill="currentColor" d="M270,736.49A208.9,208.9,0,0,1,216,729.33,207.59,207.59,0,0,1,165.91,349L474.78,170.7c99.12-57.23,226.34-23.14,283.57,76h0c57.24,99.13,23.15,226.34-76,283.58L373.5,708.59A206.37,206.37,0,0,1,270,736.49Zm308.28-535A148.15,148.15,0,0,0,504,221.39L195.17,399.72A149.06,149.06,0,0,0,344.23,657.9L653.1,479.58c71.18-41.1,95.66-132.44,54.56-203.62L733,261.32,707.66,276A149.15,149.15,0,0,0,578.32,201.45Z"></path></svg></span></div></div><div style="display: none;"><div class="aifnmjmchg-mb-5 aifnmjmchg-max-w-[372px] aifnmjmchg-min-w-[360px]" id="aifnmjmchg-search-container"><div class="aifnmjmchg-bg-neutral-100 dark:aifnmjmchg-bg-neutral-900 dark:aifnmjmchg-text-gray-200 aifnmjmchg-rounded-lg aifnmjmchg-px-4 aifnmjmchg-py-3 aifnmjmchg-border aifnmjmchg-border-gray-50 dark:aifnmjmchg-border-neutral-700"><div class="aifnmjmchg-flex"><div class="aifnmjmchg-w-11/12 aifnmjmchg-flex aifnmjmchg-gap-2 xl:aifnmjmchg-gap-3 aifnmjmchg-items-center"><div class="aifnmjmchg-logo aifnmjmchg-flex aifnmjmchg-w-7/12 aifnmjmchg-place-items-center"><span name="logo" class="aifnmjmchg-w-7 aifnmjmchg-flex-initial"><svg class=" aifnmjmchg-w-7 aifnmjmchg-flex-initial aifnmjmchg-logo-dark aifnmjmchg-logo aifnmjmchg-p-0.5 " xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830.12 868.33">    <path fill="currentColor" d="M424.14,825.57c-114.47,0-207.59-93.13-207.59-207.59V261.32c0-114.46,93.12-207.59,207.59-207.59s207.59,93.13,207.59,207.59V618C631.73,732.44,538.6,825.57,424.14,825.57Zm0-713.31c-82.19,0-149.06,66.87-149.06,149.06V618C275.08,700.17,342,767,424.14,767S573.2,700.17,573.2,618V261.32C573.2,179.13,506.33,112.26,424.14,112.26Z"></path>    <path fill="currentColor" d="M578.23,736.49a206.33,206.33,0,0,1-103.45-27.9L165.91,530.27a207.59,207.59,0,0,1-76-283.58c57.24-99.13,184.45-133.21,283.58-76L682.37,349c99.13,57.23,133.22,184.45,76,283.58A206.21,206.21,0,0,1,632.3,729.33,208.85,208.85,0,0,1,578.23,736.49ZM270,201.45A149.18,149.18,0,0,0,140.61,276C99.52,347.13,124,438.48,195.17,479.58L504,657.9c71.18,41.1,162.53,16.63,203.62-54.56h0A149.06,149.06,0,0,0,653.1,399.72L344.23,221.39A148.22,148.22,0,0,0,270,201.45Z"></path>    <path fill="currentColor" d="M270,736.49A208.9,208.9,0,0,1,216,729.33,207.59,207.59,0,0,1,165.91,349L474.78,170.7c99.12-57.23,226.34-23.14,283.57,76h0c57.24,99.13,23.15,226.34-76,283.58L373.5,708.59A206.37,206.37,0,0,1,270,736.49Zm308.28-535A148.15,148.15,0,0,0,504,221.39L195.17,399.72A149.06,149.06,0,0,0,344.23,657.9L653.1,479.58c71.18-41.1,95.66-132.44,54.56-203.62L733,261.32,707.66,276A149.15,149.15,0,0,0,578.32,201.45Z"></path></svg></span><div class="aifnmjmchg-logo-text"><div class="aifnmjmchg-font-bold aifnmjmchg-pl-1 aifnmjmchg-pr-2 aifnmjmchg-break-keep aifnmjmchg-text-sm">ChatGPT Extension</div></div></div><div class="aifnmjmchg-credits aifnmjmchg-mr-3 aifnmjmchg-w-5/12"><button type="button" class="aifnmjmchg-text-neutral-500 dark:aifnmjmchg-text-neutral-300 aifnmjmchg-border-2 aifnmjmchg-border-solid aifnmjmchg-border-[var(--aifnmjmchg-tab-menu-active-bg-color)] hover:aifnmjmchg-bg-[var(--aifnmjmchg-tab-menu-active-bg-color)] hover:aifnmjmchg-text-white aifnmjmchg-rounded-lg focus:aifnmjmchg-outline-none aifnmjmchg-text-xs aifnmjmchg-p-2 aifnmjmchg-text-center aifnmjmchg-ask-search">Tanyakan pada ChatGPT</button></div></div><div class="aifnmjmchg-w-1/12 aifnmjmchg-flex aifnmjmchg-grid aifnmjmchg-grid-cols-1 aifnmjmchg-gap-3 aifnmjmchg-items-center"><div class="aifnmjmchg-switchbar-tab-item aifnmjmchg-gap-3 aifnmjmchg-place-items-end aifnmjmchg-rounded-lg aifnmjmchg-p-2 aifnmjmchg-cursor-pointer arc-edge aifnmjmchg-options-search"><svg class="svg-inline--fa fa-gear aifnmjmchg-h-4 aifnmjmchg-w-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="gear" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M495.9 166.6c3.2 8.7 .5 18.4-6.4 24.6l-43.3 39.4c1.1 8.3 1.7 16.8 1.7 25.4s-.6 17.1-1.7 25.4l43.3 39.4c6.9 6.2 9.6 15.9 6.4 24.6c-4.4 11.9-9.7 23.3-15.8 34.3l-4.7 8.1c-6.6 11-14 21.4-22.1 31.2c-5.9 7.2-15.7 9.6-24.5 6.8l-55.7-17.7c-13.4 10.3-28.2 18.9-44 25.4l-12.5 57.1c-2 9.1-9 16.3-18.2 17.8c-13.8 2.3-28 3.5-42.5 3.5s-28.7-1.2-42.5-3.5c-9.2-1.5-16.2-8.7-18.2-17.8l-12.5-57.1c-15.8-6.5-30.6-15.1-44-25.4L83.1 425.9c-8.8 2.8-18.6 .3-24.5-6.8c-8.1-9.8-15.5-20.2-22.1-31.2l-4.7-8.1c-6.1-11-11.4-22.4-15.8-34.3c-3.2-8.7-.5-18.4 6.4-24.6l43.3-39.4C64.6 273.1 64 264.6 64 256s.6-17.1 1.7-25.4L22.4 191.2c-6.9-6.2-9.6-15.9-6.4-24.6c4.4-11.9 9.7-23.3 15.8-34.3l4.7-8.1c6.6-11 14-21.4 22.1-31.2c5.9-7.2 15.7-9.6 24.5-6.8l55.7 17.7c13.4-10.3 28.2-18.9 44-25.4l12.5-57.1c2-9.1 9-16.3 18.2-17.8C227.3 1.2 241.5 0 256 0s28.7 1.2 42.5 3.5c9.2 1.5 16.2 8.7 18.2 17.8l12.5 57.1c15.8 6.5 30.6 15.1 44 25.4l55.7-17.7c8.8-2.8 18.6-.3 24.5 6.8c8.1 9.8 15.5 20.2 22.1 31.2l4.7 8.1c6.1 11 11.4 22.4 15.8 34.3zM256 336a80 80 0 1 0 0-160 80 80 0 1 0 0 160z"></path></svg></div></div></div><!----></div></div></div><textarea id="aifnmjmchg_clipboard" style="position: fixed; bottom: -10px; z-index: -1; height: 1px; width: 1px; font-size: 0.1px;"></textarea><!----><!----><span class="aifnmjmchg-min-h-[180px] aifnmjmchg-max-h-[180px] aifnmjmchg-min-h-[145px] aifnmjmchg-max-h-[145px] aifnmjmchg-min-h-[150px] aifnmjmchg-max-h-[150px] aifnmjmchg-min-h-[160px] aifnmjmchg-h-[160px] aifnmjmchg-max-h-[160px] aifnmjmchg-min-h-[265px] aifnmjmchg-h-[265px] aifnmjmchg-max-h-[265px] aifnmjmchg-hide"></span><!----></div><div data-v-a6bcf793="" class="aifnmjmchg light" nocolor=""><div data-v-a6bcf793="" class="aifnmjmchg-context-container" style="position: absolute; left: 0px; top: 0px; pointer-events: none; z-index: 2147483645;"><div data-v-a6bcf793="" style="top: 0px; left: 0px; position: absolute;"><div data-v-a6bcf793="" style="top: 305.333px; left: 408.667px; width: 76992px; height: 1px; position: absolute;"><!----><div data-v-a6bcf793="" class="aifnmjmchg-writing-btn-wrapper" id="aifnmjmchg-writing-btn" style="bottom: 14px; right: 14px; width: 16px; height: 16px; position: absolute;"><div data-v-a6bcf793="" class="aifnmjmchg-bg-[--aifnmjmchg-tab-menu-active-bg-color]" style="display: inline-block; width: 12px; height: 12px; border-radius: 16px; cursor: pointer; pointer-events: all;"><!----></div></div></div></div></div><!----><!----><!----></div><div><template shadowrootmode="open"><style>
:host{
  --black: #515151;
  --blue: #007BFF;
  --babyblue: #6DC1E8;
  --lightblue: #E1EEFF;
  --gray: #9B9B9B;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.chatbox::-webkit-scrollbar, #text-area::-webkit-scrollbar {
  width: 6px;
}

.chatbox::-webkit-scrollbar-thumb, #text-area::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 5px; 
}

.chatbox::-webkit-scrollbar-thumb:hover, #text-area::-webkit-scrollbar-hover {
  background: #555; 
}

.slider-container{
  flex-direction: column;
  position:fixed;
  background: #F8FBFF;
  font-family: 'Inter', 'sans-serif';
  font-style: normal;
  color: var(--black);
  border-radius: 15px 0px 0px 15px;
  height: 100vh;
  width: 450px;
  top: 0;
  right: 0;
  z-index: 9999;
  padding: 0 0 16px 0;
  transition: transform 300ms ease-in-out;
}

.isHidden {
  transform: translateX(450px);
  transition: transform 300ms ease-in-out;
}

.header {
  padding: 0 20px;
  display:flex;
  justify-content: space-between;
  align-items: center;
  font-family: "Poppins", serif;
  height: 90px;
  border-bottom: 1px solid #E2E2E2;
  box-shadow: 0px 42px 67px 0px rgba(122, 122, 122, 0.1);
}

.logo {
  font-size: 32px;
  font-weight: 700;
}

.icon-border {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(2*16px);
  width: calc(2*16px);
  margin: 0;
  padding: 0;
  background-color: #E1EEFF;
  border-radius: 50%;
}

.chatbox {
  padding-top: 16px;
  overflow-y: auto;
  height: 60vh;
}

.chatting {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 16px;
  overflow-y: auto;
}

.chat-bubble {
  padding: 10px;
}

.user-chat {
  color: #fff;
  background-color: var(--blue);
  align-self: flex-end;
  border-radius: 10px 0px 10px 10px;
}

.ai-chat {
  color: var(--black);
  background-color: var(--lightblue);
  align-self: flex-start;
  border-radius: 0px 10px 10px 10px;
  max-width: 90%;
}

.follow-up-container {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 16px;
}

.follow-up {
  color: var(--blue);
  border: 1px solid var(--blue);
  border-radius: 16px;
  padding: 8px;
}

.hero {
  padding: 0 20px;
  font-size: 35px;
  font-weight: 700;
}

.welcome {
  color: var(--gray);
  font-size: 16px;
  font-weight: 400;
}

.file-type {
  font-size: 16px;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  width: 100%;
  align-items: center;
  text-align: center;
  margin-top: calc(1.5*16px);
  margin-bottom: calc(1.5*16px);
}

.file-card {
  background-color: var(--lightblue);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  max-width: 48%;
  padding: 16px;
  gap: calc(0.5*16px);
  border-radius: 10px;
}

.file-card p:nth-of-type(2) {
  color: var(--gray);
  font-weight: 400;
  font-size: 13px;
}

.example-query {
  font-size: 16px;
  padding: 0 20px;
  display:flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  gap: 16px;
}

.example-card {
  background-color: var(--lightblue);
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 16px;
  border-radius: 10px;
  font-weight: 700;
  text-decoration: none;
  color: inherit;
}

.example p:nth-child(2) {
  color: var(--gray);
  font-weight: 400;
  font-size: 13px;
}

.input-section {
  flex: 1;
  width: 100%;
  border-top: 1px solid #E2E2E2;
  box-shadow: 0px -42px 67px 0px rgba(122, 122, 122, 0.1);
}

.toolbar {
  padding: 0 20px;
  margin-top: 16px;
  display: flex;
  justify-content: space-between;
}

.radio-buttons {
  display: flex;
  justify-content: space-between;
  gap: calc(0.7*16px);
  align-items: center;
  font-size: 13.33px;
  color: var(--gray);
}

.radio-button {
  display: flex;
  align-items: center;
  gap: 5px;
}

.tools {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--babyblue);
  gap: calc(0.5*16px);
}

.text-input {
  min-height: 178px;
  margin: 16px 20px 16px 20px;
  border-radius: 20px;
  padding: 16px 16px;
  background-color: #ffffff;
}

#pdf-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px;
  border-radius: 12px;
  background-color: #F8F8F8;
}

#pdfimg-name {
  display: flex;
  align-items: center;
  gap: 8px;
}

#text-area {
  font-family: 'Inter', 'sans-serif';
  width: 100%;
  height: 110px;
  background-color: inherit;
  color: var(--black);
  resize: none;
  outline: none;
  border: none;
}

.buttons {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.copyright {
  color: var(--gray);
  font-size: 13px;
  font-weight: 400;
}

.status {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
}

.status-card {
  display: flex;
  width: 60px;
  height: 32px;
  padding: 4px 8px;
  justify-content: center;
  align-items: center;
  gap: 4px;
  border-radius: 99px;
  font-size: 16px;
  background: rgba(6, 65, 135, 0.70);
  color: #fff;
}

.point {
  font-size: 14px;
  font-style: normal;
  font-weight: 600;
  text-align: center;
  line-height: normal;
}

.subscription {
  background: var(--Linear-Blue, linear-gradient(290deg, #064187 1.05%, #007BFF 100%));
}

.blue-text{
  color:var(--blue);
}

.clickable{
  cursor: pointer;
}

.switch_stealth_mode {
  position: relative;
  display: inline-block;
  width: 48px;
  height: 24px;
}

.switch_stealth_mode input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .4s;
}

input:checked + .slider {
  background-color: #0066d3;
}

input:checked + .slider:before {
  transform: translateX(24px);
}

.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}

  .tooltip {
    position: absolute;
    background-color: white;
    color: black;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 14px;
    white-space: nowrap;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.2s ease-in-out, visibility 0.2s ease-in-out;
  }

  .tooltip.show {
    opacity: 1;
    visibility: visible;
  }

  .tooltip.top {
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    margin-bottom: 5px;
  }

  .tooltip.topRightGpt4v,
  .tooltip.topRightWolfram {
    bottom: 100%;
    left: 0;
    margin-bottom: 5px;
  }

  .code-block-header {
    background-color: #333333;
    color: white;
    font-size: 0.75rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.75rem;
    border-top-left-radius: 0.75rem;
    border-top-right-radius: 0.75rem;
  }

  .language-label {
    width: fit-content;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    color: white;
    font-size: 0.75rem;
  }

  .copy-button {
    background: none;
    border: none;
    width: fit-content;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 0.375rem;
    padding: 0 0.25rem;
  }

  .copy-text {
    margin: 0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    width: fit-content;
    color: white;
    font-size: 0.75rem;
  }

  .chat-bubble * {
    line-height: 1.5;
  }

  .chat-bubble .katex-display {
    overflow-y: visible;
  }

  .chat-bubble .katex {
    font-size: 18px !important;
  }

  .chat-bubble p {
    display: inline;
    margin: 0.27em 0;
  }

  .chat-bubble li {
    margin-bottom: 0.5em;
  }

  .chat-bubble h1, .chat-bubble h2, .chat-bubble h3, .chat-bubble h4, .chat-bubble h5, .chat-bubble h6 {
    margin-top: 0.75em;
    margin-bottom: 0.75em;
  }

  .chat-bubble ul, .chat-bubble ol {
    width: calc(100% - 20px);
    padding-left: 20px;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
  }

  .chat-bubble pre {
    border-radius: 0 0 12px 12px;
    overflow: auto;
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    font-size: 12px;
    line-height: 1.5;
  }

  .chat-bubble pre code {
    padding: 20px;
    white-space: pre-wrap;
  }

  .chat-bubble table {
    display: block;
    margin: 0.5em 0;
    border-collapse: collapse;
    overflow: auto;
  }

  .chat-bubble table th, .chat-bubble table td {
    padding: 0.5em 0.75em;
    border: 1px solid #dfe2e5;
  }

  .chat-bubble ul {
    list-style: disc;
  }

  .chat-bubble ol {
    list-style: decimal;
  }

  .chat-bubble .code-block {
    margin-block: 12px;
  }

    .chat-bubble .code-inline {
    font-size: 15px;
  }

  pre code.hljs {
  display: block;
  overflow-x: auto;
  padding: 1em
}

  code.hljs {
    padding: 3px 5px
  }

  .hljs {
    background: #1d1f21;
    color: #c5c8c6
  }
  .hljs::selection,
  .hljs span::selection {
    background: #373b41
  }
  .hljs::-moz-selection,
  .hljs span::-moz-selection {
    background: #373b41
  }
  .hljs-title,
  .hljs-name {
    color: #f0c674
  }
  .hljs-comment,
  .hljs-meta,
  .hljs-meta .hljs-keyword {
    color: #707880
  }
  .hljs-number,
  .hljs-symbol,
  .hljs-literal,
  .hljs-deletion,
  .hljs-link {
    color: #cc6666
  }
  .hljs-string,
  .hljs-doctag,
  .hljs-addition,
  .hljs-regexp,
  .hljs-selector-attr,
  .hljs-selector-pseudo {
    color: #b5bd68
  }
  .hljs-attribute,
  .hljs-code,
  .hljs-selector-id {
    color: #b294bb
  }
  .hljs-keyword,
  .hljs-selector-tag,
  .hljs-bullet,
  .hljs-tag {
    color: #81a2be
  }
  .hljs-subst,
  .hljs-variable,
  .hljs-template-tag,
  .hljs-template-variable {
    color: #8abeb7
  }
  .hljs-type,
  .hljs-built_in,
  .hljs-quote,
  .hljs-section,
  .hljs-selector-class {
    color: #de935f
  }
  .hljs-emphasis {
    font-style: italic
  }
  .hljs-strong {
    font-weight: bold
  }
</style><div class="slider-container isHidden" style="display: none;"><div class="header"><img class="clickable" src="chrome-extension://aeldeepjdhhldhbgfodleiodmeegnacm/icons/settings.svg" alt="settings"><h1 class="logo"><span class="blue-text">PhotoSolve</span></h1><img class="clickable" src="chrome-extension://aeldeepjdhhldhbgfodleiodmeegnacm/icons/exit.svg" alt="exit"></div><div class="chatbox"><div class="hero"><p>Hi <span class="blue-text">There!</span> 👋<br>Good Evening!</p><p class="welcome">Welcome to AI tutor. Ask me about ...</p></div><div class="file-type"><div class="file-card screenshot clickable"><img src="chrome-extension://aeldeepjdhhldhbgfodleiodmeegnacm/icons/crop.svg" alt="crop"><p>Screenshot</p><p>Capture an image from your screen.</p></div><div class="file-card attachment clickable" role="presentation" tabindex="0"><input accept="image/*,.png,.gif,.jpeg,.jpg,application/pdf,.pdf" multiple="" type="file" tabindex="-1" style="display: none;"><img src="chrome-extension://aeldeepjdhhldhbgfodleiodmeegnacm/icons/img-pdf.svg" alt="img-pdf"><p>Attachment</p><p>Drag and drop here to upload a file.</p></div></div><div class="example-query"><div class="example-card clickable"><div class="example"><p>Design a database schema</p><p>for an online merch store</p></div><i class="fa-solid fa-arrow-right"></i></div><div class="example-card clickable"><div class="example"><p>Make a content strategy</p><p>for local weekend events</p></div><i class="fa-solid fa-arrow-right"></i></div></div></div><div class="input-section"><div class="toolbar"><div class="radio-buttons"><div style="position: relative; display: inline-block;"><div style="position: absolute; border-radius: 0.5rem; box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.05) 0px 4px 6px -2px; z-index: 50; padding: 0.4rem; background-color: white; opacity: 0; visibility: hidden; transition: opacity 0.2s ease-in-out, visibility 0.2s ease-in-out; width: 182px; top: -60px; left: 0%; color: black;">Image Vision only available to PRO subscribers</div><div class="gpt radio-button"><p>Image Vision</p><label class="switch_stealth_mode"><input type="checkbox" id="stealth_mode_toggle" disabled=""><span class="slider round"></span></label></div></div><div style="position: relative; display: inline-block;"><div style="position: absolute; border-radius: 0.5rem; box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.05) 0px 4px 6px -2px; z-index: 50; padding: 0.4rem; background-color: white; opacity: 0; visibility: hidden; transition: opacity 0.2s ease-in-out, visibility 0.2s ease-in-out; width: 154px; top: -60px; left: 0%; color: black;">Wolfram only available to PRO subscribers</div><div class="wolfram radio-button"><p>Wolfram</p><label class="switch_stealth_mode"><input type="checkbox" id="stealth_mode_toggle" disabled=""><span class="slider round"></span></label></div></div></div><div class="tools"><div style="position: relative; display: inline-block;"><div style="position: absolute; border-radius: 0.5rem; box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.05) 0px 4px 6px -2px; z-index: 50; padding: 0.4rem; background-color: white; opacity: 0; visibility: hidden; transition: opacity 0.2s ease-in-out, visibility 0.2s ease-in-out; width: 80px; white-space: nowrap; bottom: 100%; left: 50%; transform: translateX(-50%); margin-bottom: 5px; color: black; font-size: 12px; font-weight: 400;">Screenshot</div><img class="clickable" src="chrome-extension://aeldeepjdhhldhbgfodleiodmeegnacm/icons/crop-chatbox.svg" alt="crop"></div><div style="position: relative; display: inline-block;"><div style="position: absolute; border-radius: 0.5rem; box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.05) 0px 4px 6px -2px; z-index: 50; padding: 0.4rem; background-color: white; opacity: 0; visibility: hidden; transition: opacity 0.2s ease-in-out, visibility 0.2s ease-in-out; width: 80px; white-space: nowrap; bottom: 100%; left: 50%; transform: translateX(-50%); margin-bottom: 5px; color: black; font-size: 12px; font-weight: 400;">Upload File</div><div role="presentation" tabindex="0"><img class="clickable" src="chrome-extension://aeldeepjdhhldhbgfodleiodmeegnacm/icons/uploadfile-chatbox.svg" alt="pdf"><input accept="image/*,.png,.gif,.jpeg,.jpg,application/pdf,.pdf" multiple="" type="file" tabindex="-1" style="display: none;"></div></div><div style="border-left: 2px solid rgb(226, 226, 226); height: 20px;"></div><div style="position: relative; display: inline-block;"><div style="position: absolute; border-radius: 0.5rem; box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.05) 0px 4px 6px -2px; z-index: 50; padding: 0.4rem; background-color: white; opacity: 0; visibility: hidden; transition: opacity 0.2s ease-in-out, visibility 0.2s ease-in-out; width: 80px; white-space: nowrap; bottom: 100%; left: 50%; transform: translateX(-50%); margin-bottom: 5px; color: black; font-size: 12px; font-weight: 400;">New Chat</div><img class="clickable" src="chrome-extension://aeldeepjdhhldhbgfodleiodmeegnacm/icons/addconvo-chatbox.svg" alt="addconvo"></div></div></div><div class="text-input"><textarea name="text-input" id="text-area" placeholder="Ask me a question..."></textarea><div class="buttons"><img class="clickable" src="chrome-extension://aeldeepjdhhldhbgfodleiodmeegnacm/icons/mic-disabled.svg" alt="microphone"><img class="clickable" src="chrome-extension://aeldeepjdhhldhbgfodleiodmeegnacm/icons/send.svg" alt="send"></div></div><footer><p class="copyright"></p><div class="status"><div class="point status-card"><img src="chrome-extension://aeldeepjdhhldhbgfodleiodmeegnacm/icons/thunder.svg" alt="thunder"><p>0</p></div><div class="subscription status-card clickable"><p>PRO</p></div></div></footer></div></div></template></div></html>