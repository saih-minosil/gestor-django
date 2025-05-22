
			function tooltipsPlugin(opts) {
				let seriestt;
				function init(u, opts, data) {
					let over = u.over;

					seriestt = opts.series.map((s, i) => {
						if (i == 0) return;	
						let tt = document.createElement("div");
						tt.className = "tooltip";
						tt.textContent = "Tooltip!";
						tt.style.pointerEvents = "none";
						tt.style.position = "absolute";
						tt.style.color = "rgb(0,0,0)";
						tt.style.borderColor = s.stroke;
						over.appendChild(tt);
						return tt;
					});

					function hideTips() {
						seriestt.forEach((tt, i) => {
							if (i == 0 || i>=5) return;
							tt.style.display = "none";
						});
					}

					function showTips() {
						seriestt.forEach((tt, i) => {
							if (i == 0) return;
							let s = u.series[i];
							tt.style.display = s.show ? null : "none";
						});
					}

					over.addEventListener("mouseleave", () => {
						if (!u.cursor._lock) {
						//	u.setCursor({left: -10, top: -10});
							hideTips();
						}
					});

					over.addEventListener("mouseenter", () => {
						showTips();
					});

					if (u.cursor.left < 0)
						hideTips();
					else
						showTips();
				}

				function setCursor(u) {
					const {left, top, idx} = u.cursor;

					opts?.cursorMemo?.set(left, top);

					tts=[]
					seriestt.forEach((tt, i) => {
						if (i == 0) return;
						let s = u.series[i];
						if (s.show) {
							let xVal,yVal;
							if(i<4){ //Tooltips de las series (1 al 4)
								xVal = u.data[0][idx];
								yVal = u.data[i][idx];								
								datetime=dateformat(xVal)
								var top = (yVal != null ? (Math.round(u.valToPos(yVal, s.scale))-tt.offsetHeight) : 9999) + "px";								
								if((yVal || yVal==0) && parseFloat(top) < 540){																	
									tt.innerHTML = datetime + "<br>" + s.tag+ " :" + yVal + " " + s.unidad;
									if(tt.style.display=="none"){
										tt.style.display = "block";									
									}
								}else{
									tt.style.display = "none";									
								}								
								tts.push({"top":parseInt(top),"obj":tt,"ind":i})
								var left = Math.round(u.valToPos(xVal, 'x'))
								var left_limit=window.innerWidth-200-tt.offsetWidth
								if(left>left_limit){									
									left=left_limit			
								}
								tt.style.left = left+"px"
							}
						}
					});					
					tts.sort((a, b) => a.top - b.top); //ordenar por la Y
					var height=tts[0].obj.offsetHeight
					if(tts[0])
						seriestt[tts[0].ind].style.top=tts[0].top+"px"
					if(tts[1])
						seriestt[tts[1].ind].style.top=tts[1].top+"px"
					if(tts[2]){
						if(seriestt[tts[2].ind])
							seriestt[tts[2].ind].style.top=tts[2].top+"px"
					}
					if(tts[1]){
						if(tts[1].top>tts[0].top-height && tts[1].top<tts[0].top+height){ //si el segundo tapa al primero
							var tp = tts[0].top+height
							seriestt[tts[1].ind].style.top=tp+"px"	//se posiciona debajo del primero
							tts[1].top=tp
						}
					}
					if(tts[2]){
						if(seriestt[tts[2].ind]){
							if((tts[2].top>tts[0].top-height && tts[2].top<tts[0].top+height)
							||(tts[2].top>tts[1].top-height && tts[2].top<tts[1].top+height)){ //si el tercero tapa acualquiera de los dos
								var tp = tts[1].top+height
								seriestt[tts[2].ind].style.top=tp+"px"
								tts[2].top=tp
							}
						}
					}
				}

				return {
					hooks: {
						init,
						setCursor,
						setScale: [
							(u, key) => {
								//console.log('setScale', key);
							}
						],
						setSeries: [
							(u, idx) => {
								//console.log('setSeries', idx);
							}
						],
					},
				};
			}

			// save/restore cursor and tooltip state across re-inits
			let cursLeft = -10;
			let cursTop = -10;

			const cursorMemo = {
				set: (left, top) => {
					cursLeft = left;
					cursTop = top;
				},
				get: () => ({left: cursLeft, top: cursTop}),
			};
			
		function dateformat(d){
			date=new Date(d*1000)
			cadena=date.getDate()+"-"+(date.getMonth()+1)+ " "+ date.getHours()+":"+date.getMinutes();
			return(cadena)
		}
		