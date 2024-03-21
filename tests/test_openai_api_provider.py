from typing import Optional

from faker import Faker
from faker_openai_api_provider import OpenAiApiProvider

fake = Faker()
fake.add_provider(OpenAiApiProvider)


def assert_is_functional_id(
    id: Optional[str],
    expected_prefix: str,
    sep: str = "_",
) -> None:
    assert id is not None
    prefix, suffix = id.split(sep)
    assert prefix == expected_prefix
    assert len(suffix) == 24


def test_fake_chat_completion_id():
    chat_completion_id = fake.openai().chat.completion.id()
    assert_is_functional_id(chat_completion_id, "chatcmpl")


def test_fake_file_id():
    file_id = fake.openai().file.id()
    assert_is_functional_id(file_id, "file", "-")


def test_fake_assistant_id():
    assistant_id = fake.openai().beta.assistant.id()
    assert_is_functional_id(assistant_id, "asst")


def test_fake_thread_id():
    thread_id = fake.openai().beta.thread.id()
    assert_is_functional_id(thread_id, "thread")


def test_fake_message_id():
    message_id = fake.openai().beta.thread.message.id()
    assert_is_functional_id(message_id, "msg")


def test_fake_run_id():
    run_id = fake.openai().beta.thread.run.id()
    assert_is_functional_id(run_id, "run")


def test_fake_run_step_id():
    run_step_id = fake.openai().beta.thread.run.step.id()
    assert_is_functional_id(run_step_id, "step")


def test_fake_run_step_step_details_tool_call_id():
    tool_call_id = fake.openai().beta.thread.run.step.step_details.tool_call.id()
    assert_is_functional_id(tool_call_id, "call")
