import{g as I,r as V,P as E,o as u,M as y,w as r,a as t,t as c,b as n,k as a,a4 as D,c as w,O as v,U as W,a5 as U,a6 as C,V as K,X as N,a7 as B,a8 as F,a9 as M,x as P,d as b,i as T,F as L,aa as G,ab as H,Z as O,ac as R}from"./Crvr41uX.js";import{_ as X}from"./tIZ0BYDc.js";import{_ as Z}from"./QcdhOkh-.js";import{u as z}from"./DbaDxTuc.js";import{S as J}from"./CgXrlsHy.js";const Q={class:"flex justify-between items-center mb-2"},Y={class:"text-xl font-bold"},ee={class:"text-sm text-gray-500 dark:text-gray-400"},ae={class:"mt-4"},te={class:"flex justify-between"},se=t("span",{class:"font-medium"},"API Key:",-1),ne={class:"flex justify-between"},le=t("span",{class:"font-medium"},"API Secret:",-1),oe={key:0},re={class:"flex justify-between"},ie=t("span",{class:"font-medium"},"API Passphrase:",-1),de={class:"flex justify-between"},ue=t("span",{class:"font-medium"},"Wallet Address:",-1),pe={class:"flex justify-between"},ce=t("span",{class:"font-medium"},"Stark Private Key:",-1),_e=I({__name:"ExchangeApiKey",props:{apiKey:{}},setup(S){const f=S,i=V(!1),e=V(!1),_=E();async function h(){e.value=!0;const{data:o,error:d}=await U("/exchange-api-keys/delete",{id:f.apiKey.id},!0);if(e.value=!1,d.value&&d.value.statusCode!==200){C(d);return}i.value=!1,K("success","API Key deleted successfully"),_.exchangeApiKeys=_.exchangeApiKeys.filter(x=>x.id!==f.apiKey.id)}return(o,d)=>{const x=N,A=B,s=F;return u(),y(s,{class:"mb-4 p-4 bg-white"},{default:r(()=>[t("div",Q,[t("h2",Y,c(o.apiKey.name)+" • "+c(o.apiKey.exchange),1),n(x,{icon:"i-heroicons-trash",color:"red",label:"Delete",variant:"link",onClick:d[0]||(d[0]=p=>i.value=!0)})]),t("p",ee,c(a(D)(o.apiKey.created_at).value),1),t("div",ae,[t("div",te,[se,t("span",null,c(o.apiKey.api_key),1)]),t("div",ne,[le,t("span",null,c(o.apiKey.api_secret),1)]),o.apiKey.exchange.startsWith("Dydx")||o.apiKey.exchange.startsWith("Apex")?(u(),w("div",oe,[t("div",re,[ie,t("span",null,c(o.apiKey.api_passphrase),1)]),t("div",de,[ue,t("span",null,c(o.apiKey.wallet_address),1)]),t("div",pe,[ce,t("span",null,c(o.apiKey.stark_private_key),1)])])):v("",!0)]),n(A,{modelValue:a(i),"onUpdate:modelValue":d[1]||(d[1]=p=>W(i)?i.value=p:null),title:"Delete API Key",description:`Are you sure you want to delete '${o.apiKey.name}' API key?`,type:"info"},{default:r(()=>[n(x,{variant:"solid",color:"red",class:"flex justify-center",label:"Delete",loading:a(e),onClick:h},null,8,["loading"])]),_:1},8,["modelValue","description"])]),_:1})}}}),me=t("p",null,[b(" Here you can add your API keys for various exchanges. API keys are used to connect your account to the exchange and allow the bot to trade on your behalf. "),t("br"),t("br"),b("Please note that for security reasons, once created, API keys cannot be modified or seen again. ")],-1),ye=t("br",null,null,-1),fe={class:"flex justify-end"},he={class:"mt-8"},xe={key:0},Ke=I({__name:"exchange-api-keys",setup(S){z({title:"Exchange API Keys"});const f=V(!1),i=E(),e=M({exchange:i.liveTradingExchangeNames[0],name:"",apiKey:"",apiSecret:"",apiPassphrase:"",walletAddress:"",stark_private_key:""}),_=P(()=>i.exchangeApiKeys),h=P(()=>e.exchange.startsWith("Dydx")||e.exchange.startsWith("Apex")),o=P(()=>e.exchange.startsWith("Dydx")||e.exchange.startsWith("Apex")?e.exchange&&e.apiKey&&e.apiSecret&&e.apiPassphrase&&e.walletAddress&&e.stark_private_key:e.exchange&&e.apiKey&&e.apiSecret);async function d(){if(!o.value){K("error","Please fill in all required fields");return}f.value=!0;const A={name:e.name,exchange:e.exchange,api_key:e.apiKey,api_secret:e.apiSecret};h.value&&(A.additional_fields={api_passphrase:e.apiPassphrase,wallet_address:e.walletAddress,stark_private_key:e.stark_private_key});const{data:s,error:p}=await U("/exchange-api-keys/store",A,!0);f.value=!1,p.value&&p.value.statusCode!==200&&C(p);const g=s.value;g.status==="success"?(K("success","Successfully added API key"),_.value.push(g.data),x()):g.status==="error"&&K("error",g.message)}function x(){e.exchange=i.liveTradingExchangeNames[0],e.name="",e.apiKey="",e.apiSecret="",e.apiPassphrase="",e.walletAddress="",e.stark_private_key=""}return(A,s)=>{const p=G,g=X,m=H,k=O,j=N,$=R,q=Z;return u(),y(J,null,{default:r(()=>[n(p,null,{default:r(()=>[b(" Exchange API Keys ")]),_:1}),me,ye,n($,{state:a(e),class:"space-y-4",onSubmit:d},{default:r(()=>[n(m,{label:"Exchange name:",required:""},{default:r(()=>[n(g,{modelValue:a(e).exchange,"onUpdate:modelValue":s[0]||(s[0]=l=>a(e).exchange=l),searchable:"",options:a(i).liveTradingExchangeNames},null,8,["modelValue","options"])]),_:1}),n(m,{label:"Name:",required:""},{default:r(()=>[n(k,{modelValue:a(e).name,"onUpdate:modelValue":s[1]||(s[1]=l=>a(e).name=l),type:"text",placeholder:"Give a name to this API key (e.g. subaccount1)"},null,8,["modelValue"])]),_:1}),n(m,{label:"API Key:",required:""},{default:r(()=>[n(k,{modelValue:a(e).apiKey,"onUpdate:modelValue":s[2]||(s[2]=l=>a(e).apiKey=l),placeholder:"Enter your API key here",type:"text"},null,8,["modelValue"])]),_:1}),n(m,{label:"API Secret:",required:""},{default:r(()=>[n(k,{modelValue:a(e).apiSecret,"onUpdate:modelValue":s[3]||(s[3]=l=>a(e).apiSecret=l),placeholder:"Enter your API secret here",type:"text"},null,8,["modelValue"])]),_:1}),a(h)?(u(),y(m,{key:0,label:"API Passphrase:",required:""},{default:r(()=>[n(k,{modelValue:a(e).apiPassphrase,"onUpdate:modelValue":s[4]||(s[4]=l=>a(e).apiPassphrase=l),placeholder:"Enter your API passphrase here",type:"text"},null,8,["modelValue"])]),_:1})):v("",!0),a(h)?(u(),y(m,{key:1,label:"Wallet Address:",required:""},{default:r(()=>[n(k,{modelValue:a(e).walletAddress,"onUpdate:modelValue":s[5]||(s[5]=l=>a(e).walletAddress=l),placeholder:"Enter your wallet address here",type:"text"},null,8,["modelValue"])]),_:1})):v("",!0),a(h)?(u(),y(m,{key:2,label:"Stark Private Key:",required:""},{default:r(()=>[n(k,{modelValue:a(e).stark_private_key,"onUpdate:modelValue":s[6]||(s[6]=l=>a(e).stark_private_key=l),placeholder:"Enter your Stark private key here",type:"text"},null,8,["modelValue"])]),_:1})):v("",!0),t("div",fe,[n(j,{type:"submit",icon:"i-heroicons-plus",class:"w-48 flex justify-center",label:"Create",loading:a(f),disabled:!a(o)},null,8,["loading","disabled"])])]),_:1},8,["state"]),t("div",he,[n(p,null,{default:r(()=>[b(" Previously Added "),a(_).length?(u(),w("span",xe,"("+c(a(_).length)+")",1)):v("",!0)]),_:1}),a(_).length?v("",!0):(u(),y(q,{key:0},{default:r(()=>[b(" No API keys added yet ")]),_:1})),(u(!0),w(L,null,T(a(_),l=>(u(),y(_e,{key:l.id,"api-key":l},null,8,["api-key"]))),128))])]),_:1})}}});export{Ke as default};
