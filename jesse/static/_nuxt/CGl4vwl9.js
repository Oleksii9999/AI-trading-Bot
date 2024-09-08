import{_ as Z}from"./BhE9eUkV.js";import{h as E,o as a,c as i,E as h,b as c,r as x,N as A,a5 as J,y as K,aq as Q,z as X,d as y,w as R,l as V,F as w,j as C,e as D,M as f,H as I,V as ee,m as te,v as oe,t as b,G as re,n as z}from"./CtfKdue9.js";import{d as ae}from"./uU1M6rQW.js";import{_ as se}from"./Ca0ihDfi.js";const le=["innerHTML"],ze=E({__name:"Logs",props:{logs:{}},setup(_){return(e,k)=>{const d=Z;return e.logs.length?(a(),i("pre",{key:0,class:"whitespace-pre-line rounded border dark:border-gray-600 bg-gray-50 dark:bg-gray-700 select-text text-base dark:text-gray-300 w-full px-4 sm:px-6 py-2",innerHTML:e.logs},null,8,le)):(a(),h(d,{key:1}))}}});function T(_,e){return a(),i("svg",{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 24 24",fill:"currentColor","aria-hidden":"true","data-slot":"icon"},[c("path",{"fill-rule":"evenodd",d:"M12 3.75a.75.75 0 0 1 .75.75v6.75h6.75a.75.75 0 0 1 0 1.5h-6.75v6.75a.75.75 0 0 1-1.5 0v-6.75H4.5a.75.75 0 0 1 0-1.5h6.75V4.5a.75.75 0 0 1 .75-.75Z","clip-rule":"evenodd"})])}const ne={id:"routes-section",class:"select-none"},ie={class:"w-full flex justify-center"},ue=c("span",null,"Trading Route",-1),de=c("span",null,"Data Route",-1),Te=E({__name:"Routes",props:{mode:{},timeframes:{},symbols:{},form:{},results:{},totalRoutesError:{}},setup(_){const e=_,k=x([]),d=x(""),r=A(),v=x({data_routes:e.form.data_routes}),M=x({routes:e.form.routes}),s=J({uniqueRoutesErrorMessage:"each exchange-symbol pair can be traded only once! More info: https://docs.jesse.trade/docs/routes.html#trading-multiple-routes",maxSymbolLengthErrorMessage:"Maximum symbol length is exceeded!",mustContainDashErrorMessage:'Symbol parameter must contain "-" character!',timeframeMustBeDifferentErrorMessage:"Data routes' timeframe and trading routes' timeframe must be different",emptyParameter:"You must fill all the parameters",invalidSymbol:"Symbol is invalid"}),U=K(()=>r.strategies);Q(()=>{v.value={data_routes:e.form.data_routes},M.value={routes:e.form.routes},O(),B()});function O(){e.form.routes.length||e.form.routes.push({symbol:"",timeframe:r.jesseSupportedTimeframes.includes("4h")?"4h":r.jesseSupportedTimeframes[r.jesseSupportedTimeframes.length-1],strategy:r.strategies[0]})}function B(){e.totalRoutesError.splice(0,e.totalRoutesError.length);for(const n of e.form.routes)$(n);if(e.form.data_routes.length>0)for(const n of e.form.data_routes)$(n);let t=!1;const o=e.form.routes;for(const n of o.slice(0,-1)){if(e.totalRoutesError.includes(s.uniqueRoutesErrorMessage)||t)break;for(const g of o.slice(o.indexOf(n)+1))if(n.strategy===g.strategy&&n.symbol===g.symbol&&n.symbol.length!==0){e.totalRoutesError.push(s.uniqueRoutesErrorMessage),t=!1;break}}let m=!1;const p=e.form.data_routes;for(const n of p.slice(0,-1)){if(e.totalRoutesError.includes(s.uniqueRoutesErrorMessage)||m)break;for(const g of p.slice(p.indexOf(n)+1))if(n.timeframe===g.timeframe&&n.symbol===g.symbol){e.totalRoutesError.push(s.uniqueRoutesErrorMessage),m=!0;break}}if(e.form.data_routes.length>0)for(const n of p){if(e.totalRoutesError.includes(s.timeframeMustBeDifferentErrorMessage)||t)break;for(const g of e.form.routes)if(n.symbol===g.symbol&&n.timeframe===g.timeframe){e.totalRoutesError.push(s.timeframeMustBeDifferentErrorMessage),m=!0;break}}}function $(t){!e.totalRoutesError.includes(s.emptyParameter)&&(t.symbol.length==0||t.timeframe.length==0)&&e.totalRoutesError.push(s.emptyParameter)}function j(){e.form.routes.push({symbol:"",timeframe:r.jesseSupportedTimeframes.includes("4h")?"4h":r.jesseSupportedTimeframes[r.jesseSupportedTimeframes.length-1],strategy:r.strategies[0]})}function q(){e.form.data_routes.push({symbol:"",timeframe:r.jesseSupportedTimeframes.includes("4h")?"4h":r.jesseSupportedTimeframes[r.jesseSupportedTimeframes.length-1]})}function L(t){const o=e.form.routes.indexOf(t);e.form.routes.length!==1&&o>-1&&e.form.routes.splice(o,1)}function N(t){const o=e.form.data_routes.indexOf(t);e.form.data_routes.length!==0&&o>-1&&e.form.data_routes.splice(o,1)}function H(t){const o=e.form.routes.indexOf(t),m={strategy:t.strategy,symbol:"",timeframe:t.timeframe};e.form.routes.splice(o+1,0,m)}function P(t){const o=e.form.data_routes.indexOf(t),m={symbol:"",timeframe:t.timeframe};e.form.data_routes.splice(o+1,0,m)}function F(t){const o=e.form.routes.indexOf(t);o!==0&&(e.form.routes[o]=e.form.routes[o-1],e.form.routes[o-1]=t)}function W(t){const o=e.form.data_routes.indexOf(t);o!==0&&(e.form.data_routes[o]=e.form.data_routes[o-1],e.form.data_routes[o-1]=t)}function G(t){const o=e.form.routes.indexOf(t);o!==e.form.routes.length-1&&(e.form.routes[o]=e.form.routes[o+1],e.form.routes[o+1]=t)}function Y(t){const o=e.form.data_routes.indexOf(t);o!==e.form.data_routes.length-1&&(e.form.data_routes[o]=e.form.data_routes[o+1],e.form.data_routes[o+1]=t)}return X(()=>d.value,t=>{if(t.length==0){k.value=[];return}const o=[];for(const m of e.symbols){if(o.length>50)break;m.toLowerCase().startsWith(t.toLowerCase())&&o.push(m)}k.value=o}),(t,o)=>{const m=ae,p=se,n=I,g=ee;return a(),i("div",ne,[y(m,{title:"Routes"},{default:R(()=>[c("div",ie,[c("button",{type:"button",class:"inline-flex items-center shadow-sm px-4 py-1.5 border border-gray-300 dark:border-gray-900 text-sm leading-5 font-medium rounded-l-full text-gray-700 dark:text-gray-100 bg-white dark:bg-backdrop-dark hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none",onClick:j},[y(V(T),{class:"-ml-1.5 mr-1 h-5 w-5 text-gray-400","aria-hidden":"true"}),ue]),c("button",{type:"button",class:"inline-flex items-center shadow-sm px-4 py-1.5 border border-gray-300 dark:border-gray-900 text-sm leading-5 font-medium rounded-r-full text-gray-700 dark:text-gray-100 bg-white dark:bg-backdrop-dark hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none",onClick:q},[y(V(T),{class:"-ml-1.5 mr-1 h-5 w-5 text-gray-400","aria-hidden":"true"}),de])])]),_:1}),(a(!0),i(w,null,C(t.form.routes,(l,S)=>(a(),i("div",{key:l.symbol+S,class:"flex mt-4"},[y(p,{modelValue:l.symbol,"onUpdate:modelValue":u=>l.symbol=u,query:d.value,"onUpdate:query":o[0]||(o[0]=u=>d.value=u),"clear-search-on-close":"",class:"w-full",ui:{rounded:"rounded-none rounded-l"},searchable:"","searchable-placeholder":"Search symbols...",size:"lg",options:k.value,placeholder:"Select a symbol...",onChange:o[1]||(o[1]=u=>d.value="")},{empty:R(()=>[D("Start typing...")]),_:2},1032,["modelValue","onUpdate:modelValue","query","options"]),y(p,{modelValue:l.timeframe,"onUpdate:modelValue":u=>l.timeframe=u,class:"w-full",ui:{rounded:"rounded-none"},size:"lg","value-attribute":"value",options:t.timeframes},null,8,["modelValue","onUpdate:modelValue","options"]),y(p,{modelValue:l.strategy,"onUpdate:modelValue":u=>l.strategy=u,class:"w-full",ui:{rounded:"rounded-none rounded-r"},size:"lg",options:U.value,searchable:""},null,8,["modelValue","onUpdate:modelValue","options"]),t.form.routes.length>1?(a(),h(n,{key:0,class:"",size:"lg",variant:"link",color:"gray",icon:"i-heroicons-trash",disabled:t.form.routes.length===1,onClick:u=>L(l)},null,8,["disabled","onClick"])):f("",!0),t.form.routes.length>1?(a(),h(n,{key:1,class:"",size:"lg",variant:"link",color:"gray",icon:"i-heroicons-document-duplicate",disabled:t.form.routes.length===1,onClick:u=>H(l)},null,8,["disabled","onClick"])):f("",!0),t.form.routes.length>1?(a(),h(n,{key:2,class:"",size:"lg",variant:"link",color:"gray",icon:"i-heroicons-arrow-down",disabled:t.form.routes.indexOf(l)===t.form.routes.length-1,onClick:u=>G(l)},null,8,["disabled","onClick"])):f("",!0),t.form.routes.length>1?(a(),h(n,{key:3,class:"",size:"lg",variant:"link",color:"gray",icon:"i-heroicons-arrow-up",disabled:t.form.routes.indexOf(l)===0,onClick:u=>F(l)},null,8,["disabled","onClick"])):f("",!0),y(n,{class:"",size:"lg",variant:"link",color:"gray",icon:"i-heroicons-code-bracket",to:`/strategies/${l.strategy}`},null,8,["to"])]))),128)),t.form.data_routes.length?(a(),h(g,{key:0,class:"mt-8 mb-4",title:"Data Routes"})):f("",!0),(a(!0),i(w,null,C(t.form.data_routes,(l,S)=>(a(),i("div",{key:l.symbol+S+l.timeframe,class:"flex mt-4"},[y(p,{modelValue:l.symbol,"onUpdate:modelValue":u=>l.symbol=u,query:d.value,"onUpdate:query":o[2]||(o[2]=u=>d.value=u),"clear-search-on-close":"",class:"w-full",ui:{rounded:"rounded-none rounded-l"},searchable:"",size:"lg",options:k.value,placeholder:"Select a symbol...",onChange:o[3]||(o[3]=u=>d.value="")},{empty:R(()=>[D("Start typing...")]),_:2},1032,["modelValue","onUpdate:modelValue","query","options"]),y(p,{modelValue:l.timeframe,"onUpdate:modelValue":u=>l.timeframe=u,class:"w-full",ui:{rounded:"rounded-none rounded-r"},size:"lg","value-attribute":"value",options:t.timeframes},null,8,["modelValue","onUpdate:modelValue","options"]),y(n,{size:"lg",variant:"link",color:"gray",icon:"i-heroicons-trash",onClick:u=>N(l)},null,8,["onClick"]),t.form.routes.length>1?(a(),h(n,{key:0,class:"",size:"lg",variant:"link",color:"gray",icon:"i-heroicons-document-duplicate",onClick:u=>P(l)},null,8,["onClick"])):f("",!0),t.form.data_routes.length>1?(a(),h(n,{key:1,class:"",size:"lg",variant:"link",color:"gray",icon:"i-heroicons-arrow-down",disabled:t.form.data_routes.indexOf(l)===t.form.data_routes.length-1,onClick:u=>Y(l)},null,8,["disabled","onClick"])):f("",!0),t.form.data_routes.length>1?(a(),h(n,{key:2,class:"",size:"lg",variant:"link",color:"gray",icon:"i-heroicons-arrow-up",disabled:t.form.data_routes.indexOf(l)===0,onClick:u=>W(l)},null,8,["disabled","onClick"])):f("",!0)]))),128))])}}}),me=["textContent"],ce=E({__name:"Tooltip",props:{title:{}},setup(_){const e=x(!1),k=()=>{e.value=!0},d=()=>{e.value=!1};return(r,v)=>(a(),i("span",{class:"relative underline",onMouseenter:k,onMouseleave:d},[te(c("span",{class:"absolute -top-10 z-90 bg-gray-900 rounded px-2 py-1 text-sm text-white",textContent:b(r.title)},null,8,me),[[oe,V(e)]]),re(r.$slots,"default")],32))}}),fe={class:"flex flex-col select-none"},pe={class:"-my-2 overflow-x-auto"},ge={class:"py-2 align-middle inline-block min-w-full"},ye={class:"border dark:border-gray-600 overflow-hidden sm:rounded"},he={class:"min-w-full divide-y divide-gray-200 dark:divide-gray-600 hide-scroll overflow-x-scroll"},ke={key:0,class:"bg-gray-100 dark:bg-gray-800 select-none"},be={key:1},_e=["textContent"],ve=["textContent"],xe=["textContent"],we={key:1},Ce=["textContent"],Re=["textContent"],Ee=["textContent"],Se={key:0,class:"text-center text-xs dark:bg-gray-700 py-4 opacity-30 dark:opacity-75 select-none"},Ue=E({__name:"MultipleValuesTable",props:{header:{type:Boolean},data:{},headerItems:{}},setup(_){return(e,k)=>{const d=ce;return a(),i("div",fe,[c("div",pe,[c("div",ge,[c("div",ye,[c("table",he,[e.header?(a(),i("thead",ke,[c("tr",null,[(a(!0),i(w,null,C(e.headerItems,r=>(a(),i("th",{key:r,scope:"col",class:"px-6 py-3 text-left text-xs font-bold text-gray-500 dark:text-gray-400"},b(r),1))),128))])])):f("",!0),e.data.length?(a(),i("tbody",be,[(a(!0),i(w,null,C(e.data,(r,v)=>(a(),i("tr",{key:v,class:z(["text-gray-900 dark:text-gray-200",v%2===0?"bg-white dark:bg-backdrop-dark":"bg-gray-50 dark:bg-gray-700"])},[(a(!0),i(w,null,C(r,(M,s)=>(a(),i("td",{key:s,class:z(["px-6 py-4 whitespace-nowrap text-sm font-medium",r[s].style])},[r[s].tooltip?(a(),h(d,{key:0,title:r[s].tooltip},{default:R(()=>[r[s].tag==="code"?(a(),i("code",{key:0,class:"rounded border dark:border-gray-600 bg-gray-50 dark:bg-gray-700 select-text text-sm dark:text-gray-300 w-full px-4 sm:px-6 py-2",textContent:b(r[s].value===0?"":r[s].value)},null,8,_e)):r[s].tag==="pre"?(a(),i("pre",{key:1,class:"whitespace-pre-line rounded border dark:border-gray-600 bg-gray-50 dark:bg-gray-700 select-text text-sm dark:text-gray-300 w-full px-4 sm:px-6 py-2",textContent:b(r[s].value===0?"":r[s].value)},null,8,ve)):(a(),i("span",{key:2,textContent:b(r[s].value===0?"":r[s].value)},null,8,xe))]),_:2},1032,["title"])):(a(),i("span",we,[r[s].tag==="code"?(a(),i("code",{key:0,class:"rounded border dark:border-gray-600 bg-gray-50 dark:bg-gray-700 select-text text-sm dark:text-gray-300 w-full px-4 sm:px-6 py-2",textContent:b(r[s].value===0?"":r[s].value)},null,8,Ce)):r[s].tag==="pre"?(a(),i("pre",{key:1,class:"whitespace-pre-line rounded border dark:border-gray-600 bg-gray-50 dark:bg-gray-700 select-text text-sm dark:text-gray-300 w-full px-4 sm:px-6 py-2",textContent:b(r[s].value===0?"":r[s].value)},null,8,Re)):(a(),i("span",{key:2,textContent:b(r[s].value===0?"":r[s].value)},null,8,Ee))]))],2))),128))],2))),128))])):f("",!0)]),e.data.length?f("",!0):(a(),i("div",Se," Empty List "))])])])])}}});export{ze as _,Te as a,Ue as b};
