from playwright.sync_api import sync_playwright, expect

def test_i18n(page):
    page.goto("http://localhost:8000")

    # Helper function to change language and check description
    def check_language_description(lang_abbr, expected_text):
        current_lang = page.locator("#current-lang").inner_text()
        if current_lang != lang_abbr:
            # Open the language menu
            page.locator("#current-lang").click()
            # Wait for options to be visible
            page.locator("#lang-options").wait_for(state="visible")
            # Click the desired language
            page.locator(f"#lang-options .lang-icon:has-text('{lang_abbr}')").click()
        # Wait for the description to update
        expect(page.locator("#description")).to_have_text(expected_text)

    # The page might load in 'pt' or the browser's 'en'.
    # Let's start by explicitly setting it to a known state.
    # To avoid issues with the initial state, we'll cycle through all languages.

    check_language_description("EN", "Download the route in Portuguese:")
    check_language_description("ES", "Descarga la ruta en Portugués:")
    check_language_description("FR", "Téléchargez l'itinéraire en Portugais :")
    check_language_description("PT", "Descarregue o roteiro em Português:")
