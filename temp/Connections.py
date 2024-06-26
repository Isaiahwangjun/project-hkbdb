def get_temp():

    Connections_labels = {
        "顧問": "hasAdvisor",
        "表兄": "hasBiaoSyong",
        "兄弟": "hasBrother",
        "妹夫": "hasBrotherInLaw",
        "同學": "hasClassmate",
        "同事": "hasColleague",
        "堂兄弟": "hasCousin",
        "女兒": "hasDaughter",
        "後代": "hasDescendants",
        "父親": "hasFather",
        "岳父": "hasFatherInLaw",
        "長女": "hasFirstDaughter",
        "長子": "hasFirstSon",
        "友人": "hasFriend",
        "朋友關係": "hasFriendship",
        "祖父": "hasGrandFather",
        "祖母": "hasGrandMother",
        "孫": "hasGrandSon",
        "曾子孫": "hasGreatGrandSon",
        "工作關係": "hasHired",
        "丈夫": "hasHusband",
        "介紹人": "hasIntroducer",
        "親屬關係": "hasKinship",
        "認識": "hasKnown",
        "母親": "hasMother",
        "外孫": "hasMotherGrandSon",
        "姪子": "hasNephew",
        "姐姐": "hasOlderSister",
        "參與政治": "hasParticipatePolitics",
        "同遊": "hasProceededWith",
        "兒子": "hasSon",
        "女婿": "hasSonInLaw",
        "夫妻": "hasSpouse",
        "有幕僚": "hasStaffMemberWas",
        "學生": "hasStudent",
        "有下屬": "hasSubordinateWas",
        "贊助政治活動": "hasSupportedPolitics",
        "老師": "hasTeacher",
        "師生關係": "hasTeacherStudent",
        "妻子": "hasWife",
        "為…工作": "hasWorkFor",
        "雅集": "hasYaji",
        "弟弟": "hasYoungerBrother",
        "妹妹": "hasYoungerSister",
        "是...的顧問": "isAdvisorOf",
        "是....的表兄": "isBiaoSyongOf",
        "是...的妹夫": "isBrotherInLawOf",
        "是...的兄弟": "isBrotherOf",
        "是...的同學": "isClassmateOf",
        "是...的同事": "isColleagueOf",
        "是...的堂兄弟": "isCousinOf",
        "是...的女兒": "isDaughterOf",
        "是...的後代": "isDescendantsOf",
        "是...岳父": "isFatherInLawOf",
        "是...的父親": "isFatherOf",
        "是...的長女": "isFirstDaughterOf",
        "是...的長子": "isFirstSonOf",
        "友人": "isFriendOf",
        "是...的朋友關係": "isFriendshipOf",
        "是...的祖父": "isGrandFatherOf",
        "是...的祖母": "isGrandMotherOf",
        "是...的孫": "isGrandSonOf",
        "是...的曾子孫": "isGreatGrandSonOf",
        "是...的工作關係": "isHiredOf",
        "是...的丈夫": "isHusbandOf",
        "是...的介紹人": "isIntroducerOf",
        "是...的親屬關係": "isKinshipOf",
        "與...認識": "isKnownWith",
        "是...的外孫": "isMotherGrandSonOf",
        "是...的母親": "isMotherOf",
        "是...的姪子": "isNephewOf",
        "是...的姐姐": "isOlderSisterOf",
        "參與政治": "isParticipatePoliticsOf",
        "同遊": "isProceededWithBy",
        "是...的女婿": "isSonInLawOf",
        "是...的兒子": "isSonOf",
        "是...的夫妻": "isSpouseOf",
        "是...的幕僚": "isStaffMemberOf",
        "是...的學生": "isStudentOf",
        "是...的下屬": "isSubordinateOf",
        "被...贊助政治活動": "isSupportedPoliticsOf",
        "是...的老師": "isTeacherOf",
        "是...的師生關係": "isTeacherStudentOf",
        "是...的妻子": "isWifeOf",
        "有...為其工作": "isWorkBy",
        "雅集": "isYajiOf",
        "是...的弟弟": "isYoungerBrotherOf",
        "是...的妹妹": "isYoungerSisterOf",
        "關係備註": "relationRemarks",
        "原始資料": "source"
    }

    return Connections_labels