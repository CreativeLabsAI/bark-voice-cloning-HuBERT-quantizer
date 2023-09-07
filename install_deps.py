from bark_hubert_quantizer.hubert_manager import HuBERTManager

if __name__ == '__main__':
    HuBERTManager.make_sure_hubert_installed()
    print("hubert_installed")
    HuBERTManager.make_sure_tokenizer_installed()
    print("tokenizer_installed")