import requests
import time
import json

url = "https://pcmap-api.place.naver.com/graphql"

params = [
    {
        "operationName":"getPlacesList",
        "variables":{
            "useReverseGeocode":True,
            "input":{
                "query":"서면 맛집",
                "start":2, # 목록 페이지
                "display":20, # 페이지당 사이즈
                "adult":False,
                "spq":False,
                "queryRank":"",
                "x":"129.11262030000262",
                "y":"35.1337156999989",
                "deviceType":"pcmap",
                "bounds":"129.11000246400624;35.10601973502577;129.11609644288808;35.16070055001714"
            },
            "isNmap":False,
            "isBounds":True,
            "reverseGeocodingInput":{
                "x":"128.926445",
                "y":"35.108129"
            }
        },
        "query":"query getPlacesList($input: PlacesInput, $isNmap: Boolean!, $isBounds: Boolean!, $reverseGeocodingInput: ReverseGeocodingInput, $useReverseGeocode: Boolean = false) {\n  businesses: places(input: $input) {\n    total\n    items {\n      id\n      name\n      normalizedName\n      category\n      detailCid {\n        c0\n        c1\n        c2\n        c3\n        __typename\n      }\n      categoryCodeList\n      dbType\n      distance\n      roadAddress\n      address\n      fullAddress\n      commonAddress\n      bookingUrl\n      phone\n      virtualPhone\n      businessHours\n      daysOff\n      imageUrl\n      imageCount\n      x\n      y\n      poiInfo {\n        polyline {\n          shapeKey {\n            id\n            name\n            version\n            __typename\n          }\n          boundary {\n            minX\n            minY\n            maxX\n            maxY\n            __typename\n          }\n          details {\n            totalDistance\n            arrivalAddress\n            departureAddress\n            __typename\n          }\n          __typename\n        }\n        polygon {\n          shapeKey {\n            id\n            name\n            version\n            __typename\n          }\n          boundary {\n            minX\n            minY\n            maxX\n            maxY\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      subwayId\n      markerId @include(if: $isNmap)\n      markerLabel @include(if: $isNmap) {\n        text\n        style\n        stylePreset\n        __typename\n      }\n      imageMarker @include(if: $isNmap) {\n        marker\n        markerSelected\n        __typename\n      }\n      oilPrice @include(if: $isNmap) {\n        gasoline\n        diesel\n        lpg\n        __typename\n      }\n      isPublicGas\n      isDelivery\n      isTableOrder\n      isPreOrder\n      isTakeOut\n      isCvsDelivery\n      hasBooking\n      naverBookingCategory\n      bookingDisplayName\n      bookingBusinessId\n      bookingVisitId\n      bookingPickupId\n      baemin {\n        businessHours {\n          deliveryTime {\n            start\n            end\n            __typename\n          }\n          closeDate {\n            start\n            end\n            __typename\n          }\n          temporaryCloseDate {\n            start\n            end\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      yogiyo {\n        businessHours {\n          actualDeliveryTime {\n            start\n            end\n            __typename\n          }\n          bizHours {\n            start\n            end\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      isPollingStation\n      hasNPay\n      talktalkUrl\n      visitorReviewCount\n      visitorReviewScore\n      blogCafeReviewCount\n      bookingReviewCount\n      streetPanorama {\n        id\n        pan\n        tilt\n        lat\n        lon\n        __typename\n      }\n      naverBookingHubId\n      bookingHubUrl\n      bookingHubButtonName\n      newOpening\n      newBusinessHours {\n        status\n        description\n        dayOff\n        dayOffDescription\n        __typename\n      }\n      coupon {\n        total\n        promotions {\n          promotionSeq\n          couponSeq\n          conditionType\n          image {\n            url\n            __typename\n          }\n          title\n          description\n          type\n          couponUseType\n          __typename\n        }\n        __typename\n      }\n      mid\n      __typename\n    }\n    optionsForMap @include(if: $isBounds) {\n      ...OptionsForMap\n      displayCorrectAnswer\n      correctAnswerPlaceId\n      __typename\n    }\n    searchGuide {\n      queryResults {\n        regions {\n          displayTitle\n          query\n          region {\n            rcode\n            __typename\n          }\n          __typename\n        }\n        isBusinessName\n        __typename\n      }\n      queryIndex\n      types\n      __typename\n    }\n    queryString\n    siteSort\n    __typename\n  }\n  reverseGeocodingAddr(input: $reverseGeocodingInput) @include(if: $useReverseGeocode) {\n    ...ReverseGeocodingAddr\n    __typename\n  }\n}\n\nfragment OptionsForMap on OptionsForMap {\n  maxZoom\n  minZoom\n  includeMyLocation\n  maxIncludePoiCount\n  center\n  spotId\n  keepMapBounds\n  __typename\n}\n\nfragment ReverseGeocodingAddr on ReverseGeocodingResult {\n  rcode\n  region\n  __typename\n}"
    }
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Content-Type": "application/json",
    "X-Wtm-Graphql": "eyJhcmciOiLri6QiLCJ0eXBlIjoicGxhY2UiLCJzb3VyY2UiOiJwbGFjZSJ9"
}

# json, data, params
resp = requests.post(url, headers=headers, json=params)
result = resp.json()
data = result[0]['data']['businesses']['items']
print(data)


for d in data:
    url = "https://pcmap-api.place.naver.com/graphql"

    params = [
    {
        "operationName":"getVisitorReviews",
        "variables":{
            "input":{
                "businessId": d['id'],
                "businessType":None,
                "item":"0",
                "bookingBusinessId": d['bookingBusinessId'],
                "page":1, # 리뷰 페이지
                "size":10, #페이지당 사이즈
                "isPhotoUsed":False,
                "includeContent":True,
                "getUserStats":True,
                "includeReceiptPhotos":True,
                "cidList":d['categoryCodeList'],
                "getReactions":True,
                "getTrailer":True
            },
            "id": d['id']
        },
        "query":"query getVisitorReviews($input: VisitorReviewsInput) {\n  visitorReviews(input: $input) {\n    items {\n      id\n      rating\n      author {\n        id\n        nickname\n        from\n        imageUrl\n        borderImageUrl\n        objectId\n        url\n        review {\n          totalCount\n          imageCount\n          avgRating\n          __typename\n        }\n        theme {\n          totalCount\n          __typename\n        }\n        isFollowing\n        followerCount\n        followRequested\n        __typename\n      }\n      body\n      thumbnail\n      media {\n        type\n        thumbnail\n        thumbnailRatio\n        class\n        videoId\n        videoOriginSource\n        trailerUrl\n        __typename\n      }\n      tags\n      status\n      visitCount\n      viewCount\n      visited\n      created\n      reply {\n        editUrl\n        body\n        editedBy\n        created\n        date\n        replyTitle\n        isReported\n        isSuspended\n        __typename\n      }\n      originType\n      item {\n        name\n        code\n        options\n        __typename\n      }\n      language\n      highlightOffsets\n      apolloCacheId\n      translatedText\n      businessName\n      showBookingItemName\n      bookingItemName\n      votedKeywords {\n        code\n        iconUrl\n        iconCode\n        displayName\n        __typename\n      }\n      userIdno\n      loginIdno\n      receiptInfoUrl\n      reactionStat {\n        id\n        typeCount {\n          name\n          count\n          __typename\n        }\n        totalCount\n        __typename\n      }\n      hasViewerReacted {\n        id\n        reacted\n        __typename\n      }\n      nickname\n      showPaymentInfo\n      visitKeywords {\n        category\n        keywords\n        __typename\n      }\n      __typename\n    }\n    starDistribution {\n      score\n      count\n      __typename\n    }\n    hideProductSelectBox\n    total\n    showRecommendationSort\n    itemReviewStats {\n      score\n      count\n      itemId\n      starDistribution {\n        score\n        count\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}"
    }
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Content-Type": "application/json",
        "X-Wtm-Graphql": "eyJhcmciOiLri6QiLCJ0eXBlIjoicGxhY2UiLCJzb3VyY2UiOiJwbGFjZSJ9"
    }

    resp = requests.post(url, headers=headers, json=params)
    result = resp.json()
    result = result[0]['data']['visitorReviews']['items']
    for r in result:
        print(r['body'])
    
    break

# import requests

# url = "https://map.naver.com/p/search/%EA%B0%95%EB%82%A8%EB%8C%80%EC%97%AD%20%EC%8B%9D%EB%8B%B9/place/36193085?c=15.00,0,0,0,dh&placePath=%3Fentry%253Dbmp"

# response = requests.get(url=url)

# html_text = response.text

# print(html_text)