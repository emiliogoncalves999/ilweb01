(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[6590],{24960:function(){},26759:function(){},56272:function(){},8543:function(e,t,n){Promise.resolve().then(n.bind(n,21164)),Promise.resolve().then(n.bind(n,52692)),Promise.resolve().then(n.bind(n,42395)),Promise.resolve().then(n.bind(n,32057)),Promise.resolve().then(n.bind(n,35093))},1255:function(e,t,n){"use strict";n.d(t,{Z:function(){return y}});var r=n(22988),o=n(23950),i=n(2265),a=i.useLayoutEffect,s=function(e){var t=i.useRef(e);return a(function(){t.current=e}),t},l=function(e,t){if("function"==typeof e){e(t);return}e.current=t},u=function(e,t){var n=(0,i.useRef)();return(0,i.useCallback)(function(r){e.current=r,n.current&&l(n.current,null),n.current=t,t&&l(t,r)},[t])},c={"min-height":"0","max-height":"none",height:"0",visibility:"hidden",overflow:"hidden",position:"absolute","z-index":"-1000",top:"0",right:"0"},d=function(e){Object.keys(c).forEach(function(t){e.style.setProperty(t,c[t],"important")})},f=null,p=function(e,t){var n=e.scrollHeight;return"border-box"===t.sizingStyle.boxSizing?n+t.borderSize:n-t.paddingSize},h=function(){},m=["borderBottomWidth","borderLeftWidth","borderRightWidth","borderTopWidth","boxSizing","fontFamily","fontSize","fontStyle","fontWeight","letterSpacing","lineHeight","paddingBottom","paddingLeft","paddingRight","paddingTop","tabSize","textIndent","textRendering","textTransform","width","wordBreak"],g=!!document.documentElement.currentStyle,b=function(e){var t=window.getComputedStyle(e);if(null===t)return null;var n=m.reduce(function(e,n){return e[n]=t[n],e},{}),r=n.boxSizing;if(""===r)return null;g&&"border-box"===r&&(n.width=parseFloat(n.width)+parseFloat(n.borderRightWidth)+parseFloat(n.borderLeftWidth)+parseFloat(n.paddingRight)+parseFloat(n.paddingLeft)+"px");var o=parseFloat(n.paddingBottom)+parseFloat(n.paddingTop),i=parseFloat(n.borderBottomWidth)+parseFloat(n.borderTopWidth);return{sizingStyle:n,paddingSize:o,borderSize:i}};function T(e,t,n){var r=s(n);i.useLayoutEffect(function(){var n=function(e){return r.current(e)};if(e)return e.addEventListener(t,n),function(){return e.removeEventListener(t,n)}},[])}var v=function(e){T(window,"resize",e)},x=function(e){T(document.fonts,"loadingdone",e)},S=["cacheMeasurements","maxRows","minRows","onChange","onHeightChange"],y=i.forwardRef(function(e,t){var n=e.cacheMeasurements,a=e.maxRows,s=e.minRows,l=e.onChange,c=void 0===l?h:l,m=e.onHeightChange,g=void 0===m?h:m,T=(0,o.Z)(e,S),y=void 0!==T.value,w=i.useRef(null),E=u(w,t),_=i.useRef(0),P=i.useRef(),C=function(){var e,t,r,o,i,l,u,c,h,m,T,v=w.current,x=n&&P.current?P.current:b(v);if(x){P.current=x;var S=(e=v.value||v.placeholder||"x",void 0===(t=s)&&(t=1),void 0===(r=a)&&(r=1/0),f||((f=document.createElement("textarea")).setAttribute("tabindex","-1"),f.setAttribute("aria-hidden","true"),d(f)),null===f.parentNode&&document.body.appendChild(f),o=x.paddingSize,i=x.borderSize,u=(l=x.sizingStyle).boxSizing,Object.keys(l).forEach(function(e){f.style[e]=l[e]}),d(f),f.value=e,c=p(f,x),f.value=e,c=p(f,x),f.value="x",m=(h=f.scrollHeight-o)*t,"border-box"===u&&(m=m+o+i),c=Math.max(m,c),T=h*r,"border-box"===u&&(T=T+o+i),[c=Math.min(T,c),h]),y=S[0],E=S[1];_.current!==y&&(_.current=y,v.style.setProperty("height",y+"px","important"),g(y,{rowHeight:E}))}};return i.useLayoutEffect(C),v(C),x(C),i.createElement("textarea",(0,r.Z)({},T,{onChange:function(e){y||C(),c(e)},ref:E}))})},21164:function(e,t,n){"use strict";n.d(t,{FromTextWithoutFormProvider:function(){return v}});var r=n(57437),o=n(2265),i=n(42395),a=n(32057),s=n(14976),l=n(98090),u=n(45715),c=n(76912),d=n(30653),f=n(79294);let p={darkModeTrigger:l.U.DARK_MODE_TXT,buyTokenTrigger:l.U.BUY_TOKENS_TXT,canvasTrigger:l.U.CANVAS_TXT,remixTrigger:l.U.IMAGE_REMIX_TXT,textImageTrigger:l.U.TEXT_TO_IMAGE_TXT,backTrigger:l.U.BACK_BUTTON_TXT,upgradeTrigger:l.U.UPGRADE_TXT},h=e=>{let{children:t,navbarProps:n,primarySidebarProps:o}=e;return(0,r.jsxs)(d.X,{children:[(0,r.jsx)(d.X.Header,{children:(0,r.jsx)(c.pC,{...n,trigger:p,variant:u.x.TEXT_TO_IMAGE})}),(0,r.jsxs)(d.X.Body,{children:[(0,r.jsx)(c.hI,{...o}),(0,r.jsx)("section",{className:"flex h-full flex-1 flex-col overflow-hidden",children:t}),(0,r.jsx)(f.m,{isSubscriptionActive:n.isSubscriptionActive})]})]})};var m=n(5672),g=n(81750),b=n(27424),T=n(14125);let v=e=>{let{children:t}=e,{setActiveTool:n}=(0,a.B)(),{formHook:l}=(0,i.K)(),u=(0,m.TI)(e=>e.collections),c=(0,s.h)(m.TI),d=(0,m.TI)(e=>e.setSelectedCollection),f=(0,g.m8)()(e=>e.subscription),{isSubscriptionActive:p}=(0,T.L)(f);return(0,o.useEffect)(()=>{n(b.X.FromText)},[n]),(0,r.jsx)(h,{navbarProps:{selectedCollection:c,isSubscriptionActive:p},primarySidebarProps:{collectionState:{collections:u,selectedCollection:c,onCollectionSelect:e=>{d(e),l.reset(e.settings)}}},children:t})}},52692:function(e,t,n){"use strict";n.d(t,{PersistFromTextFormValues:function(){return f}});var r=n(2265),o=n(39343),i=n(91606),a=n(42395),s=n(14976),l=n(43897),u=n(5672),c=n(82074),d=n(10733);let f=()=>{let{formHook:e}=(0,a.K)(),t=(0,s.h)(u.TI),n=(0,i.O_)(),f=(0,c.p)(e=>e.persistFromTextSetting),{fromText:p}=(0,d.Td)()(e=>e.defaultSettings),h=(0,l.HO)(p.styleListId),m=(0,l.VI)(p.modelListId),g=(0,o.qo)({control:e.control});return(0,r.useEffect)(()=>{if(!n||t||!g)return;let e=g.style,r=g.model;f({...g,style:null!=e?e:h,model:null!=r?r:m,tags:{}})},[g,t,h,m,f,n]),null}},44177:function(e,t,n){"use strict";n.d(t,{L:function(){return o},a:function(){return r}});let r=["_id","uid","projectId","teamID","isPublic","hasPublicLink","zIndex","cornerRadius","mockupDataId","parentArtboard","smartObjectParent","thumbnailArtboard","fills","uniformScaling","uniformInnerScaling","pinToEdge","evented","selectable","title","projectTitle","visible","showSubLayers","colorTag","lowPowerMode","drawPixelGrids","snapToPixelGrids","showMotionPath","snapOnMove","snapOnResize","isClipPath","grid","parent","layerInfo","createdBy","timestamp","clippingmagic","aiContainer","maskType","projectDesc","projectTags","AWS_Key","projectColors","colorPalettes","showProjectColors","backgroundColor","animated","videoSrc","loopVideo","isVideo","patternSrc","animations","animationFrom","animationDuration","motionOptionsExpanded","customFont","customFonts","animationPathInfo","animationPathOffset","animationPathOffsetAngle","transformEffect","startAngle","assetData","originalText","seoGroup","projectPublished","premiumTemplate","perspectiveScene","publicTemplate","hasCustomThumbnail","videoPreview","layerNameHasBeenEdited","lockedByUser","showCellConnections","linkedTo","columnWidth","columnLeft","columnType","table","csvURL","content","artboards","cellIndices","userSetTextboxWidth","FORCE_MIN_TEXT_WIDTH","forceOrigins","isMask","aspectRatio"],o="shouldOptimizePhotoSerialization"},16092:function(e,t,n){"use strict";n.d(t,{C:function(){return c},o:function(){return u}});var r=n(72143),o=n(8127),i=n(54795),a=n(47802);let s=(e,t)=>{let{cfg:n}=e,r={...(0,i.WX)(e,t),cfg:n};return(0,a.wh)(r)},l=new AbortController,u=async(e,t,n)=>{l.signal.aborted&&(l=new AbortController);let a=(0,i.kw)(t);a.append("Style-Id","".concat(e.model.model_id));let{data:u}=await r.p.post(i.TG.FROM_TEXT,{body:s(e,n),headers:a,signal:l.signal},{throwOnError:!0});return{src:(0,o.RJ)(u),randomSeed:n}},c=()=>{l.abort()}},23950:function(e,t,n){"use strict";function r(e,t){if(null==e)return{};var n,r,o={},i=Object.keys(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}n.d(t,{Z:function(){return r}})}},function(e){e.O(0,[4705,789,1750,1763,231,1606,7754,7337,6533,3684,5018,9659,5510,8173,3304,7071,9772,3393,9678,2061,4756,2447,9343,901,9758,1554,3852,6573,9515,9622,974,6750,8030,8795,8211,4148,6912,5169,3843,1721,1275,2971,7023,1744],function(){return e(e.s=8543)}),_N_E=e.O()}]);