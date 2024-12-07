from common_tools.ScriptNotepadTool import ScriptNotepadTool
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def test_scriptwriter_interaction():
    # Create instances for both scriptwriters
    sw1 = ScriptNotepadTool(agent_id="Scriptwriter 1", action="view", content=None)
    sw2 = ScriptNotepadTool(agent_id="Scriptwriter 2", action="view", content=None)

    # Test scenario 1: Basic writing and viewing
    logger.info("=== Test Scenario 1: Basic writing and viewing ===")
    
    # Scriptwriter 1 writes initial content
    response = ScriptNotepadTool(
        agent_id="Scriptwriter 1",
        action="edit",
        content="INT. COFFEE SHOP - DAY\n\nA busy coffee shop filled with the morning rush.",
        replace=True
    ).run()
    logger.info(f"SW1 writes initial scene: {response}")
    
    # Scriptwriter 2 views content
    response = sw2.run()
    logger.info(f"SW2 views content: {response['notepad_content']}")

    # Test scenario 2: Concurrent editing attempt
    logger.info("\n=== Test Scenario 2: Concurrent editing attempt ===")
    
    # Scriptwriter 1 starts editing
    response = ScriptNotepadTool(
        agent_id="Scriptwriter 1",
        action="edit",
        content="SARAH (25, barista) expertly navigates the espresso machine.",
        replace=False
    ).run()
    logger.info(f"SW1 adds character: {response}")
    
    # Scriptwriter 2 attempts to edit immediately
    response = ScriptNotepadTool(
        agent_id="Scriptwriter 2",
        action="edit",
        content="Through the window, we see the city waking up.",
        replace=False
    ).run()
    logger.info(f"SW2 attempts to add description: {response}")

    # Test scenario 3: Lock timeout
    logger.info("\n=== Test Scenario 3: Lock timeout ===")
    
    # Scriptwriter 1 locks the notepad
    response = ScriptNotepadTool(
        agent_id="Scriptwriter 1",
        action="edit",
        content="CUSTOMER (O.S.)\nCan I get a vanilla latte?",
        replace=False
    ).run()
    logger.info(f"SW1 adds dialogue: {response}")
    
    # Wait for lock to expire
    logger.info("Waiting for lock timeout...")
    time.sleep(5)  # Wait less than timeout to show it's still locked
    
    # Scriptwriter 2 attempts to edit
    response = ScriptNotepadTool(
        agent_id="Scriptwriter 2",
        action="edit",
        content="SARAH\nOne vanilla latte coming right up!",
        replace=False
    ).run()
    logger.info(f"SW2 attempts to add response dialogue: {response}")
    
    # Wait for full timeout
    logger.info("Waiting for full lock timeout...")
    time.sleep(60)  # Wait for lock to expire
    
    # Scriptwriter 2 tries again after timeout
    response = ScriptNotepadTool(
        agent_id="Scriptwriter 2",
        action="edit",
        content="SARAH\nOne vanilla latte coming right up!",
        replace=False
    ).run()
    logger.info(f"SW2 tries again after timeout: {response}")

    # Final view of content
    logger.info("\n=== Final Content ===")
    response = sw1.run()
    logger.info(f"Final script content:\n{response['notepad_content']}")
    logger.info("\nEdit History:")
    for entry in response['edit_history']:
        logger.info(f"- {entry['agent_id']} performed {entry['action']}")

if __name__ == "__main__":
    test_scriptwriter_interaction() 