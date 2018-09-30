def spilit_function(content, start_line=1, argument=None, punctuation="=", * , split="\n", rest_return=True):
    """
    このコマンドはdiscordのbotでコマンドラインを管理するのに向いています。
    ----------
    content: str
        discordで動かすことを想定しています。
        基本的にmessage.contentをそのまま投げてくれれば、コマンド部分のみを取り出し、
        コマンドではない部分(一般的に最後の引数の改行以降)はそのまま返されます。
    start_line: int
        引数の始まる行数を指定できます。
        ここに指定した行数以前のcontentは引数処理されません。
    punctuation: str
        引数に代入するときに利用していた文字です。デフォルトは「=」。
        この文字の左が戻り値のキー、右がアイテムとなります。
    argument: str, list, set, tuple
        ここに入力されたものを辞書のキーとして戻り値にします。
        指定がない場合は、punctuationに指定された文字が含まれるかどうかを上から順にすべてチェックし、
        含まれていれば引数のある行、として処理します。無くなり次第終わりにします。
    split: str
        引数の区切り文字です。デフォルトは改行。
        改行以外のおススメの引数は「|」。
    rest_return: bool
        最初の引数より前と、最後の引数後の区切り文字以降を返すかどうかを判別します。
        Trueの場合、キーを「rest_first」「rest_last」として出力します。
    ---------
    return: dict
        辞書形式で帰します。
    """
    return_dict = dict()
    content_list = content.split(split)
    if start_line >= 2:
        if rest_return:
            return_dict["rest_first"] = split.join(content_list[:(start_line - 1)])
        else:
            pass
        del content_list[:(start_line - 1)]
    else:
        pass
    if argument is None:
        num = 0
        for cl in content_list:
            if punctuation in cl:
                cll = cl.split(punctuation)
                return_dict[cll[0]] = punctuation.join(cll[1:])
                num += 1
            else:
                break
        del content_list[:num]
        if rest_return:
            return_dict["rest_last"] = split.join(content_list)
        else:
            pass
        return return_dict
    elif type(argument) is str:
        num = 1
        for cl in content_list:
            if argument in cl.split(punctuation):
                return_dict[argument] = punctuation.join(cl.split(punctuation)[1:])
                del content_list[:num]
                break
            else:
                num += 1
        if rest_return:
            return_dict["rest_last"] = split.join(content_list)
        else:
            pass
        return return_dict
    elif type(argument) in (list, set, tuple):
        num = 0
        num_else = 0
        for cl in content_list:
            cll = cl.split(punctuation)
            if cll[0] in argument:
                return_dict[cll[0]] = punctuation.join(cll[1:])
                num += 1
                num += num_else
                num_else = 0
            else:
                num_else += 1
        del content_list[:num_else]
        if rest_return:
            return_dict["rest_last"] = split.join(content_list)
        else:
            pass
        return return_dict
    else:
        return dict()
