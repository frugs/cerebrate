(this["webpackJsonpcerebrate-gui"]=this["webpackJsonpcerebrate-gui"]||[]).push([[0],{204:function(e,t,a){e.exports=a(337)},209:function(e,t,a){},210:function(e,t,a){},211:function(e,t,a){},243:function(e,t){},245:function(e,t){},256:function(e,t){},258:function(e,t){},285:function(e,t){},287:function(e,t){},288:function(e,t){},294:function(e,t){},296:function(e,t){},314:function(e,t){},316:function(e,t){},328:function(e,t){},331:function(e,t){},337:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),l=a(15),o=a.n(l),s=(a(209),a(37)),i=a(38),c=a(41),p=a(40),u=(a(210),a(59)),d=a(340),f=a(25),y=a(26),m=a(84),g=(a(211),a(341)),b=function(e){Object(c.a)(a,e);var t=Object(p.a)(a);function a(e){var n;Object(s.a)(this,a),n=t.call(this,e);var r=e.tagPrefix;return n.tagPrefix=r,n}return Object(i.a)(a,[{key:"removePrefix",value:function(e){return 0!==e.indexOf(this.tagPrefix)?e:e.slice(this.tagPrefix.length)}},{key:"render",value:function(){var e=this,t=this.props,a=t.tagIntent,n=t.tags,l=t.selectedTags,o=t.formDisabled,s=t.setSelectedTags;return r.a.createElement(g.a,{createNewItemRenderer:function(e,t,a){return r.a.createElement(d.h,{active:t,onClick:a,text:e})},itemRenderer:function(t,a){var n=a.modifiers,l=a.handleClick;return n.matchesPredicate?r.a.createElement(d.h,{active:n.active,onClick:l,text:e.removePrefix(t)}):null},itemPredicate:function(t,a,n,r){return 0===a.indexOf(e.tagPrefix)&&!l.includes(a)&&a.includes(t.toLocaleLowerCase("en-GB"))},initialContent:null,items:n,selectedItems:l.filter((function(t){return 0===t.indexOf(e.tagPrefix)})),createNewItemFromQuery:function(t){return e.tagPrefix+t},onItemSelect:function(e){l.includes(e)||(l.push(e),s(l))},resetOnSelect:!0,tagRenderer:function(t){return e.removePrefix(t)},tagInputProps:{disabled:o,onRemove:function(t,a,n){l.splice(l.indexOf(e.tagPrefix+t),1),s(l)},tagProps:{intent:a}},openOnKeyDown:!0,fill:!0,placeholder:"Tags..."})}}]),a}(r.a.Component),h=a(87),v=a.n(h),R=(a(334),a(19)),x=a.n(R),E=a(43),w=function(){for(var e=arguments.length,t=new Array(e),a=0;a<e;a++)t[a]=arguments[a];return console.log(t)},O=function(){var e=Object(E.a)(x.a.mark((function e(t){return x.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,new Promise((function(e){return setTimeout(e,t)}));case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),T=function(){var e=Object(E.a)(x.a.mark((function e(){var t,a,n,r,l=arguments;return x.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:for(t=l.length,a=new Array(t),n=0;n<t;n++)a[n]=l[n];if(w(a),!(a.length<1)){e.next=4;break}return e.abrupt("return");case 4:return e.next=6,O(200);case 6:r=a[0].replayId,L.onReplayLoadedListeners.forEach((function(e){return e.onReplayLoaded({replayId:r,replayFileName:null,selectedTags:["game:fake_tag"],notes:"Some fake notes",force:!1})}));case 8:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),I=function(){var e=Object(E.a)(x.a.mark((function e(){var t,a,n,r,l=arguments;return x.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:for(t=l.length,a=new Array(t),n=0;n<t;n++)a[n]=l[n];if(w(a),!(a.length<1)){e.next=4;break}return e.abrupt("return");case 4:return r=a[0].replayId,e.next=7,O(500);case 7:L.onReplayUpdatedListeners.forEach((function(e){return e.onReplayUpdated({success:!0,replayId:r})}));case 8:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),L={selectReplay:function(){return(self&&self.selectReplay||T).apply(void 0,arguments)},submitTaggedReplay:function(){return(self&&self.submitTaggedReplay||I).apply(void 0,arguments)},onReplayLoadedListeners:[],onReplayUpdatedListeners:[]};window.replayLoaded=function(){var e=Object(E.a)(x.a.mark((function e(t){return x.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,O(200);case 2:L.onReplayLoadedListeners.forEach((function(e){return e.onReplayLoaded(t)}));case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),window.replayUpdated=function(){var e=Object(E.a)(x.a.mark((function e(t){return x.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,O(500);case 2:L.onReplayUpdatedListeners.forEach((function(e){return e.onReplayUpdated(t)}));case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}();var S=L,k=function(e){Object(c.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(s.a)(this,a),(n=t.call(this,e)).state={valid:!0,disabled:!1},n}return Object(i.a)(a,[{key:"render",value:function(){var e=this,t=this.props,a=t.replayFileName,n=t.setReplayId,l=t.setReplayFileName,o=t.setReplayData,s=t.resetAndDisableForm,i=Object(u.a)(t,["replayFileName","setReplayId","setReplayFileName","setReplayData","resetAndDisableForm"]);return r.a.createElement(d.c,Object.assign({disabled:this.state.disabled,text:a||"Choose replay file...",onInputChange:function(t){var a=t.target.value;if(a&&t.target.files){var r=t.target.files[0];e.setState({disabled:!0}),l(function(e){return e.split("\\").pop().split("/").pop()}(a)),s();var i=new FileReader;i.addEventListener("load",(function(t){var a=t.target.result,l=v.a.SHA256(v.a.lib.WordArray.create(a)).toString();n(l);var s=new FileReader;s.addEventListener("load",(function(t){var a=t.target.result;o(a),e.setState({disabled:!1}),S.selectReplay({replayId:l,replayData:a})})),s.readAsDataURL(r)})),i.readAsArrayBuffer(r)}},inputProps:{accept:".sc2replay"}},i))}}]),a}(r.a.Component);var D=function(e){var t=e.replayId,a=e.notes,n=e.submittingReplay,l=e.setNotes,o=e.submitTaggedReplay,s=Object(u.a)(e,["replayId","notes","submittingReplay","setNotes","submitTaggedReplay"]),i=s.formDisabled,c=s.failedToTagReplay,p=s.failedToLoadReplay;return r.a.createElement(d.b,{interactive:!0,elevation:f.a.TWO,className:"SubmitReplayForm-card"},r.a.createElement(d.e,null,"Save replay tags"),r.a.createElement("br",null),r.a.createElement(d.d,{label:"Replay ID"},r.a.createElement(d.f,{disabled:!0,fill:!0,value:t})),r.a.createElement(d.d,{label:"Replay file",intent:p?y.a.DANGER:null,helperText:p?"Failed to load replay, please select another or try again.":null},r.a.createElement(k,Object.assign({fill:!0},s))),r.a.createElement(d.d,{label:"Player tags"},r.a.createElement(b,Object.assign({},s,{tagPrefix:"player:",tagIntent:y.a.SUCCESS}))),r.a.createElement(d.d,{label:"Opponent tags"},r.a.createElement(b,Object.assign({},s,{tagPrefix:"opponent:",tagIntent:y.a.DANGER}))),r.a.createElement(d.d,{label:"Game tags"},r.a.createElement(b,Object.assign({},s,{tagPrefix:"game:",tagIntent:y.a.PRIMARY}))),r.a.createElement(d.d,{label:"Notes"},r.a.createElement(d.l,{fill:!0,disabled:i,value:a,onChange:function(e){return l(e.target.value)}})),r.a.createElement(d.d,{intent:c?y.a.DANGER:null,helperText:c?"Failed to save tags, please select another replay or try again.":null},r.a.createElement(d.a,{fill:!0,loading:n,intent:y.a.SUCCESS,disabled:i,onClick:o,icon:m.a.TAG},"Save tags")))},j=["player:terran","player:protoss","player:zerg","player:macro","player:all_in","player:2_base_all_in","player:mech","player:bio","player:stargate","player:twilight","player:dt","player:mass_pheonix","player:mass_void_ray","player:air_toss","player:cannon_rush","player:proxy_barracks","player:proxy_hatch","player:winner","player:loser","opponent:terran","opponent:protoss","opponent:zerg","opponent:macro","opponent:all_in","opponent:2_base_all_in","opponent:mech","opponent:bio","opponent:stargate","opponent:twilight","opponent:dt","opponent:mass_pheonix","opponent:mass_void_ray","opponent:air_toss","opponent:cannon_rush","opponent:proxy_barracks","opponent:proxy_hatch","opponent:winner","opponent:loser","game:zvp","game:zvt","game:zvz","game:tvz","game:tvp","game:tvt","game:pvt","game:pvz","game:pvp","game:short","game:long","game:basetrade"],_=function(e){Object(c.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(s.a)(this,a),(n=t.call(this,e)).state={replayId:"",replayFileName:"",replayData:"",selectedTags:[],formDisabled:!0,failedToLoadReplay:!1,failedToTagReplay:!1,submittingReplay:!1,notes:"",setReplayId:function(e){return n.setState({replayId:e})},setReplayFileName:function(e){return n.setState({replayFileName:e})},setReplayData:function(e){return n.setState({replayData:e})},setSelectedTags:function(e){return n.setState({selectedTags:e})},setNotes:function(e){return n.setState({notes:e})},resetAndDisableForm:function(){return n.setState({failedToLoadReplay:!1,replayId:"",selectedTags:[],notes:"",formDisabled:!0})},submitTaggedReplay:function(){n.setState({formDisabled:!0,submittingReplay:!0}),S.submitTaggedReplay({replayId:n.state.replayId,replayData:n.state.replayData,selectedTags:n.state.selectedTags,notes:n.state.notes})}},n}return Object(i.a)(a,[{key:"componentDidMount",value:function(){S.onReplayLoadedListeners.push(this),S.onReplayUpdatedListeners.push(this)}},{key:"componentWillUnmount",value:function(){S.onReplayLoadedListeners.splice(S.onReplayLoadedListeners.indexOf(this),1),S.onReplayUpdatedListeners.splice(S.onReplayUpdatedListeners.indexOf(this),1)}},{key:"onReplayLoaded",value:function(e){var t=e.replayId,a=e.replayFileName,n=e.selectedTags,r=e.notes;e.force||this.state.replayId===t?this.setState({formDisabled:!1,submittingReplay:!1,failedToLoadReplay:!1,replayFileName:a||this.state.replayFileName,selectedTags:n,notes:r}):this.setState({formDisabled:!0,submittingReplay:!1,failedToLoadReplay:!0,replayId:"",selectedTags:[],notes:""})}},{key:"onReplayUpdated",value:function(e){var t=e.success,a=e.replayId;this.setState({submittingReplay:!1}),this.state.replayId===a&&this.setState({failedToTagReplay:!t,formDisabled:!1})}},{key:"render",value:function(){return r.a.createElement("div",{className:"App"},r.a.createElement(D,Object.assign({tags:j},this.state)))}}]),a}(r.a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(_,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[204,1,2]]]);
//# sourceMappingURL=main.bc44f542.chunk.js.map