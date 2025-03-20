
			function tooltipsPlugin(opts) {
				let cursortt;
				let seriestt;

				function init(u, opts, data) {
					console.log("Options: ")
					console.log(opts)
					let over = u.over;

					seriestt = opts.series.map((s, i) => {
						if (i == 0) return;	
						let tt = document.createElement("div");
						tt.className = "tooltip";
						tt.textContent = "Tooltip!";
						tt.style.pointerEvents = "none";
						tt.style.position = "absolute";
						//tt.style.background = "rgba(0,0,0,0.1)";
						tt.style.color = "rgb(0,0,0)";
						tt.style.borderColor = s.stroke;
						over.appendChild(tt);
						return tt;
					});
					console.log(seriestt);

					function hideTips() {
						//cursortt.style.display = "none";
						seriestt.forEach((tt, i) => {
							if (i == 0 || i>=5) return;
							tt.style.display = "none";
						});
					}

					function showTips() {
						//cursortt.style.display = null;
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
						//if(i>=4) return;	
						let s = u.series[i];
						if (s.show) {
							let xVal,yVal;
							if(i<5){ //Tooltips de las series (1 al 4)
								xVal = u.data[0][idx];
								yVal = u.data[i][idx];
								
								datetime=dateformat(xVal)
								if(yVal || yVal==0){																	
									tt.innerHTML = datetime + "<br>" + s.label+ " :" + yVal + " " + s.unidad;
									if(tt.style.display=="none"){
										tt.style.display = "block";
										console.log("Mostrando el tooltip "+i)
									}
								}else{
									tt.style.display = "none";
									console.log("Escondiendo el tooltip "+i)
								}
								var top = (yVal != null ? (Math.round(u.valToPos(yVal, s.scale))-tt.offsetHeight) : 9999) + "px";								
								tts.push({"top":parseInt(top),"obj":tt,"ind":i})
								var left = Math.round(u.valToPos(xVal, 'x'))
								var left_limit=window.innerWidth-200-tt.offsetWidth
								if(left>left_limit){									
									left=left_limit			
								}
								tt.style.left = left+"px"
							}
							else{ //"Tooltips" de las lineas de control (alertas)
								xVal = 0;
								yVal = u.data[i][0];
								//tt.textContent = s.label+'(' + yVal + ' '+s.unidad+')';
								tt.innerHTML = s.label+'(' + yVal + ' '+s.unidad+')';
								tt.style.left=0;
								if(i==5 || i==6){//Comrpbar si los tooltips de activacio,, prealerta y alerta se sobreponen (seran 5 y 6 con embalses)
									var ttn=tt.nextElementSibling //ttn es el siguiente									
									if(parseFloat(tt.style.top)>parseFloat(ttn.style.top) && parseFloat(tt.style.top)<parseFloat(ttn.style.top) + ttn.offsetHeight){
										console.log(i+1+ " esta delante de " + i)
										console.log(ttn)
										tt.style.left=parseFloat(ttn.style.left)+(ttn.offsetWidth)+"px"
									}
										//tt.style.top=(parseFloat(tt1.style.top)-tt1.offsetHeight)+"px"
									/*}else if(parseFloat(tt1.style.top)>parseFloat(tt.style.top) && parseFloat(tt.style.top)<parseFloat(tt1.style.top) +tt1.offsetHeight){//El 1 mas abajod el 2
										tt1.style.top=(parseFloat(tt.style.top)-tt.offsetHeight)+"px"
									}*/	
								} 
								//tt.style.left = Math.round(u.valToPos(xVal, 'x')) + "px";
								tt.style.top = (Math.round(u.valToPos(yVal, s.scale))-tt.offsetHeight) + "px";							
							}
							
						}
					});
					console.log(seriestt)
					tts.sort((a, b) => a.top - b.top); //ordenar por la Y
					var height=tts[0].obj.offsetHeight
					console.log(tts)
					console.log(height)
					seriestt[tts[0].ind].style.top=tts[0].top+"px"
					seriestt[tts[1].ind].style.top=tts[1].top+"px"
					seriestt[tts[2].ind].style.top=tts[2].top+"px"
					if(tts[1].top>tts[0].top-height && tts[1].top<tts[0].top+height){ //si el segundo tapa al primero
						var tp = tts[0].top+height
						console.log(tts[1].ind)
						seriestt[tts[1].ind].style.top=tp+"px"	//se posiciona debajo del primero
						tts[1].top=tp
						console.log("2 tapa")
						console.log(tts[0].top)
						console.log(tts[1].top)
						console.log(tp)
					}
					if((tts[2].top>tts[0].top-height && tts[2].top<tts[0].top+height)
					  ||(tts[2].top>tts[1].top-height && tts[2].top<tts[1].top+height)){ //si el tercero tapa acualquiera de los dos
						var tp = tts[1].top+height
						seriestt[tts[2].ind].style.top=tp+"px"
						tts[2].top=tp
						console.log("3 tapa")
					}
				}

				return {
					hooks: {
						init,
						setCursor,
						setScale: [
							(u, key) => {
								console.log('setScale', key);
							}
						],
						setSeries: [
							(u, idx) => {
								console.log('setSeries', idx);
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
			cadena=date.getDate()+"-"+date.getMonth()+ " "+ date.getHours()+":"+date.getMinutes();
			return(cadena)
		}
		