mainMenu = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://i.imgur.com/CjlM8XZ.jpg",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "🐹LINE 記帳包 主選單",
                "weight": "bold",
                "size": "xl",
                "style": "normal"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "請點選想使用的功能喔~",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 1
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
            {
                "type": "button",
                "style": "secondary",
                "height": "sm",
                "action": {
                    "type": "message",
                    "label": "查詢",
                    "text": "查詢"
                },
                "color": "#ffe89e"
            },
            {
                "type": "button",
                "style": "secondary",
                "height": "sm",
                "action": {
                    "type": "message",
                    "label": "記帳",
                    "text": "記帳"
                },
                "color": "#ffe89e"
            }
        ],
        "flex": 0
    }
}

actionMenu = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://i.imgur.com/8rSZUj7.jpg",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "🐹LINE 記帳包 收支選單",
                "weight": "bold",
                "size": "xl",
                "style": "normal"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "請點選要記錄收入還是支出喔~",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 1
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
            {
                "type": "button",
                "style": "secondary",
                "height": "sm",
                "action": {
                    "type": "message",
                    "label": "收入",
                    "text": "收入"
                },
                "color": "#ffe89e"
            },
            {
                "type": "button",
                "style": "secondary",
                "height": "sm",
                "action": {
                    "type": "message",
                    "label": "支出",
                    "text": "支出"
                },
                "color": "#ffe89e"
            }
        ],
        "flex": 0
    }
}

expenseTypeMenu = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://i.imgur.com/vUvOhk0.jpg",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "🐹LINE 記帳包 種類選單",
                "weight": "bold",
                "size": "xl",
                "style": "normal"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "請點選要記錄哪一類的支出喔~",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 1
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "食",
                            "text": "食"
                        },
                        "style": "secondary",
                        "color": "#ffe89e"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "衣",
                            "text": "衣"
                        },
                        "style": "secondary",
                        "color": "#ffe89e"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "住",
                            "text": "住"
                        },
                        "style": "secondary",
                        "color": "#ffe89e"
                    }
                ],
                "alignItems": "center",
                "justifyContent": "space-evenly",
                "paddingAll": "1%",
                "spacing": "10px"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "行",
                            "text": "行"
                        },
                        "style": "secondary",
                        "color": "#ffe89e"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "育",
                            "text": "育"
                        },
                        "style": "secondary",
                        "color": "#ffe89e"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "樂",
                            "text": "樂"
                        },
                        "style": "secondary",
                        "color": "#ffe89e"
                    }
                ],
                "alignItems": "center",
                "justifyContent": "space-evenly",
                "paddingAll": "1%",
                "spacing": "10px"
            }
        ],
        "flex": 0
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}