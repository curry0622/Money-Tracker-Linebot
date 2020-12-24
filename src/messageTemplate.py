import datetime

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
                "text": "🐹Line 記帳包 主選單",
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
                "text": "🐹Line 記帳包 種類選單",
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

incomeTypeMenu = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://i.imgur.com/JTiY1GF.jpg",
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
                "text": "🐹Line 記帳包 種類選單",
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
                                "text": "請點選要記錄哪一類的收入喔~",
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
        "layout": "horizontal",
        "spacing": "sm",
        "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "薪資",
                            "text": "薪資"
                        },
                        "color": "#ffe89e",
                        "style": "secondary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "投資",
                            "text": "投資"
                        },
                        "color": "#ffe89e",
                        "style": "secondary"
                    }
                ],
                "spacing": "sm"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "獎金",
                            "text": "獎金"
                        },
                        "color": "#ffe89e",
                        "style": "secondary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "零用錢",
                            "text": "零用錢"
                        },
                        "color": "#ffe89e",
                        "style": "secondary"
                    }
                ],
                "spacing": "sm"
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

def checkMenu():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.datetime.now() - datetime.timedelta(1)).strftime("%Y-%m-%d")
    checkMenuTemplate = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/LaVF65q.jpg",
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
                            "text": "🐹Line 記帳包 單日查詢",
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "這裡可以查看單日的收支狀況",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1
                                },
                                {
                                    "type": "text",
                                    "text": "請選擇想查看的日期喔~",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1
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
                                    "style": "secondary",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "昨日收支",
                                        "text": yesterday
                                    },
                                    "color": "#ffe89e"
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "今日收支",
                                        "text": today
                                    },
                                    "color": "#ffe89e"
                                }
                            ],
                            "spacing": "sm"
                        },
                        {
                            "type": "button",
                            "style": "secondary",
                            "height": "sm",
                            "action": {
                                "type": "datetimepicker",
                                "label": "選擇日期",
                                "data": "date",
                                "mode": "date",
                                "initial": today,
                                "max": today
                            },
                            "color": "#ffe89e"
                        }
                    ],
                    "flex": 0
                }
            },
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/6aiNpIQ.jpg",
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
                            "text": "🐹Line 記帳包 本周查詢",
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "這裡可以查看這個禮拜的收支狀況",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1,
                                    "decoration": "none"
                                },
                                {
                                    "type": "text",
                                    "text": "請選擇想查看的種類喔~",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1
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
                                    "style": "secondary",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "收入結構",
                                        "text": "這個禮拜的收入結構"
                                    },
                                    "color": "#ffe89e"
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "支出結構",
                                        "text": "這個禮拜的支出結構"
                                    },
                                    "color": "#ffe89e"
                                }
                            ],
                            "spacing": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "收支比例",
                                        "text": "這個禮拜的收支比例"
                                    },
                                    "color": "#ffe89e"
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "各項金額",
                                        "text": "這個禮拜的各項金額"
                                    },
                                    "color": "#ffe89e"
                                }
                            ],
                            "spacing": "sm"
                        }
                    ],
                    "flex": 0
                }
            },
            {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/mPRMiHT.jpg",
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
                            "text": "🐹Line 記帳包 本月查詢",
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "這裡可以查看這個月的收支狀況",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1
                                },
                                {
                                    "type": "text",
                                    "text": "請選擇想查看的種類喔~",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1
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
                                    "style": "secondary",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "收入結構",
                                        "text": "這個月的收入結構"
                                    },
                                    "color": "#ffe89e"
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "支出結構",
                                        "text": "這個月的支出結構"
                                    },
                                    "color": "#ffe89e"
                                }
                            ],
                            "spacing": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "收支比例",
                                        "text": "這個月的收支比例"
                                    },
                                    "color": "#ffe89e"
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "各項金額",
                                        "text": "這個月的各項金額"
                                    },
                                    "color": "#ffe89e"
                                }
                            ],
                            "spacing": "sm"
                        }
                    ],
                    "flex": 0
                }
            }
        ]
    }
    return checkMenuTemplate