(this["webpackJsonpcerebrate-gui"]=this["webpackJsonpcerebrate-gui"]||[]).push([[0],{198:function(e,a,t){e.exports=t(333)},203:function(e,a,t){},204:function(e,a,t){},236:function(e,a){},238:function(e,a){},249:function(e,a){},251:function(e,a){},278:function(e,a){},280:function(e,a){},281:function(e,a){},287:function(e,a){},289:function(e,a){},307:function(e,a){},309:function(e,a){},321:function(e,a){},324:function(e,a){},330:function(e,a,t){},331:function(e,a,t){},332:function(e,a,t){},333:function(e,a,t){"use strict";t.r(a);var n=t(0),r=t.n(n),l=t(15),o=t.n(l),s=(t(203),t(23)),i=t(24),p=t(26),c=t(25),u=(t(204),t(59)),d=t(336),m=t(31),y=t(84),f=t(337),g=function(e){Object(p.a)(t,e);var a=Object(c.a)(t);function t(e){var n;Object(s.a)(this,t),n=a.call(this,e);var r=e.tagPrefix;return n.tagPrefix=r,n}return Object(i.a)(t,[{key:"removePrefix",value:function(e){return 0!==e.indexOf(this.tagPrefix)?e:e.slice(this.tagPrefix.length)}},{key:"render",value:function(){var e=this,a=this.props,t=a.disabled,n=a.tagIntent,l=a.tags,o=a.selectedTags,s=a.setSelectedTags;return r.a.createElement(f.a,{createNewItemRenderer:function(e,a,t){return r.a.createElement(d.h,{active:a,onClick:t,text:e,key:e})},itemRenderer:function(a,t){var n=t.modifiers,l=t.handleClick;return n.matchesPredicate?r.a.createElement(d.h,{active:n.active,onClick:l,text:e.removePrefix(a),key:a}):null},itemPredicate:function(a,t,n,r){return 0===t.indexOf(e.tagPrefix)&&!o.includes(t)&&t.includes(a.toLocaleLowerCase("en-GB"))},initialContent:null,items:l,selectedItems:o.filter((function(a){return 0===a.indexOf(e.tagPrefix)})),createNewItemFromQuery:function(a){return e.tagPrefix+a},onItemSelect:function(e){o.includes(e)||(o.push(e),s(o))},resetOnSelect:!0,tagRenderer:function(a){return e.removePrefix(a)},tagInputProps:{disabled:t,onRemove:function(a,t,n){o.splice(o.indexOf(e.tagPrefix+a),1),s(o)},tagProps:{intent:n}},openOnKeyDown:!0,fill:!0,placeholder:"Tags..."})}}]),t}(r.a.Component),b=t(87),v=t.n(b),h=(t(327),t(17)),T=t.n(h),R=t(32),E=function(){for(var e=arguments.length,a=new Array(e),t=0;t<e;t++)a[t]=arguments[t];return console.log(a)},O=function(){var e=Object(R.a)(T.a.mark((function e(a){return T.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,new Promise((function(e){return setTimeout(e,a)}));case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})));return function(a){return e.apply(this,arguments)}}(),I=function(){var e=Object(R.a)(T.a.mark((function e(){var a,t,n,r,l=arguments;return T.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:for(a=l.length,t=new Array(a),n=0;n<a;n++)t[n]=l[n];if(E(t),!(t.length<1)){e.next=4;break}return e.abrupt("return");case 4:return e.next=6,O(200);case 6:r=t[0].replayId,L.onReplayLoadedListeners.forEach((function(e){return e.onReplayLoaded({replayId:r,replayTimestamp:1575909015,teams:["BobTheZealot","Jim Raynor"],playerTeam:null,opponentTeam:null,replayFileName:null,selectedTags:["game:fake_tag"],notes:"Some fake notes",force:!1})}));case 8:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),S=function(){var e=Object(R.a)(T.a.mark((function e(){var a,t,n,r=arguments;return T.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:for(a=r.length,t=new Array(a),n=0;n<a;n++)t[n]=r[n];return E(t),e.next=4,O(200);case 4:L.onReplayLoadedListeners.forEach((function(e){return e.onReplayLoaded({replayId:"SOME HASH VALUE",replayTimestamp:Math.floor(Date.now()/1e3),teams:["Tassadar","Artanis"],playerTeam:null,opponentTeam:null,replayFileName:null,selectedTags:["game:fake_tag_2"],notes:"This is the most recently played replay",force:!0})}));case 5:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),x=function(){var e=Object(R.a)(T.a.mark((function e(){var a,t,n,r,l,o,s,i=arguments;return T.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:for(a=i.length,t=new Array(a),n=0;n<a;n++)t[n]=i[n];if(E(t),!(t.length<1)){e.next=4;break}return e.abrupt("return");case 4:return e.next=6,O(200);case 6:r=t[0],l=r.replayId,o=r.playerTeam,s=r.opponentTeam,L.onReplayLoadedListeners.forEach((function(e){return e.onReplayLoaded({replayId:l,replayTimestamp:1575909015,teams:["BobTheZealot","Jim Raynor"],playerTeam:o,opponentTeam:s,replayFileName:null,selectedTags:["game:fake_tag"],notes:"Some fake notes",force:!1})}));case 8:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),w=function(){var e=Object(R.a)(T.a.mark((function e(){var a,t,n,r,l=arguments;return T.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:for(a=l.length,t=new Array(a),n=0;n<a;n++)t[n]=l[n];if(E(t),!(t.length<1)){e.next=4;break}return e.abrupt("return");case 4:return r=t[0].replayId,e.next=7,O(500);case 7:L.onReplayUpdatedListeners.forEach((function(e){return e.onReplayUpdated({success:!0,replayId:r})}));case 8:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),L={selectReplay:function(){return(self&&self.selectReplay||I).apply(void 0,arguments)},selectMostRecentReplay:function(){return(self&&self.selectMostRecentReplay||S).apply(void 0,arguments)},selectPlayerOpponent:function(){return(self&&self.selectPlayerOpponent||x).apply(void 0,arguments)},updateReplayInfo:function(){return(self&&self.updateReplayInfo||w).apply(void 0,arguments)},onReplayLoadedListeners:[],onReplayUpdatedListeners:[]};window.replayLoaded=function(){var e=Object(R.a)(T.a.mark((function e(a){return T.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:L.onReplayLoadedListeners.forEach((function(e){return e.onReplayLoaded(a)}));case 1:case"end":return e.stop()}}),e)})));return function(a){return e.apply(this,arguments)}}(),window.replayUpdated=function(){var e=Object(R.a)(T.a.mark((function e(a){return T.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,O(500);case 2:L.onReplayUpdatedListeners.forEach((function(e){return e.onReplayUpdated(a)}));case 3:case"end":return e.stop()}}),e)})));return function(a){return e.apply(this,arguments)}}();var k=L,P=(t(330),function(e){Object(p.a)(t,e);var a=Object(c.a)(t);function t(e){var n;return Object(s.a)(this,t),(n=a.call(this,e)).state={valid:!0,disabled:!1},n}return Object(i.a)(t,[{key:"render",value:function(){var e=this,a=this.props,t=a.replayFileName,n=a.setReplayId,l=a.setReplayFileName,o=a.setReplayData,s=a.resetAndDisableForm,i=Object(u.a)(a,["replayFileName","setReplayId","setReplayFileName","setReplayData","resetAndDisableForm"]);return r.a.createElement("div",{className:"ReplaySelector-container"},r.a.createElement(d.c,Object.assign({disabled:this.state.disabled,text:t||"Choose replay file...",onInputChange:function(a){var t=a.target.value;if(t&&a.target.files){var r=a.target.files[0];e.setState({disabled:!0}),l(function(e){return e.split("\\").pop().split("/").pop()}(t)),s();var i=new FileReader;i.addEventListener("load",(function(a){var t=a.target.result,l=v.a.SHA256(v.a.lib.WordArray.create(t)).toString();n(l);var s=new FileReader;s.addEventListener("load",(function(a){var t=a.target.result;o(t),e.setState({disabled:!1}),k.selectReplay({replayId:l,replayData:t})})),s.readAsDataURL(r)})),i.readAsArrayBuffer(r)}},inputProps:{accept:".sc2replay"}},i)),r.a.createElement(d.a,{className:"ReplaySelector-button",text:"Most recent replay",onClick:function(e){s(),k.selectMostRecentReplay()}}))}}]),t}(r.a.Component)),j=(t(331),function(e){Object(p.a)(t,e);var a=Object(c.a)(t);function t(){return Object(s.a)(this,t),a.apply(this,arguments)}return Object(i.a)(t,[{key:"onPlayerSelected",value:function(e){var a=this.props,t=a.replayId,n=a.teams,r=a.setPlayerTeam,l=a.setOpponentTeam,o=a.disableForm,s=parseInt(e.currentTarget.value);if(s<0)r(null);else{r(s);var i=s,p=null;if(2===n.length){var c=0===s?1:0;l(c),p=c}o(),k.selectPlayerOpponent({replayId:t,playerTeam:i,opponentTeam:p})}}},{key:"onOpponentSelected",value:function(e){var a=this.props,t=a.replayId,n=a.teams,r=a.setPlayerTeam,l=a.setOpponentTeam,o=a.disableForm,s=parseInt(e.currentTarget.value);if(s<0)l(null);else{l(s);var i=s,p=null;if(2===n.length){var c=0===s?1:0;r(c),p=c}o(),k.selectPlayerOpponent({replayId:t,playerTeam:p,opponentTeam:i})}}},{key:"render",value:function(){var e=this,a=this.props,t=a.formDisabled,n=a.teams,l=a.playerTeam,o=a.opponentTeam;return r.a.createElement("div",{className:"SelectPlayerAndOpponentInput-container"},r.a.createElement(d.d,{className:"SelectPlayerAndOpponentInput-form-group SelectPlayerAndOpponentInput-form-group-player",label:"Player"},r.a.createElement(d.e,{disabled:t,fill:!0,iconProps:{intent:m.a.SUCCESS},options:[{label:"Choose player...",value:"-1"}].concat(n.map((function(e,a){return{label:e,value:a.toString()}}))),value:null!==l?l.toString():"-1",onChange:function(a){return e.onPlayerSelected(a)}})),r.a.createElement(d.d,{className:"SelectPlayerAndOpponentInput-form-group",label:"Opponent"},r.a.createElement(d.e,{disabled:t,fill:!0,iconProps:{intent:m.a.DANGER},options:[{label:"Choose opponent...",value:"-1"}].concat(n.map((function(e,a){return{label:e,value:a.toString()}}))),value:null!==o?o.toString():"-1",onChange:function(a){return e.onOpponentSelected(a)}})))}}]),t}(r.a.Component));function D(e){var a=new Date(1e3*e);return a.toLocaleDateString()+" "+a.toLocaleTimeString()}function N(e){var a=e.replayTimestamp;return r.a.createElement(d.d,{label:"Replay date"},r.a.createElement(d.f,{disabled:!0,fill:!0,value:a&&D(a)}))}var C=function(e){var a=e.notes,t=e.submittingReplay,n=e.setNotes,l=e.updateReplayInfo,o=Object(u.a)(e,["notes","submittingReplay","setNotes","updateReplayInfo"]),s=o.replayId,i=o.formDisabled,p=o.playerTeam,c=o.opponentTeam,f=o.failedToTagReplay,b=o.failedToLoadReplay;return r.a.createElement("div",null,r.a.createElement("br",null),r.a.createElement(d.d,{label:"Replay ID"},r.a.createElement(d.f,{disabled:!0,fill:!0,value:s})),r.a.createElement(d.d,{label:"Replay file",intent:b?m.a.DANGER:null,helperText:b?"Failed to load replay, please select another or try again.":null},r.a.createElement(P,Object.assign({fill:!0},o))),r.a.createElement(N,o),r.a.createElement(j,o),r.a.createElement(d.d,{label:"Player tags"},r.a.createElement(g,Object.assign({},o,{disabled:i||null===p,tagPrefix:"player:",tagIntent:m.a.SUCCESS}))),r.a.createElement(d.d,{label:"Opponent tags"},r.a.createElement(g,Object.assign({},o,{disabled:i||null===c,tagPrefix:"opponent:",tagIntent:m.a.DANGER}))),r.a.createElement(d.d,{label:"Game tags"},r.a.createElement(g,Object.assign({},o,{disabled:i,tagPrefix:"game:",tagIntent:m.a.PRIMARY}))),r.a.createElement(d.d,{label:"Notes"},r.a.createElement(d.o,{fill:!0,disabled:i,value:a,onChange:function(e){return n(e.target.value)}})),r.a.createElement(d.d,{intent:f?m.a.DANGER:null,helperText:f?"Failed to save tags, please select another replay or try again.":null},r.a.createElement(d.a,{fill:!0,loading:t,intent:m.a.SUCCESS,disabled:i||null===p||null===c,onClick:l,icon:y.a.TAG},"Save tags")))},A=t(53),_=(t(332),function(e){Object(p.a)(t,e);var a=Object(c.a)(t);function t(e){var n;return Object(s.a)(this,t),(n=a.call(this,e)).state={navbarTabId:"Home"},n}return Object(i.a)(t,[{key:"render",value:function(){var e=this;return r.a.createElement(d.i,{className:"CerebrateNavbar-navbar"},r.a.createElement(d.i.Group,null,r.a.createElement(d.i.Heading,{className:"CerebrateNavbar-navbar-heading"},r.a.createElement("em",null,"Cerebrate - A StarCraft II Replay Manager"))),r.a.createElement(d.i.Group,{align:A.a.RIGHT},r.a.createElement(d.m,{animate:!0,id:"navbar",large:!0,selectedTabId:this.state.navbarTabId,onChange:function(a){return e.setState({navbarTabId:a})}},r.a.createElement(d.l,{id:"form",title:"Replay Details"}),r.a.createElement(d.l,{id:"search",title:"Find Replay"}))))}}]),t}(r.a.Component)),F=t(30),U=["player:terran","player:protoss","player:zerg","player:macro","player:all_in","player:2_base_all_in","player:mech","player:bio","player:stargate","player:twilight","player:dt","player:mass_pheonix","player:mass_void_ray","player:air_toss","player:cannon_rush","player:proxy_barracks","player:proxy_hatch","player:winner","player:loser","opponent:terran","opponent:protoss","opponent:zerg","opponent:macro","opponent:all_in","opponent:2_base_all_in","opponent:mech","opponent:bio","opponent:stargate","opponent:twilight","opponent:dt","opponent:mass_pheonix","opponent:mass_void_ray","opponent:air_toss","opponent:cannon_rush","opponent:proxy_barracks","opponent:proxy_hatch","opponent:winner","opponent:loser","game:zvp","game:zvt","game:zvz","game:tvz","game:tvp","game:tvt","game:pvt","game:pvz","game:pvp","game:short","game:long","game:basetrade"],G=function(e){Object(p.a)(t,e);var a=Object(c.a)(t);function t(e){var n;return Object(s.a)(this,t),(n=a.call(this,e)).state={replayId:"",replayFileName:"",replayTimestamp:null,replayData:"",teams:[],playerTeam:null,opponentTeam:null,selectedTags:[],formDisabled:!0,failedToLoadReplay:!1,failedToTagReplay:!1,submittingReplay:!1,notes:"",setReplayId:function(e){return n.setState({replayId:e})},setReplayFileName:function(e){return n.setState({replayFileName:e})},setReplayData:function(e){return n.setState({replayData:e})},setPlayerTeam:function(e){return n.setState({playerTeam:e})},setOpponentTeam:function(e){return n.setState({opponentTeam:e})},setSelectedTags:function(e){return n.setState({selectedTags:e})},setNotes:function(e){return n.setState({notes:e})},resetAndDisableForm:function(){return n.setState({failedToLoadReplay:!1,replayId:"",replayTimestamp:null,teams:[],playerTeam:null,opponentTeam:null,selectedTags:[],notes:"",formDisabled:!0})},disableForm:function(){return n.setState({formDisabled:!0})},updateReplayInfo:function(){n.setState({formDisabled:!0,submittingReplay:!0}),k.updateReplayInfo({replayId:n.state.replayId,replayData:n.state.replayData,selectedTags:n.state.selectedTags,playerTeam:n.state.playerTeam,opponentTeam:n.state.opponentTeam,notes:n.state.notes})}},n}return Object(i.a)(t,[{key:"componentDidMount",value:function(){k.onReplayLoadedListeners.push(this),k.onReplayUpdatedListeners.push(this)}},{key:"componentWillUnmount",value:function(){k.onReplayLoadedListeners.splice(k.onReplayLoadedListeners.indexOf(this),1),k.onReplayUpdatedListeners.splice(k.onReplayUpdatedListeners.indexOf(this),1)}},{key:"onReplayLoaded",value:function(e){var a=e.replayId,t=e.replayFileName,n=e.replayData,r=e.replayTimestamp,l=e.teams,o=e.playerTeam,s=e.opponentTeam,i=e.selectedTags,p=e.notes;e.force||this.state.replayId===a?this.setState({replayId:a,replayData:n||this.state.replayData,formDisabled:!1,submittingReplay:!1,failedToLoadReplay:!1,replayTimestamp:r,teams:l,playerTeam:o,opponentTeam:s,replayFileName:t||this.state.replayFileName,selectedTags:i,notes:p}):this.setState({formDisabled:!0,submittingReplay:!1,failedToLoadReplay:!0,replayId:"",teams:[],playerTeam:null,opponentTeam:null,replayTimestamp:null,selectedTags:[],notes:""})}},{key:"onReplayUpdated",value:function(e){var a=e.success,t=e.replayId;this.setState({submittingReplay:!1}),this.state.replayId===t&&this.setState({failedToTagReplay:!a,formDisabled:!1})}},{key:"render",value:function(){return r.a.createElement("div",{className:"App"},r.a.createElement(d.b,{interactive:!0,elevation:F.a.TWO,className:"App-card"},r.a.createElement(_,null),r.a.createElement(C,Object.assign({tags:U},this.state))))}}]),t}(r.a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(G,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[198,1,2]]]);
//# sourceMappingURL=main.e8ddb14b.chunk.js.map