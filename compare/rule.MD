計算公式 (accuracy)

* 完全匹配: 一模一樣才給分
* 是否包含: 只要答案與正解有一方包含在內，即得滿分，否則獲得相似分數
* 無序匹配: 以空格為斷行, 應用在如筆名 (多個答案放在 list, 順序不重要)

計算方式 (onlyGPT & onlyHKBDB)

* 一維資料，一欄位算一分
* 二維資料分兩種計分
  * 同一筆事件中多填的欄位，一欄位會根據表單的總欄位占比 (如 Education，共有 hasAcademicDegree, hasStartDate ... 七個欄位，所以一欄位佔 1/7 分
  * 若是直接多一整筆事件，加一分

compare flow

* 刪除空白的 sheet
* 判斷目前計算的 sheet 屬於一維還二維資料
  * 一維: 從 data&ans 取得 key 對應的值,
    * 若兩種都取到，計算相似度 (accuracy)
    * data 有, ans 沒有, 計算 onlyGPT
    * data 沒有, ans 有, 計算 onlyHKBDB
  * 二維: 因二維是由多個事件構成，彼此沒有順序, 直接比對可能會比錯筆資料
    如 data: 事件1  ans: 事件2
    * > 事件2         事件1
      >
    * 先找到 data 的關鍵欄位 (可能像是 rdfs:label)
    * 比對 ans 所有的關鍵欄位，以找到相關事件
    * 接著比對方法如一維資料
* 若有某一 excel 少對方 sheet, 走 onlyGPT or onlyHKBDB 計算
