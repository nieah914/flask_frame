  var searchParam = new Object();

  function save_btn_clicked() {
      searchParam = Object.assign(searchParam, self.setSendParam());
      self.service_store_insertDate(searchParam);
  }

  function setSendParam() {
          var param = new Object();
          param['district']	  	=$("input[name='district']").val();
          param['building_nm']    =$("input[name='building_nm']").val();
          param['hosu']    		=$("input[name='hosu']").val();
          param['category']       =$("input[name='category']").val();
          param['category_nm']    =$("input[name='category_nm']").val();
          param['maintance_cost'] =$("input[name='maintance_cost']").val();
          param['rent_py_rating'] =$("input[name='rent_py_rating']").val();
          param['real_py_size']   =$("input[name='real_py_size']").val();
          param['bun_py_size']    =$("input[name='bun_py_size']").val();
          param['real_py_raing']  =$("input[name='real_py_raing']").val();
          param['real_m2_size']   =$("input[name='real_m2_size']").val();
          param['bun_m2_size']    =$("input[name='bun_m2_size']").val();
          param['address']        =$("input[name='address']").val();
          param['public1']        =$("input[name='public1']").val();
          param['public2']        =$("input[name='public2']").val();
          param['public3']        =$("input[name='public3']").val();
          param['public4']        =$("input[name='public4']").val();
          param['public5']        =$("input[name='public5']").val();
          param['public6']        =$("input[name='public6']").val();
          param['public7']        =$("input[name='public7']").val();
          param['public_sum']     =$("input[name='public_sum']").val();
          param['floar']          =$("input[name='floar']").val();
          param['facing']         =$("input[name='facing']").val();
          param['lessor1']        =$("input[name='lessor1']").val();
          param['lessor2']        =$("input[name='lessor2']").val();
          param['lessor1_phone']  =$("input[name='lessor1_phone']").val();
          param['lessor2_phone']  =$("input[name='lessor2_phone']").val();
          param['sale_price']     =$("input[name='sale_price']").val();
          param['sale_py_rating'] =$("input[name='sale_py_rating']").val();
          param['lessor_add']     =$("input[name='lessor_add']").val();
  		  param['lessor_etc']    =$("textarea[name='lessor_etc']").val();

          param['lessee1']       =$("input[name='lessee1']").val();
          param['lessee2']       =$("input[name='lessee2']").val();
          param['lessee1_phone'] =$("input[name='lessee1_phone']").val();
          param['lessee2_phone'] =$("input[name='lessee2_phone']").val();
          param['move_in_dt']    =$("input[name='move_in_dt']").val();
          param['right_money']   =$("input[name='right_money']").val();
          param['h1']            =$("input[name='h1']").val();
          param['h2']            =$("input[name='h2']").val();
          param['brand_nm']      =$("input[name='brand_nm']").val();
          param['sector1']       =$("input[name='sector1']").val();
          param['sector2']       =$("input[name='sector2']").val();
          param['deposit']       =$("input[name='deposit']").val();
          param['monthly']       =$("input[name='monthly']").val();
          param['right_money']   =$("input[name='right_money']").val();
          param['lessee_etc']    =$("textarea[name='lessee_etc']").val();
  		param['recomend1']    =$("input[name='recomend1']").val();
  		param['recomend2']    =$("input[name='recomend2']").val();
  		param['recomend3']    =$("input[name='recomend3']").val();
  		param['park']    =$("input[name='park']").val();
		   param['maintance_py_cost'] =$("input[name='maintance_py_cost']").val();
           param['mamul_character']         =$("input[name='mamul_character']").val();
           param['sale_dt']           =$("input[name='sale_dt']").val();
           param['move_possible_dt']  =$("input[name='move_possible_dt']").val();
           param['total_cost']        =$("input[name='total_cost']").val();
           param['monthly_py']        =$("input[name='monthly_py']").val();
           param['profit_rate']       =$("input[name='profit_rate']").val();
           param['reg_change_dt']     =$("input[name='reg_change_dt']").val();



          return param;
      }


  function loadDatas(data) {
           $("input[name='district']").val(data.district);
           $("input[name='building_nm']").val(data.building_nm);
           $("input[name='hosu']").val(data.hosu);

           $("#category_nm").val(data.category).prop("selected", true); //값이 1인 option 선택
           $("#category_cd").val(data.category_nm).prop("selected", true); //값이 1인 option 선택


           $("input[name='maintance_cost']").val(data.maintance_cost);
           $("input[name='rent_py_rating']").val(data.rent_py_rating);
           $("input[name='real_py_size']").val(data.real_py_size);
           $("input[name='bun_py_size']").val(data.bun_py_size);
           $("input[name='real_py_raing']").val(data.real_py_raing);
           $("input[name='real_m2_size']").val(data.real_m2_size);
           $("input[name='bun_m2_size']").val(data.bun_m2_size);
           $("input[name='address']").val(data.address);
           $("input[name='public1']").val(data.public1);
           $("input[name='public2']").val(data.public2);
           $("input[name='public3']").val(data.public3);
           $("input[name='public4']").val(data.public4);
           $("input[name='public5']").val(data.public5);
           $("input[name='public6']").val(data.public6);
           $("input[name='public7']").val(data.public7);
           $("input[name='public_sum']").val(data.public_sum);

           $("input[name='floar']").val(data.floar);
           $("input[name='facing']").val(data.facing);
           $("input[name='lessor1']").val(data.lessor1);
           $("input[name='lessor2']").val(data.lessor2);
           $("input[name='lessor1_phone']").val(data.lessor1_phone);
           $("input[name='lessor2_phone']").val(data.lessor2_phone);
           $("input[name='sale_price']").val(data.sale_price);
           $("input[name='sale_py_rating']").val(data.sale_py_rating);
           $("input[name='lessor_add']").val(data.lessor_add);
  		 $("textarea[name='lessor_etc']").val(data.lessor_etc);


          $("input[name='lessee1']").val(data.lessee1);
          $("input[name='lessee2']").val(data.lessee2);
          $("input[name='lessee1_phone']").val(data.lessee1_phone);
          $("input[name='lessee2_phone']").val(data.lessee2_phone);
          $("input[name='lessee_add']").val(data.lessee_add);
          $("input[name='move_in_dt']").val(data.move_in_dt);
          $("input[name='h1']").val(data.h1);
          $("input[name='h2']").val(data.h2);
           $("input[name='brand_nm']").val(data.brand_nm);
           $("input[name='sector1']").val(data.sector1);
           $("input[name='sector2']").val(data.sector2);
  		 $("input[name='recomend1']").val(data.recomend1);
           $("input[name='recomend2']").val(data.recomend2);
  		 $("input[name='recomend3']").val(data.recomend3);
  		 $("input[name='park']").val(data.park);
           $("input[name='deposit']").val(data.deposit);
           $("input[name='monthly']").val(data.monthly);
           $("input[name='right_money']").val(data.right_money);
           $("textarea[name='lessee_etc']").val(data.lessee_etc);

		   $("input[name='right_money']").val(data.right_money);
		   $("input[name='right_money']").val(data.right_money);
		   $("input[name='right_money']").val(data.right_money);
		   $("input[name='right_money']").val(data.right_money);

		   $("input[name='maintance_py_cost']").val(data.maintance_py_cost);
           $("input[name='mamul_character']").val(data.mamul_character);
           $("input[name='sale_dt']").val(data.sale_dt);
           $("input[name='move_possible_dt']").val(data.move_possible_dt);
           $("input[name='total_cost']").val(data.total_cost);
           $("input[name='monthly_py']").val(data.monthly_py);
           $("input[name='profit_rate']").val(data.profit_rate);
           $("input[name='reg_change_dt']").val(data.reg_change_dt);



      }

  function service_lessee_updateDate(filter) {
      console.log("데이터를 가지고 오고 시자합니다.");
      console.log(filter);
      return $.ajax({
          type: "PUT"
          , url: "/lessee_detail"
          , data: filter
          , dataType: "json"
          , success: function (data) {
              alert("저장되었습니다.");
              opener.parent.test();
              self.close();   //자기자신창을 닫습니다.
              //부모창 함수를 호출한다.

          }
          , error: function (request,status,error) {
              //status 200은 정상이기 때문에 예외처리함.
              alert(error);
              if(request.status != '200')
                  alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
          }
          , complete: function () {  console.log('complete'); }
      });
  }
















  function service_lessor_updateDate(filter) {
      console.log("데이터를 가지고 오고 시자합니다.");
      console.log(filter);
      return $.ajax({
          type: "PUT"
          , url: "/lessor_detail"
          , data: filter
          , dataType: "json"
          , success: function (data) {
              console.log("lessor 데이터를 저장함.");
              service_lessee_updateDate(filter);
          }
          , error: function (request,status,error) {
              //status 200은 정상이기 때문에 예외처리함.
              alert(error);
              if(request.status != '200')
                  alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
          }
          , complete: function () {  console.log('complete'); }
      });
  }


  function service_store_insertDate(filter) {
      console.log("데이터를 가지고 오고 시자합니다.");
      console.log(filter);
      var date = new Date();
      filter.today = getFormatDate(date);
      console.log(filter)
      return $.ajax({
          type: "PUT"
          , url: "/mamul_detail/insert"
          , data: filter
          , dataType: "json"
          , success: function (data) {
              console.log("store 데이터를 저장함.");
              service_store_updateDate(filter);
          }
          , error: function (request,status,error) {
              //status 200은 정상이기 때문에 예외처리함.
              alert(error);
              if(request.status != '200')
                  alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
          }
          , complete: function () {  console.log('complete'); }
      });
  }

  function service_store_updateDate(filter) {
      console.log("데이터를 가지고 오고 시자합니다.");
      console.log(filter);
      var date = new Date();
      filter.today = getFormatDate(date);
      console.log(filter)
      return $.ajax({
          type: "PUT"
          , url: "/mamul_detail"
          , data: filter
          , dataType: "json"
          , success: function (data) {
              console.log("store 데이터를 저장함.");
              service_lessor_updateDate(filter);
          }
          , error: function (request,status,error) {
              //status 200은 정상이기 때문에 예외처리함.
              alert(error);
              if(request.status != '200')
                  alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
          }
          , complete: function () {  console.log('complete'); }
      });
  }
  function getFormatDate(date){
      var year = date.getFullYear();              //yyyy
      var month = (1 + date.getMonth());          //M
      month = month >= 10 ? month : '0' + month;  //month 두자리로 저장
      var day = date.getDate();                   //d
      day = day >= 10 ? day : '0' + day;          //day 두자리로 저장
      return  year + '' + month + '' + day;       //'-' 추가하여 yyyy-mm-dd 형태 생성 가능
  }
  function service_store_getData(filter) {
      console.log("데이터를 가지고 오고 시자합니다.");
      console.log(filter);
      return $.ajax({
          type: "GET"
          , url: "/mamul_detail"
          , data: filter
          , dataType: "json"
          , success: function (data) {
              console.log('success');
              console.log(data);
  			if(typeof data.length == "undefined" || data.length == null || data.length == "") {
  				document.getElementById('id_district').readOnly  = false;
  				document.getElementById('id_building_nm').readOnly  = false;
  				document.getElementById('id_hosu').readOnly  = false;
  			}
  			else
  				loadDatas(data[0]);
          }
          , error: function (request,status,error) {
              //status 200은 정상이기 때문에 예외처리함.
              alert(error);
              if(request.status != '200')
                  alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
          }
          , complete: function () {  console.log('complete'); }
      });
  }
  function getParam(param) {
      return new URLSearchParams(window.location.search).get(param);
  }

  function service_store_getImage(filter) {
      console.log("데이터를 가지고 오고 시자합니다.");
      console.log(filter);
      return $.ajax({
          type: "GET"
          , url: "/store_image"
          , data: filter
          , dataType: "json"
          , success: function (data) {

              for(var i = 0; i < data.length; i++) {
                  var Ul = document.getElementById("images");
                  var newLi = document.createElement("li");
                  var newSpan = document.createElement("span");
                  var newImg = document.createElement('img');
                  newImg.src=data[i].path;
                  newImg.setAttribute('data-large-src', data[i].path);
                  newImg.setAttribute('alt', data[i].file_nm);
                  newLi.appendChild(newImg);
                  Ul.appendChild(newLi);
              }

              var slideshow = $(".pgwSlideshow").pgwSlideshow({
                mainClassName: 'pgwSlideshow',
                transitionEffect: 'fading',
                autoSlide: false,
                maxHeight: null,
                listPosition : 'center',
                displayControls : false,
                afterSlide: function(){
                  var counter = slideshow.getCurrentSlide();
                  if (counter === 1){
                   console.log("this is number one!");

                   var x = document.getElementsByClassName("ps-current");
                   x.setAttribute('style', 'height: 382.5px;');
                   // add google map code for number one here
                  }
                  else
                  {
                   console.log("something else");
                  }
                }
              });
          }
          , error: function (request,status,error) {
              //status 200은 정상이기 때문에 예외처리함.
              alert(error);
              if(request.status != '200')
                  alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
          }
          , complete: function () {  console.log('complete'); }
      });
  }




  function service_common_getData(filter) {
      console.log("데이터를 가지고 오고 시자합니다.");
      console.log(filter);
      return $.ajax({
          type: "GET"
          , url: "/common/detailCode"
          , data: filter
          , dataType: "json"
          , success: function (data) {
              console.log('success');
              console.log(data);

              var TTYPE = data;
              for(var count = 0; count < TTYPE.length; count++){
                  //매물방식
                  if(TTYPE[count]['group_cd'] == 'M02') {
                      console.log(TTYPE[count]);
                      var option = $("<option value=" + TTYPE[count]['code_nm'] + ">" + TTYPE[count]['code_cd'] + "</option>");
                      var option2 = $("<option value=" + TTYPE[count]['code_cd'] + ">" + TTYPE[count]['code_nm'] + "</option>");

                      $('#category_cd').append(option);
                      $('#category_nm').append(option2);

                  }
               }
               loading();


          }
          , error: function (request,status,error) {
              //status 200은 정상이기 때문에 예외처리함.
              alert(error);
              if(request.status != '200')
                  alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
          }
          , complete: function () {  console.log('complete');


           }
      });
  }


  function loading() {
      var param = new Object();
      param.building_nm = getParam("arg1");
      param.distict = getParam("arg2");
      param.distict = getParam("arg2");
      param.hosu = getParam("arg3");
      service_store_getData(param);
      service_store_getImage(param);
  }

  window.onload = function(){
      console.log(getParam("arg1"));
      console.log(getParam("arg2"));
      var param = new Object();
      service_common_getData(param);


      $("#category_nm").change( function() {
          //TODO
          searchParam['category'] = $("#category_nm option:selected").val();
          alert(searchParam['category']);
      });

  }


	$(function () {
		$("#jsGrid").jsGrid({
			width: "100%",
			height: "700",
			inserting: false,
			sorting: true,
			paging: false,
			autoload: false,

			rowClick: function(args) {
				if(args.event.target.className == "my-row-custom-class jsgrid-cell jsgrid-align-center") {
					albumCalculateInfo.btn_popup_clicked(args)
				}
				// 클릭 클릭시
				/*
				if(args.item.item_desc)

					*/
			},

			controller: {
				loadData: function(filter) {
						for(let i in filter) {
							console.log(filter[i])
							if(filter[i] == '')
								delete filter[i];
						}
						return $.ajax({
							type: "GET"
							, url: "/test2"
							, data: filter
							, dataType: "json"
							, success: function () {  console.log('success'); }
							, error: function (request,status,error) {
								//status 200은 정상이기 때문에 예외처리함.
								alert(error);
								if(request.status != '200')
									alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
							}
							, complete: function (data) {
								console.log('complete');
								console.log(data.responseJSON.length);
								var row_num = data.responseJSON.length;
								if(!data.responseJSON.length)
									row_num = "0";
								document.getElementById("output1").value = row_num;
							}
						});

				},
				updateItem: function(item) {
					var d = $.Deferred();
					console.log(item);
					$.ajax({
						url: "/api/database",
						data: JSON.stringify(item),
						type: "PUT",
						dataType: "json",
						contentType: "application/json",
					}).done(function(response) {
						d.resolve(response);
					});
					return d.promise();
				},
				deleteItem: function(item) {
					var d = $.Deferred();
					$.ajax({
						url: "/api/database",
						data: item,
						type: "DELETE",
					}).done(function(response) {
						d.resolve(response);
					});
					return d.promise();
				},
				insertItem: function(item) {
					var d = $.Deferred();
					$.ajax({
						url: "/api/database",
						data: JSON.stringify(item),
						dataType: "json",
						contentType: "application/json",
						type: "POST",
					}).done(function(response) {
						d.resolve(response);
					});
					return d.promise();
				},


			},

			fields: [
				{ name: "item_desc",     type: "text",     title: "상세보기",   align: "center" , width: 80,
				  cellRenderer:
					function(item, value){
					  return $("<td>").addClass("my-row-custom-class").append(item);
					},
				   itemTemplate: function (value, item) {
						console.log("itemTemplate");
						console.log(value);
						console.log(item);
						return  value;
					}
				},
				{ name: "district",      type: "text",     width: 100, validate: "required" ,title:"권역별"},
				{ name: "building_nm",   type: "text",     width: 100, validate: "required" ,title:"빌딩명"},
				{ name: "hosu",          type: "text",     width: 80, validate: "required" ,title:"호수"},
				{ name: "category_nm",   type: "text",     width: 80, validate: "required" ,title:"매물방식"},
				{ name: "rec_dt",        type: "text",     width: 80, validate: "required" ,title:"접수일자"},
				{ name: "brand_nm",      type: "text",     width: 150, validate: "required" ,title:"상호명"},
				{ name: "move_in_dt",   type: "text",     width: 80, validate: "required" ,title:"입주일"},
				{ name: "bun_py_size",   type: "text",     width: 80, validate: "required" ,title:"분양(평)"},
				{ name: "real_py_size",  type: "text",     width: 80, validate: "required" ,title:"전용(평)"},
				{ name: "sale_price",    type: "text",     width: 60, validate: "required" ,title:"매매가"},
				{ name: "deposit",       type: "text",     width: 60, validate: "required" ,title:"보증금"},
				{ name: "monthly",       type: "text",     width: 60, validate: "required" ,title:"월세"},
				{ name: "right_money",   type: "text",     width: 60, validate: "required" ,title:"권리금"},
				{ name: "maintance_cost",type: "text",     width: 60, validate: "required" ,title:"관리비"},
				{ name: "total_cost"    ,type: "text",     width: 60, validate: "required" ,title:"총비용"},
				{ name: "bun_m2_size",   type: "text",     width: 80, validate: "required" ,title:"분양(M2)"},
				{ name: "real_m2_size",  type: "text",     width: 80, validate: "required" ,title:"전용(M2)"},
				{ name: "lessor1",       type: "text",     width: 80, validate: "required" ,title:"소유자"},
				{ name: "address",       type: "text",     width: 150, validate: "required" ,title:"주소"},
				{
					type: "control",
					modeSwitchButton: false,
					editButton: false,
					deleteButton:false
				}


			]
		});
	});


