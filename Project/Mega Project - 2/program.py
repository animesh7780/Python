import pyautogui
import pyperclip
import time

def click_and_drag(click_position, start_drag, end_drag):
    """
    Automates clicking an icon and selecting text via a drag operation.
    The selected text is copied to the clipboard and returned.

    Args:
    - click_position: Tuple of (x, y) for clicking the icon.
    - start_drag: Tuple of (x, y) to start the drag operation.
    - end_drag: Tuple of (x, y) to end the drag operation.

    Returns:
    - The text copied to the clipboard.
    """
    # Click on the icon
    pyautogui.click(click_position)
    time.sleep(1)  # Wait for the app to respond

    # Drag to select the text
    pyautogui.moveTo(start_drag)
    pyautogui.mouseDown()  # Start the drag
    pyautogui.moveTo(end_drag, duration=1)  # Drag to the end position
    pyautogui.mouseUp()  # Release the drag

    # Copy the selected text to clipboard
    pyautogui.hotkey("ctrl", "c")  # Works for Windows/Linux
    time.sleep(0.5)  # Give some time for the clipboard to update

    # Retrieve the copied text from the clipboard
    copied_text = pyperclip.paste()
    return copied_text

if __name__ == "__main__":
    # Define positions
    click_position = (78, 1057)  # Icon position
    start_drag = (770, 287)      # Start of text selection
    end_drag = (1706, 933)       # End of text selection

    # Call the function and print the result
    extracted_text = click_and_drag(click_position, start_drag, end_drag)
    print("Extracted Text:\n", extracted_text)
