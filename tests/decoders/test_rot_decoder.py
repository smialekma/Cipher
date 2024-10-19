import pytest

from src.decoders.rot_decoder import Rot13Decoder, Rot47Decoder


class TestRot13DecoderDecode:

    @pytest.fixture()
    def decoder(self):
        return Rot13Decoder()

    @pytest.mark.parametrize(
        "test_input, expected",
        [("jvgnz", "witam"), ("swqxy", "fjdkl"), ("neohm", "arbuz")],
    )
    def test_should_return_decoded_words(self, decoder, test_input, expected):
        assert decoder.decode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [("Xbolłn zn znłl obx", "Kobyła ma mały bok"), ("Nyn zn xbgn", "Ala ma kota")],
    )
    def test_should_return_decoded_sentences(self, decoder, test_input, expected):
        assert decoder.decode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("Qmvrń", "Dzień"), ("qMvrŃ qBoel", "dZieŃ dObry")]
    )
    def test_should_return_letter_case(self, decoder, test_input, expected):
        assert decoder.decode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("Urw520", "Hej520"), ("89402", "89402")]
    )
    def test_should_return_numbers_without_decoding(
        self, decoder, test_input, expected
    ):
        assert decoder.decode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("Urw, Zntqn!", "Hej, Magda!"), ("$$%@", "$$%@")]
    )
    def test_should_return_punctuation_without_decoding(
        self, decoder, test_input, expected
    ):
        assert decoder.decode(test_input) == expected


class TestRot13DecoderEncode:

    @pytest.fixture()
    def decoder(self):
        return Rot13Decoder()

    @pytest.mark.parametrize(
        "test_input,expected",
        [("witam", "jvgnz"), ("fjdkl", "swqxy"), ("arbuz", "neohm")],
    )
    def test_should_return_encoded_words(self, decoder, test_input, expected):
        assert decoder.encode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [("Kobyła ma mały bok", "Xbolłn zn znłl obx"), ("Ala ma kota", "Nyn zn xbgn")],
    )
    def test_should_return_encoded_sentences(self, decoder, test_input, expected):
        assert decoder.encode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("Dzień", "Qmvrń"), ("dZieŃ dObry", "qMvrŃ qBoel")]
    )
    def test_should_return_letter_case(self, decoder, test_input, expected):
        assert decoder.encode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("Hej520", "Urw520"), ("89402", "89402")]
    )
    def test_should_return_numbers_without_decoding(
        self, decoder, test_input, expected
    ):
        assert decoder.encode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("Hej, Magda!", "Urw, Zntqn!"), ("$$%@", "$$%@")]
    )
    def test_should_return_punctuation_without_decoding(
        self, decoder, test_input, expected
    ):
        assert decoder.encode(test_input) == expected


class TestRot47DecoderDecode:

    @pytest.fixture()
    def decoder(self):
        return Rot47Decoder()

    @pytest.mark.parametrize(
        "test_input,expected",
        [("H:E2>", "witam"), ("7;5<=", "fjdkl"), ("2C3FK", "arbuz")],
    )
    def test_should_return_decoded_words(self, decoder, test_input, expected):
        assert decoder.decode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [("z@3Jł2 >2 >2łJ 3@<", "Kobyła ma mały bok"), ("p=2 >2 <@E2", "Ala ma kota")],
    )
    def test_should_return_decoded_sentences(self, decoder, test_input, expected):
        assert decoder.decode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("sK:6ń", "Dzień"), ("5+:6Ń 5~3CJ", "dZieŃ dObry")]
    )
    def test_should_correctly_return_letter_case(self, decoder, test_input, expected):
        assert decoder.decode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("w6;da_", "Hej520"), ("ghc_a", "89402")]
    )
    def test_should_correctly_decode_numbers(self, decoder, test_input, expected):
        assert decoder.decode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("w6;[ |2852P", "Hej, Magda!"), ("SSTo", "$$%@")]
    )
    def test_should_correctly_decode_punctuation(self, decoder, test_input, expected):
        assert decoder.decode(test_input) == expected


class TestRot47DecoderEncode:

    @pytest.fixture()
    def decoder(self):
        return Rot47Decoder()

    @pytest.mark.parametrize(
        "test_input,expected",
        [("witam", "H:E2>"), ("fjdkl", "7;5<="), ("arbuz", "2C3FK")],
    )
    def test_should_return_encoded_words(self, decoder, test_input, expected):
        assert decoder.encode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [("Kobyła ma mały bok", "z@3Jł2 >2 >2łJ 3@<"), ("Ala ma kota", "p=2 >2 <@E2")],
    )
    def test_should_return_encoded_sentences(self, decoder, test_input, expected):
        assert decoder.encode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("Dzień", "sK:6ń"), ("dZieŃ dObry", "5+:6Ń 5~3CJ")]
    )
    def test_should_correctly_encode_letter_case(self, decoder, test_input, expected):
        assert decoder.encode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("Hej520", "w6;da_"), ("89402", "ghc_a")]
    )
    def test_should_correctly_encode_numbers(self, decoder, test_input, expected):
        assert decoder.encode(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected", [("Hej, Magda!", "w6;[ |2852P"), ("$$%@", "SSTo")]
    )
    def test_should_correctly_encode_punctuation(self, decoder, test_input, expected):
        assert decoder.encode(test_input) == expected
